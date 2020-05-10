var lettercount = function(letter, string) {
    var count = 0;
    for (i of string) {
        if (i === letter) {
            count += 1;
        }
    }
    return count; 
}

var perm = function(a, b){
    if (a.length != b.length) { return false; }
    var alphabet = 'abcdefghijklmnopqrstuvwxyz';

    for (alpha of alphabet) {
        if (lettercount(alpha, a) != lettercount(alpha, b)) {
            return false   
        }
    }
    return true;
}
