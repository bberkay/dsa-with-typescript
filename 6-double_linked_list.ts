/*
Doubly Linked List
We add a pointer to the previous node in a doubly-linked list. Thus, we can go in either direction: forward or backward.
*/

class CDNode{
    private next:CDNode;
    private prev:CDNode;
    private value:number;

    public constructor(value:number){
        this.value = value
    }

    public setNext(next_node:CDNode){
        this.next = next_node;
    }

    public getNext(): CDNode
    {
        return this.next;
    }

    public setPrev(prev_node:CDNode){
        this.prev = prev_node;
    }

    public getPrev(): CDNode
    {
        return this.prev;
    }

    public getValue(): number
    {
        return this.value;
    }

}

let node = new CDNode(5);
let node2 = new CDNode(10);
let node3 = new CDNode(15);
node.setNext(node2);
node2.setNext(node3);
node2.setPrev(node);

console.log(node.getNext().getPrev().getValue());


