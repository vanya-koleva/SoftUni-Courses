function calculateTime(input) {
    let worldRecord = Number(input[0]);
    let distance = Number(input[1]);
    let timePerMeter = Number(input[2]);

    let timesResistance = Math.floor(distance / 15)
    let totalTime = (distance * timePerMeter) + (timesResistance * 12.5)

    if (totalTime < worldRecord) {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    } else {
        let diff = totalTime - worldRecord
        console.log(`No, he failed! He was ${diff.toFixed(2)} seconds slower.`)
    }
}

calculateTime(["55555.67", "3017", "5.03"])
