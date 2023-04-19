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

let t_node = new TNode(5);
let t_node2 = new TNode(10);
let t_node3 = new TNode(15);
let t_node4 = new TNode(20);
let t_node5 = new TNode(25);

t_node.right = t_node3; // t_node.value = 5 t_node.right = 15
t_node.left = t_node2; // t_node.value = 5 t_node.left = 10
t_node.left.left = t_node4; // t_node.value = 5 t_node.left = 10 t_node.left.left = 20
t_node.left.right = t_node5; // t_node.value = 5 t_node.left = 10 t_node.left.right = 25

console.log("in order");
inorder(t_node); // 20 10 25 5 15
console.log("pre order");
preorder(t_node); // 5 10 20 25 15
console.log("post order");
postorder(t_node); // 20 25 10 15 5


