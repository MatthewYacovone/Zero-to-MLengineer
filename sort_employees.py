def sort_employees(employees, sort_by):
    sorting_indicies = ["name", "age", "salary"]
    idx = sorting_indicies.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[idx])

    return sorted_employees


employees = [
    ["John", 25, 25000],
    ["Sarah", 30, 64000],
    ["Mike", 18, 29000],
    ["Susan", 29, 40000],
]

sort_by = "age"
sorted_employees = sort_employees(employees, sort_by)


class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

apple = Fruit("Apple", 10)
banana = Fruit("Banana", 12)

print(apple.name, apple.calories)
print(banana.name, banana.calories)

