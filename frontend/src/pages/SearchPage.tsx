import { useEffect, useRef, useState } from "react";
import AddModel from "../components/AddModel";
import Button from "../components/Button";
import SearchComp from "../components/SearchComp";
import gsap from "gsap";
import SvgContainer from "../components/SvgContainer";

const SearchPage = () => {
    const [showAddModal, setShowAddModal] = useState<boolean>(false);
    const addModelContainer = useRef<HTMLDivElement | null>(null);
    
    useEffect(() => {
        if (showAddModal) {
            gsap.to(addModelContainer.current, {
                x: "0",
                ease: "power2.inOut"
                
            })
        }
        else {
             gsap.to(addModelContainer.current, {
                x: "100%",
                ease: "power2.inOut"
            })
        }
    }, [showAddModal]);

    return (
        <div>
            <div className="fixed left-1/2 -translate-x-1/2 top-[2rem] flex bg-cream_90 p-[1em] rounded-[1em] gap-[3rem]">
                <SearchComp/>
                <Button
                    prop={{
                        onClick: () => setShowAddModal(true)
                    }}
                >
                    Add
                </Button>
            </div>
            <div 
                className="fixed right-0 translate-x-full flex flex-col h-screen"
                ref={addModelContainer}
            >
               <AddModel
                    closeModel={() => setShowAddModal(false)}
               />
            </div>
            <SvgContainer
                xMin={0}
                yMin={0}
                initial_zoom={0.5}
            >
                <rect
                    x={0}
                    y={0}
                    width={100}
                    height={100}
                    fill="red"
                />
            </SvgContainer>
        </div>
    );
};

export default SearchPage;