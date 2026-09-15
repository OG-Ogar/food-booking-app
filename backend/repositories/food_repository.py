from models.food import Food


def get_foods():

    foods = [
        Food(1, "Jollof Rice", 2500, "Nigerian Food", 10),
        Food(2, "Fried Rice", 3000, "Nigerian Food", 5),
        Food(3, "Pizza", 5000, "Fast Food", 3),
        Food(4, "Burger", 3500, "Fast Food", 0),
        Food(5, "Chicken", 4000, "Protein", 8)
    ]

    return foods