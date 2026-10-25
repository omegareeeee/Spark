import { useState } from "react";
import Button from "./Button";

const SearchComp = () => {
    const [query, setQuery] = useState<string>("");
    
    return (
        <div>
            <input
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