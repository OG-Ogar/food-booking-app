// =========================================
// FOODBOOK - MAIN JAVASCRIPT
// =========================================


document.addEventListener("DOMContentLoaded", () => {

    setupMobileMenu();

    setupQuantity();

});


/*
 * Mobile navigation
 */

function setupMobileMenu() {

    const menuToggle =
        document.getElementById("menuToggle");

    const navLinks =
        document.querySelector(".nav-links");


    if (!menuToggle || !navLinks) {
        return;
    }


    menuToggle.addEventListener("click", () => {

        navLinks.classList.toggle("mobile-open");

    });

}


/*
 * Food quantity
 */

function setupQuantity() {

    const quantityElement =
        document.getElementById("quantity");

    const totalPriceElement =
        document.getElementById("totalPrice");

    const increaseButton =
        document.getElementById("increaseQuantity");

    const decreaseButton =
        document.getElementById("decreaseQuantity");


    if (
        !quantityElement ||
        !totalPriceElement ||
        !increaseButton ||
        !decreaseButton
    ) {

        return;

    }


    const price = 2500;

    let quantity = 1;


    function updateTotal() {

        quantityElement.textContent = quantity;

        const total = price * quantity;

        totalPriceElement.textContent =
            `₦${total.toLocaleString()}`;

    }


    increaseButton.addEventListener("click", () => {

        quantity++;

        updateTotal();

    });


    decreaseButton.addEventListener("click", () => {

        if (quantity <= 1) {
            return;
        }

        quantity--;

        updateTotal();

    });


    updateTotal();

}