/*
Linked List
A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node.

Applications
In undo fuctionality of softwares, Hash tables, Graphs, Dynamic memory allocation
*/

class CNode{
    // For circular create a head property then connect to last node to first node
    private next:CNode|null;
    private value:number;

    public constructor(value:number){ 
        this.next = null;
        this.value = value;
    }

    public setNext(next_node:CNode){
        this.next = next_node
    }

    public getValue():number
    {
        return this.value;
    }

    public getNext():CNode|null
    {
        return this.next
    }
}
let node = new CNode(5);
let node2 = new CNode(10);
let node3 = new CNode(15);
let node4 = new CNode(20);
let node5 = new CNode(25);
node.setNext(node2); // node.value = 5 node.next = 10
node2.setNext(node3); // node2.value = 10 node2.next = 15
node3.setNext(node4); // node3.value = 15 node3.next = 20
node4.setNext(node5); // node4.value = 20 node4.next = 25

// Traverse a Linked List
let travel:CNode|null = node; 
while(travel != null){
    console.log(travel.getValue()); // 5 10 15 20 25
    travel = travel.getNext();
}