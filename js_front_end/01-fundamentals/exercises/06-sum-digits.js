function solve(num) {
    const strFromNum = num.toString();
    let sum = 0;

    for (let i = 0; i < strFromNum.length; i++) {
        sum += Number(strFromNum[i]);
    }

    console.log(sum);
}

solve(245678);
solve(97561);
solve(543);
