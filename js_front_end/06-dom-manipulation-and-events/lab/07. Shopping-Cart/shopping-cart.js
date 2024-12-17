document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const addProductButtonElements = document.querySelectorAll('.add-product');
    const checkoutButtonEl = document.querySelector('.checkout');
    const textareaEl = document.querySelector('textarea');

    let products = [];
    let totalPrice = 0;

    [...addProductButtonElements].forEach(btn => {
        btn.addEventListener('click', addProductInCart);
    });

    checkoutButtonEl.addEventListener('click', checkout);

    function addProductInCart(e) {
        const productEl = e.target.parentNode.parentNode;
        const productTitle = productEl.querySelector('.product-title');
        const productPrice = productEl.querySelector('.product-line-price');

        printMessage(productTitle, productPrice);

        if (!products.includes(productTitle.textContent)) {
            products.push(productTitle.textContent);
        }

        totalPrice += Number(productPrice.textContent);
    }

    function printMessage(title, price) {
        textareaEl.textContent += `Added ${title.textContent} for ${Number(price.textContent).toFixed(2)} to the cart.\n`;
    }

    function checkout(e) {
        textareaEl.textContent += `You bought ${products.join(', ')} for ${totalPrice.toFixed(2)}.`;

        document.querySelectorAll('button').forEach(el => el.setAttribute('disabled', 'disabled'));
    }
}
