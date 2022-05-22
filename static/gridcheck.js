function gridcheck(celltag) {

    const squares = [];
    const verified = [];

    for (let i=-1; i<2; i++) {
        var dig1 = parseInt(celltag[0])
        var dig2 = parseInt(celltag[1])
        var new1 = dig1 + i;
        for (let j=-1; j<2; j++) {
            var new2 = dig2 + j;
            squares.push((new1.toString() + new2.toString()))
        }
    }

    for (let i=0; i<squares.length; i++) {

        if (squares[i].length > 2) {
            continue
        }
        if (squares[i].includes('5')) {
            continue
        } else {
            verified.push(squares[i])
        }
    }
    return verified;
}
