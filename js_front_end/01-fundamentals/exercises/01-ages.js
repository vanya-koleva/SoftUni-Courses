function solve(age) {
    if (age < 0) console.log('out of bounds');
    if (0 <= age && age <= 2) console.log('baby');
    if (3 <= age && age <= 13) console.log('child');
    if (14 <= age && age <= 19) console.log('teenager');
    if (20 <= age && age <= 65) console.log('adult');
    if (66 <= age) console.log('elder');
}

solve(-1);
