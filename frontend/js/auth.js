// =========================================
// FOODBOOK - AUTHENTICATION JAVASCRIPT
// =========================================


document.addEventListener("DOMContentLoaded", () => {

    setupPasswordToggles();

    setupLogin();

    setupRegistration();

});


/*
 * Show / hide password
 */

function setupPasswordToggles() {

    const buttons = document.querySelectorAll(".password-toggle");

    buttons.forEach((button) => {

        button.addEventListener("click", () => {

            const targetId = button.dataset.target;

            const input = document.getElementById(targetId);

            if (!input) {
                return;
            }

            if (input.type === "password") {

                input.type = "text";

                button.textContent = "Hide";

            } else {

                input.type = "password";

                button.textContent = "Show";

            }

        });

    });

}


/*
 * Login
 */

function setupLogin() {

    const form = document.getElementById("loginForm");

    if (!form) {
        return;
    }

    form.addEventListener("submit", async (event) => {

        event.preventDefault();

        const phone = document.getElementById("phone").value.trim();

        const password = document.getElementById("password").value;

        const button = document.getElementById("loginButton");


        if (!phone || !password) {

            showAuthMessage(
                "Please enter your phone number and password.",
                "error"
            );

            return;
        }


        button.disabled = true;

        button.textContent = "Logging in...";


        /*
         * Backend integration will go here.
         *
         * Example later:
         *
         * const response = await fetch("/login", {
         *     method: "POST",
         *     headers: {
         *         "Content-Type": "application/json"
         *     },
         *     body: JSON.stringify({
         *         phone,
         *         password
         *     })
         * });
         */


        // Temporary frontend simulation

        setTimeout(() => {

            showAuthMessage(
                "Login form is working. Backend connection will be added next.",
                "success"
            );

            button.disabled = false;

            button.textContent = "Login";

        }, 800);

    });

}


/*
 * Registration
 */

function setupRegistration() {

    const form = document.getElementById("registerForm");

    if (!form) {
        return;
    }

    form.addEventListener("submit", async (event) => {

        event.preventDefault();


        const fullName =
            document.getElementById("fullName").value.trim();

        const phone =
            document.getElementById("registerPhone").value.trim();

        const location =
            document.getElementById("location").value.trim();

        const password =
            document.getElementById("registerPassword").value;

        const confirmPassword =
            document.getElementById("confirmPassword").value;

        const button =
            document.getElementById("registerButton");


        if (
            !fullName ||
            !phone ||
            !location ||
            !password ||
            !confirmPassword
        ) {

            showAuthMessage(
                "Please fill in all fields.",
                "error"
            );

            return;
        }


        if (password.length < 6) {

            showAuthMessage(
                "Password must be at least 6 characters.",
                "error"
            );

            return;
        }


        if (password !== confirmPassword) {

            showAuthMessage(
                "Passwords do not match.",
                "error"
            );

            return;
        }


        button.disabled = true;

        button.textContent = "Creating account...";


        /*
         * Backend integration will go here.
         */


        // Temporary frontend simulation

        setTimeout(() => {

            showAuthMessage(
                "Registration form is working. Backend connection will be added next.",
                "success"
            );

            button.disabled = false;

            button.textContent = "Create Account";

        }, 800);

    });

}


/*
 * Display authentication messages
 */

function showAuthMessage(message, type) {

    const messageBox =
        document.getElementById("authMessage");

    if (!messageBox) {
        return;
    }

    messageBox.textContent = message;

    messageBox.classList.remove(
        "hidden",
        "message-success",
        "message-error"
    );


    if (type === "success") {

        messageBox.classList.add("message-success");

    } else {

        messageBox.classList.add("message-error");

    }

}