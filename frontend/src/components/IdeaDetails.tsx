import { useContext, useEffect, useState } from "react";
import type { Idea } from "../pages/SearchPage";
import Button from "./Button";
import ChosenIdContext from "../contexts/ChosenIdContext";
import UserInput from "./UserInput";
import AddComment from "../utils/addComment";
import fetchComments from "../utils/fetchComments";
import IdeasContext from "../contexts/IdeasContext";

export type Comment = {
    idea_id: string,
    author_name: string,
    text: string,
    id: number
};

const IdeaDetails = ({title, author_name, created_at, description, github_url, id}: Idea) => {
    const chosenIdContext = useContext(ChosenIdContext);
    const [comments, setComments] = useState<Comment[]>([]);
    const [input, setInput] = useState("");
    const ideasContext = useContext(IdeasContext);

    useEffect(() => {
        fetchComments(id)
        .then(comments => setComments(comments));
    }, [id]);
    
    return (
        <div className="grow bg-cream_90 max-w-[25rem] border-[.3em] border-dark_15 rounded-tl-[1em] rounded-bl-[1em] overflow-scroll"
        >
            <div className="p-[1.5em] border-b-[.2em]">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" className="w-[2rem] cursor-pointer absolute left-[1rem]"
                onClick={() => {
                    chosenIdContext?.handleChosenIdChange(null);
                }}
                >
                    <path fill="#272827" d="M320 576C461.4 576 576 461.4 576 320C576 178.6 461.4 64 320 64C178.6 64 64 178.6 64 320C64 461.4 178.6 576 320 576zM231 231C240.4 221.6 255.6 221.6 264.9 231L319.9 286L374.9 231C384.3 221.6 399.5 221.6 408.8 231C418.1 240.4 418.2 255.6 408.8 264.9L353.8 319.9L408.8 374.9C418.2 384.3 418.2 399.5 408.8 408.8C399.4 418.1 384.2 418.2 374.9 408.8L319.9 353.8L264.9 408.8C255.5 418.2 240.3 418.2 231 408.8C221.7 399.4 221.6 384.2 231 374.9L286 319.9L231 264.9C221.6 255.5 221.6 240.3 231 231z"/>
                </svg>
                <h1 className="font-bold text-[1.5rem] text-center">{title}</h1>
            </div>
            <div className="flex flex-col gap-4 p-[1.5em] border-b-[.2em]">
                <div>
                    <p>{author_name}</p>
                    <p>{created_at}</p>
                </div>
                <div className="flex flex-col gap-5">
                    <p className="font-medium">
                        {description}
                    </p>
                    {github_url && (
                        <Button>
                            Github Repo
                        </Button>
                    )}
                    <div className="flex flex-col gap-4">
                        <p className="text-[1.5rem] font-bold">Comments</p>
                        <div>
                            <UserInput
                                forComment
                                value={input}
                                handleValueChange={setInput}
                                placeHolder="comment"
                                isLargeText
                            />
                        </div>
                        <Button
                            isDark
                            prop={
                                {
                                    onClick: async () => {
                                        const comment =  await AddComment({
                                            author_name: `user${Math.random() * 100000}`,
                                            text: input,
                                            iid: id
                                        });
                                        const clone = structuredClone(comments);
                                        clone.unshift(comment);
                                        setComments(clone);
                                        ideasContext?.handleIdeasChange(ideasContext.ideas.map(idea => {
                                            const cl = structuredClone(idea);
                                            if (cl.id === id) {
                                                cl.comment_count = cl.comment_count + 1;
                                            }
                                            return cl;
                                        }));
                                    }
                                }
                            }
                        >
                            Add comments
                        </Button>
                    </div>
                    
                </div>
            </div>
            <div className="flex flex-col">
                    {comments.map(comment => (
                      <div className="flex flex-col gap-2 p-4 border-b-[.2em]">
                        <h1 className="font-bold">{comment.author_name}</h1>
                        <p>{comment.text}</p>
                      </div>  
                    ))}
            </div>
        </div>
    );
};

export default IdeaDetails;