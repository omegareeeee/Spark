import type { ComponentProps, ReactNode } from "react";

type ButtonProp = {
    children: ReactNode,
    isDark?: boolean,
    prop: ComponentProps<'button'>;
};


const Button = ({children, isDark, ...rest}: ButtonProp) => {
    let clssName = "border-[.2em] py-[.5em] px-[1.5em] rounded-[.5em] font-bold z-30 relative -translate-[.3em] bg-cream_90 active:translate-0 transition-all hover:-translate-[.2em]";
    let shadowClass = "w-full h-full bg-dark_15 absolute top-0 left-0 rounded-[.5em] z-20";
    if (isDark) {
        clssName += " bg-dark_15 border-gray_15 text-cream_90";
        shadowClass += " bg-gray_15";
    }
    else {
        clssName += " bg-cream_90 border-dark_15 text-dark_15";
        shadowClass += " bg-dark_15";
    }
    return (
        <button 
            className="cursor-pointer relative"
            {...rest.prop}
        >
            <div className={clssName}>
                {children}
            </div>
            <div className={shadowClass}></div>
        </button>
    );
};

export default Button;