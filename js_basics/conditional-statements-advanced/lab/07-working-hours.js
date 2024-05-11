function workingHours(input) {
    let hour = Number(input[0]);
    let day = input[1];

    if (day != "Sunday" && (10 <= hour && hour <= 18)) {
        console.log("open");
    } else {
        console.log("closed")
    }
}

workingHours(["11", "Sunday"])
