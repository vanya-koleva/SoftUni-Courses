function palindromeIntegers(numbers) {
    numbers.forEach(printResult);

    function isPalindrome(num) {
        const forwardNum = num.toString();
        const backwardNum = forwardNum.split('').reverse().join('');

        return forwardNum === backwardNum;
    }

    function printResult(num) {
        console.log(isPalindrome(num));
    }
}

palindromeIntegers([123, 323, 421, 121]);
