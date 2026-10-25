import { useContext, useEffect, useRef, useState } from "react";
import type { Idea } from "../pages/SearchPage";
import gsap from "gsap";
import ChosenIdContext from "../contexts/ChosenIdContext";

const Node = ({x, y, id}: Idea & {r: number}) => {
    const container = useRef<SVGGElement | null>(null);
    const wrapper = useRef<SVGGElement | null>(null);
    const tl = useRef<GSAPTimeline | null>(null);
    const chosenIdContext = useContext(ChosenIdContext);


    return (
        <g  transform={`translate(${x}, ${y})`}
            className="cursor-pointer"
               
        >
            <g ref={wrapper}
                transform="scale(1)"
            >
                <circle
                    className="hover:scale-[1.2] transition-all active:scale-[0.8]"
                    fill="#D7F5F8"
                    onClick={() => chosenIdContext?.handleChosenIdChange(id)}
                    r={24}
                    stroke="#AAC2C4"
                    strokeWidth={4}
                />
            </g>
        </g>
    );
};

export default Node;