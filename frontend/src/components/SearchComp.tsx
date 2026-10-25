import { useState } from "react";
import Button from "./Button";

const SearchComp = () => {
    const [query, setQuery] = useState<string>("");
    
    return (
        <div className="flex gap-[1rem]">
            <input
                className="focus:outline-none p-[.5em] font-bold border-[.2em] rounded-[.5em] border-dark_15"
                placeholder="Your idea"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <Button>
                Search
            </Button>
        </div>
    );
};

export default SearchComp;