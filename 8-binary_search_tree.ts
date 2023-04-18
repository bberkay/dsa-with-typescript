/*
Binary Search Tree
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
-It is called a binary tree because each tree node has a maximum of two children.
-It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.

The properties that separate a binary search tree from a regular binary tree is
-All nodes of left subtree are less than the root node
-All nodes of right subtree are more than the root node
-Both subtrees of each node are also BSTs i.e. they have the above two properties

Applications
- In multilevel indexing in the database, for dynamic sorting, For managing virtual memory areas in Unix kernel
*/
class BSTNode{
    public left:BSTNode;
    public right:BSTNode;
    public value:number | null;

    constructor(data:number){
        this.value = data;
    }
}

function addToBST(bst:BSTNode, node:BSTNode){
    if(node.value! > bst.value!){
        if(!bst.right)
            bst.right = node
        else
            addToBST(bst.right, node);
    }
    else if(node.value! < bst.value!){
        if(!bst.left)
            bst.left = node
        else
            addToBST(bst.left, node);
    }
}

function searchOnBST(bst:BSTNode, search:number): boolean
{
    if(!bst)
        return false;
    if(bst.value == search)
        return true;
    if(searchOnBST(bst.right, search))
        return true
    if(searchOnBST(bst.left, search))
        return true
    return false;
}

function traverseInOrder(bst:BSTNode)
{
    if(bst){
        traverseInOrder(bst.left);
        console.log(bst.value);
        traverseInOrder(bst.right);
    }
}

function minOfBST(bst:BSTNode): BSTNode
{
    if(!bst.left)
        return bst;
    return minOfBST(bst.left);
}

function maxOfBST(bst:BSTNode): BSTNode
{
    if(!bst.right)
        return bst;
    return maxOfBST(bst.right);
}

function deleteFromBST(bst:BSTNode, data:number): BSTNode|undefined|null
{
    if(!bst)
        return null;

    if(bst.value == data){
        if(!(bst.right && bst.left)){
            bst.value = null;
            return bst   
        }
        else if(!bst.right && bst.left){
            let temp = maxOfBST(bst.left).value;
            bst.value = temp;
            deleteFromBST(bst.left, temp!);
        }else{
            let temp = minOfBST(bst.right).value;
            bst.value = temp;
            deleteFromBST(bst.right, temp!);
        }
        return bst;
    }
    else if(data > bst.value!)  
        bst.right = deleteFromBST(bst.right, data)!;
    else if(data < bst.value!)
        bst.left = deleteFromBST(bst.left, data)!;

    return bst;
}

let root = new BSTNode(8);
let node2 = new BSTNode(3);
let node3 = new BSTNode(10);
let node4 = new BSTNode(1);
let node5 = new BSTNode(6);
let node6 = new BSTNode(4);
let node7 = new BSTNode(7);
let node8 = new BSTNode(14);

console.log("\n\n========================================");

addToBST(root, node2);
addToBST(root, node3);
addToBST(root, node4);
addToBST(root, node5);
addToBST(root, node6);
addToBST(root, node7);
addToBST(root, node8);
//traverseInOrder(root);
//console.log(searchOnBST(root, 14));
//console.log(minOfBST(root).value);
//console.log(maxOfBST(root).value);
root = deleteFromBST(root, 3)!;
traverseInOrder(root);

console.log("========================================\n\n");
