class Pizza:
    def __init__(self, ingredients: set, id):
        self.ingredients = ingredients
        self.id = id

    @property
    def n_ingredients(self):
        return len(self.ingredients)


class Delivery:
    def __init__(self, pizzas_ids: list):
        self.pizzas_ids = pizzas_ids

    def get_output(self):
        team_size = len(self.pizzas_ids)
        return str(team_size) + " " + " ".join(self.pizzas_ids) + "\n"


if __name__ == "__main__":
    pizzas = list()

    with open("e.in", "r") as f:
        n_pizzas, n_teams_of_2, n_teams_of_3, n_teams_of_4 = map(int, f.readline().split())
        for idx in range(n_pizzas):
            n_ingredients, *ingredients = f.readline().split()
            pizzas.append(Pizza(ingredients=set(ingredients), id=idx))

    pizzas.sort(key=lambda pizza: pizza.n_ingredients, reverse=True)

    deliveries = list()
    n_pizzas_delivered = 0
    for _ in range(n_teams_of_2):
        if n_pizzas_delivered + 2 > n_pizzas:
            break
        deliveries.append(Delivery(
            pizzas_ids=[str(pizza.id) for pizza in pizzas[n_pizzas_delivered:n_pizzas_delivered+2]]
        ))
        n_pizzas_delivered += 2

    for _ in range(n_teams_of_3):
        if n_pizzas_delivered + 3 > n_pizzas:
            break
        deliveries.append(Delivery(
            pizzas_ids=[str(pizza.id) for pizza in pizzas[n_pizzas_delivered:n_pizzas_delivered+3]]
        ))
        n_pizzas_delivered += 3

    for _ in range(n_teams_of_4):
        if n_pizzas_delivered + 4 > n_pizzas:
            break
        deliveries.append(Delivery(
            pizzas_ids=[str(pizza.id) for pizza in pizzas[n_pizzas_delivered:n_pizzas_delivered+4]]
        ))
        n_pizzas_delivered += 4

    with open("e.out", "w") as f:
        f.write(f"{len(deliveries)}\n")
        for delivery in deliveries:
            f.write(delivery.get_output())
