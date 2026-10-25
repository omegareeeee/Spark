type UserInputType = {
    value: string,
    handleValueChange: (value: string) => void
}

const UserInput = ({value, handleValueChange}: UserInputType) => {
    return (
        <div>
            <input
                value={value}
                onChange={e => handleValueChange(e.target.value)}
            />
        </div>
    );
};