function calculateTime(input) {
    let seriesName = input[0];
    let episodeDuration = Number(input[1]);
    let breakDuration = Number(input[2]);

    let lunchDuration = (1 / 8) * breakDuration;
    let leisureDuration = (1 / 4) * breakDuration;
    let freeTime = breakDuration - leisureDuration - lunchDuration;
    let diff = Math.abs(freeTime - episodeDuration);

    if (freeTime >= episodeDuration) {
        console.log(`You have enough time to watch ${seriesName} and left with ${Math.ceil(diff)} minutes free time.`)
    } else {
        console.log(`You don't have enough time to watch ${seriesName}, you need ${Math.ceil(diff)} more minutes.`)
    }
}

calculateTime(["Teen Wolf", "48", "60"])


