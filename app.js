/*
Stack
A stack is a linear data structure that follows the principle of Last In First Out(LIFO).

Applications
To reverse a word, In compilers(arithmetics operations), In browsers(back button)
*/
var Stack = /** @class */ (function () {
    function Stack() {
        this.stack = [];
    }
    Stack.prototype.push = function (a) {
        this.stack[this.stack.length === 0 ? 0 : this.stack.length] = a;
    };
    Stack.prototype.pop = function () {
        var temp = this.stack[this.stack.length - 1];
        this.stack.splice(this.stack.length - 1, 1);
        return temp;
    };
    Stack.prototype.isEmpty = function () {
        return this.stack.length === 0;
    };
    Stack.prototype.peek = function () {
        return this.stack[this.stack.length - 1 != -1 ? this.stack.length - 1 : 0];
    };
    return Stack;
}());
var stack = new Stack();
stack.push(1); // stack is -> [1]
stack.push(2); // stack is -> [1, 2]
stack.push(3); // stack is -> [1, 2, 3]
stack.pop(); // pop result is -> [3]
console.log(stack); // stack is -> [1, 2]
console.log(stack.peek()); // top of stack is -> 2
