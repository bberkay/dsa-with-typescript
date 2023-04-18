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
        this.queue[this.queue.length === 0 ? 0 : this.queue.length] = a;
    }

    public dequeue(): number
    {
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
queue.enqueue(2) // [2, 1]
queue.enqueue(3) // [3, 2, 1]
queue.enqueue(4) // [4, 3, 2, 1]
queue.enqueue(5) // [5, 4, 3, 2, 1]

queue.display()

queue.dequeue()
queue.dequeue()
queue.display()