function solve(password) {
    const isValidLength = password => password.length >= 6 && password.length <= 10;
    const isAlphaNumeric = password => /^[A-Za-z0-9]+$/.test(password);
    const hasTwoDigits = password =>
        password.split('').filter(character => Number.isInteger(Number(character))).length >= 2;

    const validations = [
        [isValidLength, 'Password must be between 6 and 10 characters'],
        [isAlphaNumeric, 'Password must consist only of letters and digits'],
        [hasTwoDigits, 'Password must have at least 2 digits'],
    ];

    const errors = validations
        .map(([validator, message]) => (validator(password) ? '' : message))
        .filter(message => message);

    errors.forEach(message => console.log(message));

    if (errors.length === 0) {
        console.log('Password is valid');
    }
}

solve('logIn');
solve('MyPass123');
solve('Pa$s$s');
