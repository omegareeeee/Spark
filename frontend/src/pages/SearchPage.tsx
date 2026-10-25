import Button from "../components/Button";
import SearchComp from "../components/SearchComp";

const SearchPage = () => {
    return (
        <div>
            <div className="fixed left-1/2 -translate-x-1/2 top-[2rem] flex bg-cream_90 p-[1em] rounded-[1em] gap-[3rem]">
                <SearchComp/>
                <Button>
                    Add
                </Button>
            </div>
        </div>
    );
};

export default SearchPage;