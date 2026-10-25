

class Node {
    public x: number;
    public y: number;
    public idea: string;
    public container!: SVGGElement | null;
    public wrapper!: SVGElement | null;
    public dom!: SVGCircleElement | null;

    public constructor(x: number, y: number, idea: string) {
        this.x = x;
        this.y = y;
        this.idea = idea;
    }
}