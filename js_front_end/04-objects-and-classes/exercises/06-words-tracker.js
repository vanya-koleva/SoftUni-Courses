function solve(input) {
    const words = input
        .shift()
        .split(' ')
        .reduce((result, word) => ({ ...result, [word]: 0 }), {});

    for (const word of input) {
        if (words.hasOwnProperty(word)) {
            words[word]++;
        }
    }

    Object.entries(words)
        .sort((a, b) => b[1] - a[1])
        .forEach(([word, count]) => console.log(`${word} - ${count}`));
}

solve([
    'this sentence',
    'In',
    'this',
    'sentence',
    'you',
    'have',
    'to',
    'count',
    'the',
    'occurrences',
    'of',
    'the',
    'words',
    'this',
    'and',
    'sentence',
    'because',
    'this',
    'is',
    'your',
    'task',
]);
