import AddModel from "../components/AddModel";
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
            <div className="fixed min-h-screen right-0">
                <AddModel/>
            </div>
        </div>
    );
};

export default SearchPage;