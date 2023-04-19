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
        // if node value is greater than bst value
        // then it should be added to the right of bst
        if(!bst.right)
            bst.right = node
        else
            addToBST(bst.right, node);
    }
    else if(node.value! < bst.value!){
        // if node value is less than bst value
        // then it should be added to the left of bst
        if(!bst.left)
            bst.left = node
        else
            addToBST(bst.left, node);
    }
}

function searchOnBST(bst:BSTNode, search:number): boolean
{
    // if bst is null or search is not found
    if(!bst)
        return false;
    // if search is found
    if(bst.value == search)
        return true;
    // if search is not found then search on right subtree
    if(searchOnBST(bst.right, search))
        return true
    // if search is not found then search on left subtree
    if(searchOnBST(bst.left, search))
        return true
    return false;
}

function traverseInOrder(bst:BSTNode)
{
    // left -> root -> right
    if(bst){
        traverseInOrder(bst.left);
        console.log(bst.value);
        traverseInOrder(bst.right);
    }
}

function minOfBST(bst:BSTNode): BSTNode
{
    // get the left most node
    if(!bst.left)
        return bst;
    return minOfBST(bst.left);
}

function maxOfBST(bst:BSTNode): BSTNode
{
    // get the right most node
    if(!bst.right)
        return bst;
    return maxOfBST(bst.right);
}

function deleteFromBST(bst:BSTNode, data:number): BSTNode|undefined|null
{
    if(!bst)
        return null;

    if(bst.value == data){
        // if node to be deleted is a leaf node
        if(!(bst.right && bst.left)){
            bst.value = null;
            return bst   
        }
        else if(!bst.right && bst.left){
            // if node to be deleted has only left child
            // then replace it with the maximum value of left subtree
            let temp = maxOfBST(bst.left).value;
            bst.value = temp;
            deleteFromBST(bst.left, temp!);
        }else{
            // if node to be deleted has only right child
            // then replace it with the minimum value of right subtree
            let temp = minOfBST(bst.right).value;
            bst.value = temp;
            deleteFromBST(bst.right, temp!);
        }
        return bst;
    }
    else if(data > bst.value!) // if data is greater than bst value then search on right subtree
        bst.right = deleteFromBST(bst.right, data)!;
    else if(data < bst.value!) // if data is less than bst value then search on left subtree
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
traverseInOrder(root); // 1 3 4 6 7 8 10 14
console.log(searchOnBST(root, 14)); // true
console.log(minOfBST(root).value); // 1
console.log(maxOfBST(root).value); // 14
root = deleteFromBST(root, 3)!; // 3 is removed and replaced with left subtree's max value i.e. 4
traverseInOrder(root); // 1 4 6 7 8 10 14

console.log("========================================\n\n");
