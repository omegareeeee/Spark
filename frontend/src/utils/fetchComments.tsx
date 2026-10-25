import type { Comment } from "../components/IdeaDetails";

const fetchComments = async (iid: string) => {
    const response = await fetch(import.meta.env.VITE_API_URL + `ideas/${iid}/comments`);
    const body = await response.json() as Comment[];
    return body;
};

export default fetchComments;
