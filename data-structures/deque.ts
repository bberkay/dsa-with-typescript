/*
Deque
Deque or Double Ended Queue is a type of queue in which insertion and removal of elements can either be performed from the front or the rear. Thus, it does not
follow FIFO rule(First In First Out).

Applications
In undo operations on software, To store history in browsers, For implementing both stacks and queues.
*/
class Deque{
    private deque:number[] = [];

    public addRear(a:number): void
    {
        // add element to rear
        this.deque.push(a);
    }

    public addFront(a:number): void
    {
        // add element to front
        let cache_even = this.deque[0];
        let cache_odd = this.deque[0];
        this.deque[0] = a;
        let l = this.deque.length + 1;
        for(let i = 1;i<l;i++){
            if(i % 2 == 0){
                cache_even = this.deque[i];
                if(i + 1 >= l)
                    this.deque.push(cache_odd);
                else
                    this.deque[i] = cache_odd;
            }else{
                cache_odd = this.deque[i];
                if(i + 1 >= l)
                    this.deque.push(cache_even);
                else
                    this.deque[i] = cache_even;
            }
        }

    }

    public removeFront(): number
    {
        // delete front element
        const temp = this.deque[0];
        this.deque.splice(0, 1);
        return temp;
    }

    public removeRear(): number
    {
        // delete rear element
        const temp = this.deque[this.deque.length - 1];
        this.deque.splice(this.deque.indexOf(this.deque.length - 1), 1);
        return temp;
    }

}

let deque = new Deque()
deque.addRear(8); // [8]
deque.addRear(5); // [8, 5]
deque.addFront(7); // [7, 8, 5]
deque.addFront(10); // [10, 7, 8, 5]
deque.addRear(11); // [10, 7, 8, 5, 11]

console.log(deque); // [10, 7, 8, 5, 11]

deque.removeRear(); // 11
deque.removeFront(); // 10
deque.addFront(55); // [55, 7, 8, 5]
deque.addRear(45); // [55, 7, 8, 5, 45]

console.log(deque); // [55, 7, 8, 5, 45]