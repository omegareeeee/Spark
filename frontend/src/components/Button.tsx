import type { ReactNode } from "react";

const Button = ({children}: {children: ReactNode}) => {
    return (
        <button className="cursor-pointer">
            {children}
        </button>
    );
};

export default Button;