import { useState } from "react";
import UserInput from "./UserInput";
import Button from "./Button";

type AddModalProp = {
    closeModel: () => void
}

const AddModel = ({closeModel}: AddModalProp) => {
    const [name, setName] = useState<string>("");
    const [linkedin, setLinkedin] = useState<string>("");
    const [idea, setIdea] = useState<string>("");
    const [des, setDes] = useState<string>("");
    const [github, setGitHub] = useState<string>("");

    return (
        <form className="bg-cream_90 flex flex-col border-[.2em] rounded-tl-[1em] rounded-bl-[1em] grow overflow-hidden border-dark_15">
            <div className="flex items-center justify-center px-[3em] border-b-[.2em] border-dark_15 relative">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" className="w-[2rem] cursor-pointer absolute left-[1rem]" onClick={() => closeModel()}>
                    <path fill="#272827" d="M320 576C461.4 576 576 461.4 576 320C576 178.6 461.4 64 320 64C178.6 64 64 178.6 64 320C64 461.4 178.6 576 320 576zM231 231C240.4 221.6 255.6 221.6 264.9 231L319.9 286L374.9 231C384.3 221.6 399.5 221.6 408.8 231C418.1 240.4 418.2 255.6 408.8 264.9L353.8 319.9L408.8 374.9C418.2 384.3 418.2 399.5 408.8 408.8C399.4 418.1 384.2 418.2 374.9 408.8L319.9 353.8L264.9 408.8C255.5 418.2 240.3 418.2 231 408.8C221.7 399.4 221.6 384.2 231 374.9L286 319.9L231 264.9C221.6 255.5 221.6 240.3 231 231z"/>
                </svg>
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