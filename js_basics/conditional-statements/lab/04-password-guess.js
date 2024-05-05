function passwordGuess(input) {
    let passowrd = "s3cr3t!P@ssw0rd";
    if (input[0] == passowrd) {
        console.log("Welcome")
    }
    else {
        console.log("Wrong password!")
    }
}

passwordGuess(["s3cr3t!P@ssw0rd"])
