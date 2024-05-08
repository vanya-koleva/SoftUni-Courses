function calculateTime(input) {
    let hours = Number(input[0]);
    let minutes = Number(input[1]);

    let totalTime = hours * 60 + minutes + 15;
    let h = Math.floor(totalTime / 60);
    let min = totalTime % 60;

    if (h > 23) {
        h = 0
    }

    if (min < 10) {
        console.log(`${h}:0${min}`);
    } else {
        console.log(`${h}:${min}`)
    }
}

calculateTime(["11", "08"])
