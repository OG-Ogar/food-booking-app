const customer = {
    name: "Samuel",
    totalOrders: 12,
    activeOrders: 2,
    favoriteFoods: 5,
    totalSpent: 42500
};


document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("customerName").textContent =
        customer.name;

    document.getElementById("totalOrders").textContent =
        customer.totalOrders;

    document.getElementById("activeOrders").textContent =
        customer.activeOrders;

    document.getElementById("favoriteFoods").textContent =
        customer.favoriteFoods;

    document.getElementById("totalSpent").textContent =
        `₦${customer.totalSpent.toLocaleString()}`;

});