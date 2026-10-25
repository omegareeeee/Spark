import { useCallback, useRef, useState, type ReactNode } from "react";


type SvgContainerProp = {
    xMin: number,
    yMin: number,
    children: ReactNode,
    initial_zoom: number
};

type ViewBox = {
    xMin: number,
    yMin: number,
    width: number,
    height: number
}

const SvgContainer = ({xMin, yMin, children, initial_zoom}: SvgContainerProp) => {

    const [viewBox, setViewBox] = useState<ViewBox>({
        xMin: xMin,
        yMin: yMin,
        width: 4500 * initial_zoom,
        height: 4500 * initial_zoom
    });

    const container = useRef<SVGSVGElement | null>(null);

     const getSVGPoint = useCallback((point: {x: number, y: number}) => {
        if (container.current) {
            const p = container.current.createSVGPoint();
            p.x = point.x;
            p.y = point.y;
            
            return p.matrixTransform(container.current.getScreenCTM().inverse());
        }

    }, [container.current]);
    
    return (
        <svg
            ref={container}
            viewBox={`${viewBox.xMin} ${viewBox.yMin} ${viewBox.width} ${viewBox.height}`}
            preserveAspectRatio="xMidYMid meet"
            className="w-screen h-screen"
        >
            {children}
        </svg>
    );
};

export default SvgContainer;