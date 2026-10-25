import { useEffect, useMemo, useRef, useState } from "react";
import AddModel from "../components/AddModel";
import Button from "../components/Button";
import SearchComp from "../components/SearchComp";
import gsap from "gsap";
import SvgContainer from "../components/SvgContainer";
import Node from "../graph/Node";
import fetchIdea from "../utils/fetchIdeas";
import IdeasContext from "../contexts/IdeasContext";
import { resolveOverlaps } from "../utils/resolveOverlaps";
import IdeaDetails from "../components/IdeaDetails";
import ChosenIdContext from "../contexts/ChosenIdContext";

export type Idea = {
    id: string,
    x: number,
    y: number,
    title: string,
    description: string,
    author_name: string,
    github_url: string,
    created_at: string
};

const SearchPage = () => {
    const [showAddModal, setShowAddModal] = useState<boolean>(false);
    const addModelContainer = useRef<HTMLDivElement | null>(null);
    const ideaModalContainer =  useRef<HTMLDivElement | null>(null);
    const [ideas, setIdeas] = useState<Idea[]>([]);
    const [chosenId, setChosenId] = useState<string | null>(null);

    const chosenIdea = useMemo(() => {
        for (let idea of ideas) {
            if (idea.id === chosenId) {
                return idea;
            }
        }
        return null;
    }, [chosenId]);


    const chosenIdContext = useMemo(() => {
        return {
            chosenId: chosenId,
            handleChosenIdChange: setChosenId
        }
    }, [chosenId]);
    
    

    const ideaContext = useMemo(() => {
        return {
            ideas: ideas,
            handleIdeasChange: setIdeas
        }
    }, [ideas]);

    const nodes = useMemo(() => resolveOverlaps(ideas), [ideas]);
    
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

    useEffect(() => {
        gsap.to(ideaModalContainer.current, {
            x: chosenId === null ? "100%" : "0",
            ease: "power2.inOut"
        });

    }, [chosenId]);


    useEffect(() => {
        fetchIdea()
        .then(ideas => {
            setIdeas(ideas);
        });
    }, []);

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
                <IdeasContext
                    value={
                        ideaContext
                    }
                >
                    <AddModel
                        closeModel={() => setShowAddModal(false)}
                />
                </IdeasContext>
            </div>
            <ChosenIdContext
                value={chosenIdContext}
            >
                <div 
                    className="fixed right-0 flex flex-col h-screen translate-x-full"
                    ref={ideaModalContainer}
                >
                    {chosenIdea && <IdeaDetails {...chosenIdea}/>}
                </div>

                <SvgContainer
                    xMin={0}
                    yMin={0}
                    initial_zoom={0.5}
                >
                {nodes.map(node => (
                    <Node {...node} key={node.id}/>
                ))}
                </SvgContainer>
            </ChosenIdContext>
        </div>
    );
};

export default SearchPage;