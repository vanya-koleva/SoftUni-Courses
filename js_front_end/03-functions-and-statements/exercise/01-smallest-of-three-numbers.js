function smallestNumber(num1, num2, num3) {
    function findSmallest(numbers) {
        let minNumber = Number.MAX_SAFE_INTEGER;

        for (const num of numbers) {
            if (minNumber > num) {
                minNumber = num;
            }
        }

        return minNumber;
    }

    console.log(findSmallest([num1, num2, num3]));
}

smallestNumber(2, 5, 3);

function defaultMathMin(...numbers) {
    console.log(Math.min(...numbers));
}

defaultMathMin(2, 5, 3);

function smallestOfTwo(num1, num2, num3) {
    const smallestNum = (a, b) => (a > b ? b : a);

    console.log(smallestNum(num1, smallestNum(num2, num3)));
}

smallestOfTwo(2, 5, 3);
