/*
This is a JS implementation of the Chudonovksy Pi computation formula.
Don't run it in your browser. Run it with NodeJS in your shell. 
Ka^Io 
*/

factorial = function(n){
    if(n === 0) { return 1; }
    else {
        return n * factorial( n - 1 ); 
    }
}

Chudonovksy = function() { 
    pi = 0; 

    for(let i = 0; i < 16; i++){
        top = Math.pow(-1, i % 2) * factorial(6*i) * (13591409 + 545140134*i);
        bot = factorial(3*i) * Math.pow(factorial(i), 3) * Math.pow(640320, 3*i+3/2);
        pi += top / bot;
    }

    pi = 12 * pi; 
    pi = 1 / pi;
    console.log(pi);
}

Chudonovksy();
