function solve(input) {
    const occurences = input
        .toLowerCase()
        .split(' ')
        .reduce((acc, word) =>
            acc.hasOwnProperty(word)
                ? { ...acc, [word]: acc[word] + 1 }
                : { ...acc, [word]: 1 },
            {});

    const result = Object
        .entries(occurences)
        .filter(([word, count]) => count % 2 != 0)
        .map(([word, count]) => word)
        .join(' ');

    console.log(result);
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
