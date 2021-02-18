import itertools


class Pizza:
    def __init__(self, ingredients, id):
        self.ingredients = ingredients
        self.n_ingredients = len(self.ingredients)
        self.id = id


class Delivery:
    def __init__(self, pizzas_ids, ingredients):
        self.pizzas_ids = pizzas_ids
        self.ingredients = ingredients
        self.n_ingredients = len(self.ingredients)


class Submission:
    def __init__(self, deliveries):
        self.deliveries = deliveries

    def create_submission_file(self, filename):
        score = 0
        result = f"{len(self.deliveries)}\n"
        for delivery in deliveries:
            team_size = len(delivery.pizzas_ids)
            result += str(team_size) + " " + " ".join(delivery.pizzas_ids) + "\n"
            score += delivery.n_ingredients ** 2

        if filename == "a.out" and score <= 74:
            return
        if filename == "b.out" and score <= 7338:
            return
        if filename == "c.out" and score <= 687305267:
            return
        if filename == "d.out" and score <= 5887484:
            return
        if filename == "e.out" and score <= 8348932:
            return

        with open(f"{filename}_{score}", "w") as f:
            f.write(result)


if __name__ == "__main__":
    for dataset in ["a", "b", "c", "d", "e"]:
        pizzas = list()

        with open(f"{dataset}.in", "r") as f:
            n_pizzas, n_teams_of_2, n_teams_of_3, n_teams_of_4 = map(int, f.readline().split())
            for idx in range(n_pizzas):
                n_ingredients, *ingredients = f.readline().split()
                pizzas.append(Pizza(ingredients=ingredients, id=idx))
            n_teams_of_x_tuples = [(4, n_teams_of_4), (3, n_teams_of_3), (2, n_teams_of_2)]

        for is_reverse in [True, False]:
            pizzas.sort(key=lambda pizza: pizza.n_ingredients, reverse=is_reverse)

            for n_teams_of_x_tuples_perm in itertools.permutations(n_teams_of_x_tuples, 3):
                deliveries = list()
                n_pizzas_delivered = 0

                for team_size, n_teams in n_teams_of_x_tuples_perm:
                    for _ in range(n_teams):
                        if n_pizzas_delivered + team_size > n_pizzas:
                            break

                        pizzas_to_deliver = pizzas[n_pizzas_delivered:n_pizzas_delivered+team_size]

                        ids, ingredients = [], []
                        for pizza in pizzas_to_deliver:
                            ids.append(str(pizza.id))
                            ingredients += pizza.ingredients
                        ingredients = list(set(ingredients))

                        deliveries.append(Delivery(pizzas_ids=ids, ingredients=ingredients))
                        n_pizzas_delivered += team_size

                submission = Submission(deliveries)
                submission.create_submission_file(filename=f"{dataset}.out")
