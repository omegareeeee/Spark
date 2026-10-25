import type { Idea } from "../pages/SearchPage";

const FACTOR = 200, R_MIN = 18, R_MAX = 44, PAD = 6;

export function resolveOverlaps(ideas: Idea[]) {
    const maxCount = Math.max(1, ...ideas.map(i => i.comment_count));
    const nodes = ideas.map(i => ({
        ...i,
        r: R_MIN + (R_MAX - R_MIN) * Math.sqrt(i.comment_count / maxCount),
        x: i.x * FACTOR,
        y: i.y * FACTOR,
    }));

    for (let iter = 0; iter < 100; iter++) {
        let moved = false;
        for (let a = 0; a < nodes.length; a++) {
            for (let b = a + 1; b < nodes.length; b++) {
                let dx = nodes[b].x - nodes[a].x;
                let dy = nodes[b].y - nodes[a].y;
                let d = Math.hypot(dx, dy);
                const min = nodes[a].r + nodes[b].r + PAD;  
                if (d >= min) continue;
                if (d < 1e-6) { dx = Math.cos(a + b); dy = Math.sin(a + b); d = 1; }
                const push = (min - d) / 2;
                const ux = dx / d, uy = dy / d;
                nodes[a].x -= ux * push;  nodes[a].y -= uy * push;
                nodes[b].x += ux * push;  nodes[b].y += uy * push;
                moved = true;
            }
        }
        if (!moved) break;
    }
    return nodes;
}