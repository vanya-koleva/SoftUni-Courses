function calculateCommission(input) {
    let city = input[0];
    let sales = Number(input[1]);
    let percent = 0

    if (0 <= sales && sales <= 500) {
        switch (city) {
            case "Sofia":
                percent = 5;
                break;
            case "Varna":
                percent = 4.5;
                break;
            case "Plovdiv":
                percent = 5.5;
                break;
            default:
                percent = 0;
                break;
        }
    } else if (500 < sales && sales <= 1000) {
        switch (city) {
            case "Sofia":
                percent = 7;
                break;
            case "Varna":
                percent = 7.5;
                break;
            case "Plovdiv":
                percent = 8;
                break;
            default:
                percent = 0;
                break;
        } 
    } else if (1000 < sales && sales <= 10000) {
            switch (city) {
                case "Sofia":
                    percent = 8;
                    break;
                case "Varna":
                    percent = 10;
                    break;
                case "Plovdiv":
                    percent = 12;
                    break;
                default:
                    percent = 0;
                    break;
        }
    } else if (sales > 10000) {
        switch (city) {
            case "Sofia":
                percent = 12;
                break;
            case "Varna":
                percent = 13;
                break;
            case "Plovdiv":
                percent = 14.5;
                break;
            default:
                percent = 0;
                break;
        }
    }
    if (percent == 0) {
        console.log("error")
    } else {
        let commission = sales * percent / 100
        console.log(commission.toFixed(2))
    }
}

calculateCommission(["Kaspichan", "-50"])
