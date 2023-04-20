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

let d_node = new CDNode(5);
let d_node2 = new CDNode(10);
let d_node3 = new CDNode(15);
d_node.setNext(d_node2); // node.value = 5 node.next = 10
d_node2.setNext(d_node3); // node2.value = 10 node2.next = 15
d_node2.setPrev(d_node); // node2.prev = 5

console.log(d_node.getNext().getPrev().getValue()); // 5


