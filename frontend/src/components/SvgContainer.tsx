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
};

const ZOOM_IN_FACTOR = 0.95;
const ZOOM_OUT_FACTOR = 1.05;

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

    function wheelZoom(event) {
        event.preventDefault();
        if (event.ctrlKey) {
            const svgPoint = getSVGPoint({x: event.clientX, y: event.clientY});
            const zoomFactor = event.deltaY < 0 ? ZOOM_IN_FACTOR : ZOOM_OUT_FACTOR;
            const newHeight = viewBox.height*zoomFactor;
            const newWidth = viewBox.width*zoomFactor;
            
            setViewBox({
                xMin: svgPoint.x - (svgPoint.x - viewBox.xMin) * zoomFactor, 
                yMin: svgPoint.y - (svgPoint.y - viewBox.yMin) * zoomFactor, 
                width: newWidth,
                height: newHeight
            });
        }
        else {
            const deltaX = event.deltaX*2;
            const deltaY = event.deltaY*2;
            
            setViewBox({
                xMin: viewBox.xMin + deltaX,
                yMin: viewBox.yMin + deltaY,
                width: viewBox.width,
                height: viewBox.height
            })
        }
    };
    
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