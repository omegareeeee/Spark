import Button from "../components/Button";
import SearchComp from "../components/SearchComp";

const SearchPage = () => {
    return (
        <div>
            <div className="fixed left-1/2 -translate-x-1/2 top-[1rem] flex">
                <SearchComp/>
                <Button>
                    Add
                </Button>
            </div>
        </div>
    );
};

export default SearchPage;