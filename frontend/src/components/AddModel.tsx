import { useState } from "react";
import UserInput from "./UserInput";
import Button from "./Button";


const AddModel = () => {
    const [name, setName] = useState<string>("");
    const [linkedin, setLinkedin] = useState<string>("");
    const [idea, setIdea] = useState<string>("");
    const [des, setDes] = useState<string>("");
    const [github, setGitHub] = useState<string>("");

    return (
        <form className="bg-cream_90 flex flex-col border-[.2em] rounded-tl-[1em] rounded-bl-[1em] grow overflow-scroll border-dark_15">
            <div className="flex items-center justify-center px-[3em] border-b-[.2em] border-dark_15">
                <h1 className="font-bold text-[1.5rem] py-[.5em]">Add Your Idea</h1>
            </div>
            <div className="flex-col flex justify-around grow p-[1.5em]">   
                <UserInput
                    value={name}
                    handleValueChange={setName}
                    placeHolder="Your name"
                    isLargeText={false}
                />
                <UserInput
                    value={linkedin}
                    handleValueChange={setLinkedin}
                    placeHolder="Linkedin"
                    isLargeText={false}
                />
                <UserInput
                    value={idea}
                    handleValueChange={setIdea}
                    placeHolder="idea's title"
                    isLargeText={false}
                />
                <UserInput
                    value={des}
                    handleValueChange={setDes}
                    placeHolder="Description of your idea..."
                    isLargeText
                />
                <UserInput
                    value={github}
                    handleValueChange={setGitHub}
                    placeHolder="GitHub repo (Optional)"
                    isLargeText={false}
                />
                <Button
                    isDark
                >
                    <p>Add</p>
                </Button>
            </div>
        </form>
    );
};

export default AddModel;