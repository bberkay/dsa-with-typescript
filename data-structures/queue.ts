/*
Queue
A queue is a useful data structure in programming. Queue follows the First in First Out(FIFO) rule.

Applications
Call Center(call order), Scheduling(CPU, Disk, Operation)
*/
class Queue{
    private queue:number[] = [];

    public enqueue(a:number): void
    {
        this.queue[this.queue.length] = a;
    }

    public dequeue(): number
    {
        // delete first element in stack
        const temp = this.queue[0];
        this.queue.splice(0, 1);
        return temp;
    }

    public display(): void
    {
        console.log(this.queue);
    }
}

let queue = new Queue();
queue.enqueue(1) // [1]
queue.enqueue(2) // [1, 2]
queue.enqueue(3) // [1, 2, 3]
queue.enqueue(4) // [1, 2, 3, 4]
queue.enqueue(5) // [1, 2, 3, 4, 5]

queue.display() // [1, 2, 3, 4, 5]

queue.dequeue() // [2, 3, 4, 5]
queue.dequeue() // [3, 4, 5]
queue.display() // [4, 5]