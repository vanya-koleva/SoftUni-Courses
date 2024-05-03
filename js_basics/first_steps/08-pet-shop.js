function petShop(input) {
    let dogFood = Number(input[0]) * 2.5
    let catFood = Number(input[1]) * 4
    let totalPrice = catFood + dogFood

    console.log(`${totalPrice} lv.`)
}

petShop(["5" ,"4"])
