type UserInputType = {
    value: string,
    handleValueChange: (value: string) => void,
    placeHolder: string,
    isLargeText: boolean
}

const UserInput = ({value, handleValueChange, placeHolder, isLargeText}: UserInputType) => {
    return (
        <div className="relative self-center">
            {isLargeText ? (
                <textarea
                    className="font-bold text-dark_15 focus:outline-none bg-cream_90 z-20 relative p-[.5em] border-[.2em] border-dark_15 rounded-[.5em] -translate-[.2em] h-[20rem] overflow-scroll w-[25vw]"
                    value={value}
                    onChange={e => handleValueChange(e.target.value)}
                    placeholder={placeHolder}
            />) : (<input
                className="font-bold text-dark_15 focus:outline-none bg-cream_90 z-20 relative p-[.5em] border-[.2em] border-dark_15 rounded-[.5em] -translate-[.2em] w-[25vw]"
                value={value}
                onChange={e => handleValueChange(e.target.value)}
                placeholder={placeHolder}
            />)}
            <div className="absolute w-full h-full bg-dark_15 top-0 left-0 rounded-[.5em] z-10"></div>
        </div>
    );
};

export default UserInput;