function lettercheck(cellid, answer, gridlist) {

    const present = [];
    const absent = [];

    for (let i=0; i<gridlist.length; i++) {

        const letter = document.getElementById(gridlist[i]).innerHTML
        if (answer.includes(letter)) {
            present.push(gridlist[i]);
        } else {
            absent.push(gridlist[i])
        }
    }

    for (let i=0; i<present.length; i++) {
        var cell = document.getElementById(present[i])
        cell.className = 'confirmed';
    }

    for (let i=0; i<absent.length; i++) {
        var cell = document.getElementById(absent[i])
        cell.className = 'absent'
    }

}