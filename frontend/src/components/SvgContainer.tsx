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

const getFingerDistance = (touch1, touch2) => {
    const finger1 = {
        x: touch1.clientX,
        y: touch1.clientY
    };
    const finger2 = {
        x: touch2.clientX,
        y: touch2.clientY
    };

    const dx = finger1.x - finger2.x;
    const dy = finger1.y - finger2.y;

    return Math.sqrt(dx*dx + dy*dy);
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

     function touchMove(event) {
        event.preventDefault();
        const touches = [...event.touches];
        if (touches.length == 2) {
            const finger1 = {
                x: touches[0].clientX,
                y: touches[0].clientY
            };
            const finger2 = {
                x: touches[1].clientX,
                y: touches[1].clientY
            };

            const midPointX = (finger1.x + finger2.x)/2;
            const midPointY = (finger1.y + finger2.y)/2;
            const startDis = fingerStartDis;
            const distance = getFingerDistance(touches[0], touches[1]);
            const zoomFactor = distance > startDis ? ZOOM_IN_FACTOR : ZOOM_OUT_FACTOR;
            
            const point = container.current.createSVGPoint();
            point.x = midPointX;
            point.y = midPointY;

            const svgMidPoint = getSVGPoint({x: midPointX, y: midPointY});
            const newHeight = viewBox.height*zoomFactor;
            const newWidth = viewBox.width*zoomFactor;
 
            setFingerStartDis(distance);
            setViewBox({
                xMin: svgMidPoint.x - (svgMidPoint.x - viewBox.xMin) * zoomFactor, 
                yMin: svgMidPoint.y - (svgMidPoint.y - viewBox.yMin) * zoomFactor, 
                width: newWidth,
                height: newHeight
            });
        }
    }

    function touchStart(event) {
        event.preventDefault();
        const touches = [...event.touches];
        if (touches.length == 2) {
            const distance = getFingerDistance(touches[0], touches[1]);
            setFingerStartDis(distance);
        }
        
    }
    
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