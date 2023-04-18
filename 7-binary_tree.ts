/*
Binary Tree
A binary tree is a tree data structure in which each parent node can have at most two children. Each node of a binary tree consists of three items:
- data item
- address of left child
- address of right child

Applications
For easy and quick access to data, in router algorithims
*/

class TNode {
    public value: number;
    public left: TNode;
    public right: TNode;

    public constructor(data:number) {
        this.value = data
    }
}

function inorder(node:TNode) {
    if(node){
        inorder(node.left);
        console.log(node.value);
        inorder(node.right);
    }
}

function preorder(node:TNode) {
    if(node){
        console.log(node.value);
        preorder(node.left);
        preorder(node.right);
    }
}

function postorder(node:TNode) {
    if(node){
        postorder(node.left);
        postorder(node.right);
        console.log(node.value);
    }
}

let node = new TNode(5);
let node2 = new TNode(10);
let node3 = new TNode(15);
let node4 = new TNode(20);
let node5 = new TNode(25);
node.right = node3;
node.left = node2;
node.left.left = node4;
node.left.right = node5;
console.log("in order");
inorder(node);
console.log("pre order");
preorder(node);
console.log("post order");
postorder(node);


