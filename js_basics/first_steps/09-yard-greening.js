function yardGreening(input) {
    let meters = Number(input[0]);
    let totalPrice = meters * 7.61
    let discount = totalPrice * 0.18
    let finalPrice = totalPrice - discount

    console.log(`The final price is: ${finalPrice} lv.`)
    console.log(`The discount is: ${discount} lv.`)
}

yardGreening(["550"])
