// =========================================
// FOODBOOK - MENU JAVASCRIPT
// =========================================


document.addEventListener("DOMContentLoaded", () => {

    setupSearch();

    setupFilters();

    applyURLCategory();

});


/*
 * Search food
 */

function setupSearch() {

    const searchInput =
        document.getElementById("foodSearch");

    const cards =
        document.querySelectorAll(".food-card");

    const noResults =
        document.getElementById("noResults");


    if (!searchInput) {
        return;
    }


    searchInput.addEventListener("input", () => {

        const searchTerm =
            searchInput.value.toLowerCase().trim();

        let visibleCount = 0;


        cards.forEach((card) => {

            const foodName =
                card.dataset.name.toLowerCase();

            if (foodName.includes(searchTerm)) {

                card.style.display = "";

                visibleCount++;

            } else {

                card.style.display = "none";

            }

        });


        if (visibleCount === 0) {

            noResults.classList.remove("hidden");

        } else {

            noResults.classList.add("hidden");

        }

    });

}


/*
 * Category filters
 */

function setupFilters() {

    const filterButtons =
        document.querySelectorAll(".filter-btn");

    const cards =
        document.querySelectorAll(".food-card");

    const noResults =
        document.getElementById("noResults");


    filterButtons.forEach((button) => {

        button.addEventListener("click", () => {

            const category =
                button.dataset.category;


            /*
             * Update active button
             */

            filterButtons.forEach((btn) => {

                btn.classList.remove("active");

            });

            button.classList.add("active");


            /*
             * Filter food
             */

            let visibleCount = 0;


            cards.forEach((card) => {

                const cardCategory =
                    card.dataset.category;


                if (
                    category === "all" ||
                    cardCategory === category
                ) {

                    card.style.display = "";

                    visibleCount++;

                } else {

                    card.style.display = "none";

                }

            });


            if (visibleCount === 0) {

                noResults.classList.remove("hidden");

            } else {

                noResults.classList.add("hidden");

            }

        });

    });

}


/*
 * Category from URL
 *
 * Example:
 *
 * menu.html?category=rice
 */

function applyURLCategory() {

    const params =
        new URLSearchParams(window.location.search);

    const category =
        params.get("category");


    if (!category) {
        return;
    }


    const button =
        document.querySelector(
            `.filter-btn[data-category="${category}"]`
        );


    if (button) {

        button.click();

    }

}