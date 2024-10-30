
var MinStack = function() {
    this.stack = []
    this.minstack = []
};


MinStack.prototype.push = function(val) {
    this.stack.push(val)
    if (this.minstack[this.minstack.length - 1] > val || this.minstack.length == 0) {
        this.minstack.push(val)
    } else {
        this.minstack.push(this.minstack[this.minstack.length - 1])
    }
};

MinStack.prototype.pop = function() {
    this.stack.pop(this.stack[this.stack.length - 1])
    this.minstack.pop(this.minstack[this.minstack.length - 1])
};

MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1]    
};

MinStack.prototype.getMin = function() {
    return this.minstack[this.minstack.length - 1]
};

var Mystack = new MinStack()
Mystack.push(-2)
console.log(Mystack.stack) //prints the new value of the stack after -2 is pushed to it
Mystack.push(0)
console.log(Mystack.stack) //prints the new value of the stack after 0 is pushed to it
Mystack.push(-3)
console.log(Mystack.stack) //prints the new value of the stack after -3 is pushed to it
console.log(Mystack.getMin()) //prints the minimum value from the stack that is -3
Mystack.pop()
console.log(Mystack.stack) //prints the new value of the stack after the last elemnent is poped
console.log(Mystack.top()) //prints the last value of the stack that is 0
console.log(Mystack.getMin()) //prints the minimum value from the stack that is -2



// var evalRPN = function(tokens) {
//     var NumberStack = []
//     var result
//     function calculate (a, b , operator){
//         switch(operator){
//             case "+":
//                 return Math.trunc(a + b)
//             case "-":
//                 return Math.trunc(a - b)
//             case "*":
//                 return Math.trunc(a * b)
//             case "/":
//                 return Math.trunc(a/b)
//         }
//     }
//     for(var x of tokens){
//         y =  Number(x)
//         if (!isNaN(y)) NumberStack.push(y)
//         else {
//             result = calculate(NumberStack[NumberStack.length - 2],NumberStack[NumberStack.length - 1],x)
//             // console.log(NumberStack[NumberStack.length - 2],x, NumberStack[NumberStack.length - 1])
//             // console.log(result)
//             NumberStack.pop(NumberStack[NumberStack.length - 1])
//             NumberStack.pop(NumberStack[NumberStack.length - 1])
//             NumberStack.push(result)
//         }
//     }
//     return(NumberStack[0])
// };




// var generateParenthesis = function(n) {
    
//     return n
// };
// console.log(generateParenthesis(3))