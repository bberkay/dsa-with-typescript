/*

    Bellman-Ford Algorithm

    The Bellman-Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph. It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

    In Real Life:
        1. Routing Algorithms: Bellman-Ford is used by routing protocols to compute the shortest path between the source and destination nodes.

    Description and comments created by chatgpt and github copilot
 */

type GraphForBF = {
    vertices: string[],
    edges: {u: string, v: string, w: number}[]
}

function bellmanFord(graph: GraphForBF, source: string): void
{
    
}

const graph: GraphForBF = {
    vertices: ["A", "B", "C", "D", "E"],
    edges: [
        { u: "A", v: "B", w: 4 },
        { u: "A", v: "C", w: 2 },
        { u: "B", v: "C", w: 3 },
        { u: "B", v: "D", w: 2 },
        { u: "B", v: "E", w: 3 },
    ],
}

bellmanFord(graph, "A");