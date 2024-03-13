import random

class City:
    def __init__(self):
        self.streets = []

    def add_street(self):
        street = []
        num_houses = random.randint(5, 20)
        for i in range(1, num_houses + 1):
            population = random.randint(1, 100)
            street.append((i, population))
        self.streets.append(street)

    def remove_street(self, street_index):
        if 0 <= street_index < len(self.streets):
            del self.streets[street_index]
        else:
            print("Вулиці з таким індексом не існує.")

    def get_population(self):
        total_population = sum(sum(house[1] for house in street) for street in self.streets)
        return total_population

    def print_city_table(self):
        print("Вулиця\tБудинок\tНаселення")
        for i, street in enumerate(self.streets, start=1):
            for house in street:
                print(f"{i}\t{house[0]}\t{house[1]}")

# Приклад використання класу
city = City()
city.add_street()
city.add_street()
city.print_city_table()

print("Загальне населення:", city.get_population())
 