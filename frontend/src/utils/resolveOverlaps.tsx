// utils/resolveOverlaps.ts
import { forceSimulation, forceX, forceY, forceCollide } from "d3-force";
import type { Idea } from "../pages/SearchPage";

const FACTOR = 200, R = 24, PAD = 6;

export function resolveOverlaps(ideas: Idea[]) {
    const nodes = ideas.map(i => ({
        ...i,
        tx: i.x * FACTOR, ty: i.y * FACTOR,   // anchor (true position)
        x:  i.x * FACTOR, y:  i.y * FACTOR,   // mutated by the simulation
    }));
    forceSimulation(nodes as any)
        .force("x", forceX((d: any) => d.tx).strength(0.3))
        .force("y", forceY((d: any) => d.ty).strength(0.3))
        .force("collide", forceCollide(R + PAD))
        .stop()
        .tick(150);
    return nodes;
}