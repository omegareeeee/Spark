import type { Comment } from "../components/IdeaDetails";

type AddCommentRequest = {
    author_name: string,
    text: string,
    iid: string
};


const AddComment = async (request: AddCommentRequest): Promise<Comment> => {
    const response = await fetch(import.meta.env.VITE_API_URL + `ideas/${request.iid}/comments`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(request)
    });
    const body = await response.json() as Comment;
    
    return body;
};

export default AddComment;