function calculatePrice(input) {
    let fruit = input[0];
    let day = input[1];
    let quantity = Number(input[2]);
    let price = 0;
    
    if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
        if (fruit == "banana") {
            price = 2.5;
        } else if (fruit == "apple") {
            price = 1.2;
        } else if (fruit == "orange") {
            price = 0.85;
        } else if (fruit == "grapefruit") {
            price = 1.45;
        } else if (fruit == "kiwi") {
            price = 2.7;
        } else if (fruit == "pineapple") {
            price = 5.5;
        } else if (fruit == "grapes") {
            price = 3.85;
        }
    } else if (day == "Saturday" || day == "Sunday") {
        if (fruit == "banana") {
            price = 2.7;
        } else if (fruit == "apple") {
            price = 1.25;
        } else if (fruit == "orange") {
            price = 0.9;
        } else if (fruit == "grapefruit") {
            price = 1.6;
        } else if (fruit == "kiwi") {
            price = 3;
        } else if (fruit == "pineapple") {
            price = 5.6;
        } else if (fruit == "grapes") {
            price = 4.20;
        }
    } 
    if (price == 0) {
        console.log("error")
    } else {
    let totalPrice = price * quantity
    console.log(totalPrice.toFixed(2))
    }
}

calculatePrice(["tomato", "Tuesday", "2"])
