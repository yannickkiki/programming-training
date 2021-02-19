import itertools


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.n_ingredients = len(self.ingredients)


input_filename, output_filename = "a.in", "a.out_74"

pizzas = []
with open(input_filename, "r") as f:
    n_pizzas, *_ = map(int, f.readline().split())
    for _ in range(n_pizzas):
        n_ingredients, *ingredients = f.readline().split()
        pizzas.append(Pizza(ingredients=ingredients))


class Delivery:
    pizzas_all = pizzas

    def __init__(self, pizzas_ids):
        self.pizzas_ids = pizzas_ids
        self.team_size = len(self.pizzas_ids)

    def get_n_ingredients(self):
        ingredients = []
        for pizza_id in self.pizzas_ids:
            ingredients = list(set(ingredients + self.pizzas_all[pizza_id].ingredients))


if __name__ == "__main__":

    deliveries = []
    with open(output, "r") as f:
        n_deliveries = int(f.readline())
        for _ in range(n_deliveries):
            team_size, *pizzas_ids = map(int, f.readline().split())
            deliveries.append(pizzas_ids)

    deliveries_optimized = deliveries[:]

    delivery_i = deliveries[0]
    for delivery_j in deliveries[1:]:
        pizzas_ids_ij = delivery_i.pizzas_ids + delivery_j.pizzas_ids
        for new_pizzas_ids_i in itertools.combinations(pizzas_ids_ij, delivery_i.team_size):
            new_pizzas_ids_j = set(pizzas_ids_ij) - set(new_pizzas_ids_i)



