import type { Idea } from "../pages/SearchPage";

const fetchIdea = async (): Promise<Idea[]> => {
    const response = await fetch(import.meta.env.VITE_API_URL + "ideas");
    const body = (await response.json()) as Idea[];
    return body;
};

export default fetchIdea;