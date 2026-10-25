import type { ReactNode } from "react";

const Button = ({children}: {children: ReactNode}) => {
    return (
        <button className="cursor-pointer relative">
            <div className="border-[.2em] py-[.5em] px-[1.5em] rounded-[.5em] font-bold border-dark_15 z-30 relative -translate-[.2em] bg-cream_90 text-dark_15">
                {children}
            </div>
            <div className="w-full h-full bg-dark_15 absolute top-0 left-0 rounded-[.5em] z-20"></div>
        </button>
    );
};

export default Button;