// =========================================
// FOODBOOK - BOOKING JAVASCRIPT
// =========================================


document.addEventListener("DOMContentLoaded", () => {

    setupBookingQuantity();

    setupBookingForm();

    setupDeliveryMethod();

});


/*
 * Booking quantity
 */

function setupBookingQuantity() {

    const quantityElement =
        document.getElementById("bookingQuantity");

    const increaseButton =
        document.getElementById(
            "increaseBookingQuantity"
        );

    const decreaseButton =
        document.getElementById(
            "decreaseBookingQuantity"
        );

    const subtotalElement =
        document.getElementById("subtotal");

    const totalElement =
        document.getElementById("bookingTotal");


    if (
        !quantityElement ||
        !increaseButton ||
        !decreaseButton
    ) {
        return;
    }


    const foodPrice = 2500;

    const deliveryFee = 500;

    let quantity = 1;


    function updatePrice() {

        const subtotal = foodPrice * quantity;

        const total = subtotal + deliveryFee;


        quantityElement.textContent = quantity;

        subtotalElement.textContent =
            `₦${subtotal.toLocaleString()}`;

        totalElement.textContent =
            `₦${total.toLocaleString()}`;

    }


    increaseButton.addEventListener("click", () => {

        quantity++;

        updatePrice();

    });


    decreaseButton.addEventListener("click", () => {

        if (quantity <= 1) {
            return;
        }

        quantity--;

        updatePrice();

    });


    updatePrice();

}


/*
 * Delivery method
 */

function setupDeliveryMethod() {

    const options =
        document.querySelectorAll(
            'input[name="deliveryMethod"]'
        );

    const deliveryFeeElement =
        document.getElementById("deliveryFee");


    options.forEach((option) => {

        option.addEventListener("change", () => {

            if (option.value === "pickup") {

                deliveryFeeElement.textContent = "₦0";

            } else {

                deliveryFeeElement.textContent = "₦500";

            }

            /*
             * Recalculate total.
             */

            recalculateBookingTotal();

        });

    });

}


/*
 * Recalculate booking total
 */

function recalculateBookingTotal() {

    const quantityElement =
        document.getElementById("bookingQuantity");

    const subtotalElement =
        document.getElementById("subtotal");

    const deliveryFeeElement =
        document.getElementById("deliveryFee");

    const totalElement =
        document.getElementById("bookingTotal");


    if (!quantityElement) {
        return;
    }


    const quantity =
        Number(quantityElement.textContent);

    const foodPrice = 2500;

    const deliveryFee =
        deliveryFeeElement.textContent === "₦0"
            ? 0
            : 500;


    const subtotal =
        foodPrice * quantity;

    const total =
        subtotal + deliveryFee;


    subtotalElement.textContent =
        `₦${subtotal.toLocaleString()}`;

    totalElement.textContent =
        `₦${total.toLocaleString()}`;

}


/*
 * Booking form
 */

function setupBookingForm() {

    const form =
        document.getElementById("bookingForm");

    const button =
        document.getElementById(
            "confirmOrderButton"
        );


    if (!form) {
        return;
    }


    form.addEventListener("submit", async (event) => {

        event.preventDefault();


        const name =
            document.getElementById(
                "customerName"
            ).value.trim();

        const phone =
            document.getElementById(
                "customerPhone"
            ).value.trim();

        const address =
            document.getElementById(
                "deliveryAddress"
            ).value.trim();

        const notes =
            document.getElementById(
                "orderNotes"
            ).value.trim();


        const deliveryMethod =
            document.querySelector(
                'input[name="deliveryMethod"]:checked'
            ).value;


        if (!name || !phone || !address) {

            showBookingMessage(
                "Please complete your customer and delivery information.",
                "error"
            );

            return;
        }


        button.disabled = true;

        button.textContent =
            "Processing Order...";


        /*
         * Backend integration will go here.
         *
         * Later:
         *
         * fetch("/bookings", {
         *     method: "POST",
         *     ...
         * })
         */


        setTimeout(() => {

            showBookingMessage(
                "Your order has been placed successfully!",
                "success"
            );


            button.disabled = false;

            button.textContent =
                "Confirm Order";


            /*
             * Later we will redirect to
             * the order confirmation page.
             */

        }, 1000);

    });

}


/*
 * Booking message
 */

function showBookingMessage(message, type) {

    const box =
        document.getElementById(
            "bookingMessage"
        );


    if (!box) {
        return;
    }


    box.textContent = message;


    box.classList.remove(
        "hidden",
        "message-success",
        "message-error"
    );


    if (type === "success") {

        box.classList.add(
            "message-success"
        );

    } else {

        box.classList.add(
            "message-error"
        );

    }

}