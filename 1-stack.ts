/*
Stack
A stack is a linear data structure that follows the principle of Last In First Out(LIFO).

Applications
To reverse a word, In compilers(arithmetics operations), In browsers(back button)
*/
class Stack{
    private stack:number[] = [];

    public push(a: number): void
    {
        // add item to end of stack
        this.stack[this.stack.length === 0 ? 0 : this.stack.length] = a;
    }

    public pop(): number
    {
        // delete last element of stack
        const temp = this.stack[this.stack.length - 1];
        this.stack.splice(this.stack.length - 1, 1);
        return temp;
    }

    public isEmpty(): boolean
    {
        return this.stack.length === 0;
    }

    public peek(): number
    {
        // return last element of stack
        return this.stack[this.stack.length - 1 != -1 ? this.stack.length - 1 : 0];
    }
}

let stack = new Stack();
stack.push(1); // [1]
stack.push(2); // [1, 2]
stack.push(3); // [1, 2, 3]
stack.pop(); // 3
console.log(stack); // [1, 2]
console.log(stack.peek()); // 2