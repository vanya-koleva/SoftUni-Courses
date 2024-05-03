function projectCreation(input) {
    let name = input[0];
    let projectNumber = Number(input[1]);
    let hours = 3 * projectNumber

    console.log(`The architect ${name} will need ${hours} hours to complete ${projectNumber} project/s.`)
}

projectCreation(["George", "4"])
