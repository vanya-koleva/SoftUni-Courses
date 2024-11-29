function solve(words, text) {
    words = words.split(', ');

    for (let w of words) {
        text = text.replace('*'.repeat(w.length), w);
    }

    console.log(text);
}

solve('great', 'softuni is ***** place for learning new programming languages');
// softuni is great place for learning new programming languages
solve('great, learning', 'softuni is ***** place for ******** new programming languages');
// softuni is great place for learning new programming languages
