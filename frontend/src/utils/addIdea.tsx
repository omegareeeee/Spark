import type { Idea } from "../pages/SearchPage";

type AddIdeaRequest = {
    title: string,
    description: string,
    contact: string,
    author_name: string,
    github_url: string
}

const addIdea = async (request: AddIdeaRequest): Promise<Idea> => {
    const response = await fetch(import.meta.env.VITE_API_URL + "ideas", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(request)
    });
    const body = (await response.json()) as Idea
    return body;
};

export default  addIdea;