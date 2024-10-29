var evalRPN = function(tokens) {
    var NumberStack = []
    var result
    function calculate (a, b , operator){
        switch(operator){
            case "+":
                return Math.trunc(a + b)
            case "-":
                return Math.trunc(a - b)
            case "*":
                return Math.trunc(a * b)
            case "/":
                return Math.trunc(a/b)
        }
    }
    for(var x of tokens){
        y =  Number(x)
        if (!isNaN(y)) NumberStack.push(y)
        else {
            result = calculate(NumberStack[NumberStack.length - 2],NumberStack[NumberStack.length - 1],x)
            // console.log(NumberStack[NumberStack.length - 2],x, NumberStack[NumberStack.length - 1])
            // console.log(result)
            NumberStack.pop(NumberStack[NumberStack.length - 1])
            NumberStack.pop(NumberStack[NumberStack.length - 1])
            NumberStack.push(result)
        }
    }
    return(NumberStack[0])
};
console.log(evalRPN(["18"]))