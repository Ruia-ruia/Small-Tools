/*
Weird kind of permutation test using bijection as the condition.
*/

var perm = function(a, b) {
    if (a.length != b.length) { return false; }

    counts = []; 
    for (i of a) {
        count = 0;
        for (j of b) {
            if (i == j) {
                count += 1;
            }
        }
        counts.push(count);
    }

    for (x of counts) {
        if (x === 0) {
        return false
        }
    }
    return true; 
}

perm('hello', 'ehllo');
perm('helll', 'ehllo');
