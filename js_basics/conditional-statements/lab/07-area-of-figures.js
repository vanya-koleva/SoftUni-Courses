function calculateArea(input) {
    let figure = input[0];
    if (figure == "square") {
        let side = Number(input[1]);
        let area = side * side;
        console.log((area).toFixed(3));
    } else if (figure == "rectangle") {
        let length = Number(input[1]);
        let width = Number(input[2]);
        let area = length * width;
        console.log((area).toFixed(3));
    } else if (figure == "circle") {
        let radius = Number(input[1]);
        let area = radius * radius * Math.PI;
        console.log((area).toFixed(3));
    } else if (figure == "triangle") {
        let base = Number(input[1]);
        let height = Number(input[2]);
        let area = (base * height) / 2;
        console.log((area).toFixed(3));
    }
}

calculateArea(["circle", "6"])
