import { createContext } from "react";

type chosenIdContextType = {
    chosenId: string | null,
    handleChosenIdChange: (id: string | null) => void
}

const ChosenIdContext = createContext<chosenIdContextType | null>(null);

export default ChosenIdContext;