function solve(text) {
    const pattern = /#[A-Za-z]+/g;
    const captures = text.match(pattern);
    captures.forEach(function (element) {
        console.log(element.substring(1));
    });
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia');
solve('The symbol # is known #variously in English-speaking #regions as the #number sign');
