type UserInputType = {
    value: string,
    handleValueChange: (value: string) => void,
    placeHolder: string
}

const UserInput = ({value, handleValueChange, placeHolder}: UserInputType) => {
    return (
        <div className="relative">
            <input
                className="font-bold text-dark_15 focus:outline-none bg-cream_90 z-20 relative p-[.5em] border-[.2em] border-dark_15 rounded-[.5em] -translate-[.2em]"
                value={value}
                onChange={e => handleValueChange(e.target.value)}
                placeholder={placeHolder}
            />
            <div className="absolute w-full h-full bg-dark_15 top-0 left-0 rounded-[.5em] z-10"></div>
        </div>
    );
};

export default UserInput;