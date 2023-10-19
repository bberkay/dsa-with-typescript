/*
    Breadth First Search

    Breadth First Search (BFS) is a graph traversal algorithm where we start at a root node and keep traversing down until we reach the end. If we reach a node that has no children, we backtrack to the previous node and continue the same process.

    In Real Life:
        1. Web Crawlers: DFS is used to build web crawlers. Web crawlers start from a root page, and follow links to other pages. DFS is used to decide which pages to follow, and which to ignore.
        2. Finding Connected Components: DFS can be used to find all the connected components in an undirected graph. The graph is traversed using DFS, and each time a new vertex is reached, a new connected component is discovered.
        3. Topological Sorting: DFS can be used to topologically sort a graph. The graph is traversed using DFS, and each time a vertex is finished expanding, it is added to the topological sort.

    Description and comments created by chatgpt and github copilot
 */