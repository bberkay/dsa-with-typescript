/*
Circular Queue
A circular queue is the extended version of regular queue where the last element is connected to the first element. Thus forming a circle-like structure.

Applications
CPU Scheduling, Traffic Management
*/

class CircularQueue{
    public queue:any[] = [];
    public max_size:number = 0;

    public front:number = 0;
    public rear:number = -1;

    public constructor(size:number){
        // init queue with limit
        this.max_size = size;
        for(let i = 1; i <= this.max_size; i++)
            this.queue.push(null);
    }

    public enqueue(a:number): void
    {   
        // replace it with the leading null element.
        let isEmpty = true;
        if(this.rear + 1 <= this.max_size - 1 && this.queue[this.rear + 1] == null){
            this.queue[this.rear + 1] = a;
            this.rear += 1;
        }else{
            for(let i = 0; i<this.max_size-1;i++){
                if(this.queue[i] != null)
                    isEmpty = false;
                if(this.queue[i] == null){
                    this.rear = i;
                    this.queue[i] = a;
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
        // delete leading null element from queue
        const temp = this.queue[this.front];
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
circular_queue.enqueue(1); // [1]
circular_queue.enqueue(2); // [1, 2]
circular_queue.enqueue(3); // [1, 2, 3]
circular_queue.enqueue(4); // [1, 2, 3, 4]
circular_queue.enqueue(5); // [1, 2, 3, 4, 5]
circular_queue.display(); // [1, 2, 3, 4, 5]

circular_queue.dequeue(); // 1
circular_queue.dequeue(); // 2
circular_queue.display(); // [3, 4, 5]

circular_queue.enqueue(12); // [12, 3, 4, 5]
circular_queue.enqueue(13); // [12, 13, 3, 4, 5]
circular_queue.display(); // [12, 13, 3, 4, 5]

circular_queue.dequeue(); // 12
circular_queue.display(); // [13, 3, 4, 5]