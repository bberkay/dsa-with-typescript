/*
Circular Queue
A circular queue is the extended version of regular queue where the last element is connected to the first element. Thus forming a circle-like structure.

Applications
CPU Scheduling, Traffic Management
*/

class CircularQueue{
    public queue:number[] = [];
    public max_size:number = 0;

    public front:number = -1;
    public rear:number = -1;

    public constructor(size:number){
        this.max_size = size;
        for(let i = 1; i <= this.max_size; i++)
            this.queue.push(null);
    }

    public enqueue(a:number): void
    {
        let isEmpty = true;
        if(this.rear + 1 <= this.max_size - 1 && this.queue[this.rear + 1] == null){
            this.queue[this.rear + 1] = a;
            this.rear += 1;
            console.log("added in true: " + a.toString());
        }else{
            for(let i = 0; i<this.max_size-1;i++){
                if(this.queue[i] != null)
                    isEmpty = false;
                if(this.queue[i] == null){
                    this.rear = i;
                    this.queue[i] = a;
                    console.log("added in false: " + a.toString());
                    break;
                }
            }
        }

        if(isEmpty == true)
            this.front = 0;
        else
            console.log("list is full");
    }

    public dequeue():number
    {
        const temp = this.front;
        for(let i = 0; i<=this.max_size-1;i++){
            if(this.queue[i] != null){
                this.queue[this.queue.indexOf(this.queue[i])] = null;
                this.front += 1;
                break;
            }
        }
        return temp;
    }

    public display(): void
    {
        console.log(this.queue.filter(item => item !== null));
    }

}

let circular_queue = new CircularQueue(5);
circular_queue.enqueue(1);
circular_queue.enqueue(2);
circular_queue.enqueue(3);
circular_queue.enqueue(4);
circular_queue.enqueue(5);
circular_queue.display();

circular_queue.dequeue();
circular_queue.dequeue();
circular_queue.display();

circular_queue.enqueue(12);
circular_queue.enqueue(13);
circular_queue.display();

circular_queue.dequeue();
circular_queue.display();