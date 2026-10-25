import { createContext } from "react";
import type { Idea } from "../pages/SearchPage"

type IdeasContextType = {
    ideas: Idea[],
    handleIdeasChange: (ideas: Idea[]) => void
};

const IdeasContext = createContext<IdeasContextType | null>(null);

export default IdeasContext;