const profileForm = document.getElementById("profileForm");

const editBtn = document.getElementById("editBtn");

const cancelBtn = document.getElementById("cancelBtn");

const saveBtn = document.getElementById("saveBtn");

const logoutBtn = document.getElementById("logoutBtn");

const profileMessage =
    document.getElementById("profileMessage");


const inputs = [
    document.getElementById("fullName"),
    document.getElementById("email"),
    document.getElementById("phone"),
    document.getElementById("address")
];


let originalValues = {};


function enableEditing() {

    inputs.forEach(input => {
        input.disabled = false;
    });

    editBtn.classList.add("hidden");

    cancelBtn.classList.remove("hidden");

    saveBtn.classList.remove("hidden");
}


function disableEditing() {

    inputs.forEach(input => {
        input.disabled = true;
    });

    editBtn.classList.remove("hidden");

    cancelBtn.classList.add("hidden");

    saveBtn.classList.add("hidden");
}


function saveOriginalValues() {

    originalValues = {};

    inputs.forEach(input => {
        originalValues[input.id] = input.value;
    });
}


function restoreOriginalValues() {

    inputs.forEach(input => {
        input.value = originalValues[input.id];
    });
}


editBtn.addEventListener("click", () => {

    saveOriginalValues();

    enableEditing();

});


cancelBtn.addEventListener("click", () => {

    restoreOriginalValues();

    disableEditing();

    profileMessage.textContent = "";

});


profileForm.addEventListener("submit", (event) => {

    event.preventDefault();


    const name = document
        .getElementById("fullName")
        .value.trim();

    const email = document
        .getElementById("email")
        .value.trim();

    const phone = document
        .getElementById("phone")
        .value.trim();


    if (!name || !email || !phone) {

        profileMessage.textContent =
            "Please fill in all required fields.";

        return;
    }


    /*
        Later:

        fetch("/customers/me", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(...)
        });
    */


    document.getElementById("profileName").textContent =
        name;

    document.getElementById("profileEmail").textContent =
        email;

    document.getElementById("profilePhone").textContent =
        phone;


    profileMessage.textContent =
        "Profile updated successfully.";

    disableEditing();

});


logoutBtn.addEventListener("click", () => {

    /*
        Later this will call the backend:

        POST /auth/logout
    */

    const confirmLogout =
        confirm("Are you sure you want to logout?");

    if (!confirmLogout) {
        return;
    }


    // Temporary frontend logout
    localStorage.removeItem("token");

    window.location.href = "login.html";

});