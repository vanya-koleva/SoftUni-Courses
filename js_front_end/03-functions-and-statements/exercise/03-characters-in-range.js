function charsInRange(first, second) {
    const [start, end] = [...arguments].sort();
    const result = getCharsBetween(start, end);

    console.log(result.join(' '));
    // console.log(...result);

    function getCharsBetween(start, end) {
        let characters = [];

        for (let i = start.charCodeAt(0) + 1; i < end.charCodeAt(0); i++) {
            characters.push(String.fromCharCode(i));
        }

        return characters;
    }
}

charsInRange('a', 'd');
