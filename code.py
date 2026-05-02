class Car:
    def __init__(self, price: float, color: str, year: int, model: str, brand: str):
        self.price = price
        self.color = color
        self.year = year
        self.model = model
        self.brand = brand

    def __eq__(self, other) -> bool:
        if not isinstance(other, Car):
            return False
        return (self.brand == other.brand and
                self.model == other.model and
                self.year == other.year and
                self.price == other.price and
                self.color == other.color)

    def __str__(self) -> str:
        return f"Car({self.price}, {self.color}, {self.year}, {self.model}, {self.brand})"

def main():
        cars = [
            Car(20000, "Зелений", 2015, "Land Cruiser 300", "Toyota"),
            Car(6767, "Червоний", 1988, "ВАЗ-2101", "Lada"),
            Car(14880, "Жовтий", 1990, "Mercedes-Benz E-Class 1990", "Mercedes"),
            Car(7777, "Бірюзовий", 2020, "Corolla", "Toyota"),
            Car(50000, "Золотий", 2019, "Mustang", "Ford")
        ]

        print("Початковий масив")
        for car in cars:
            print(car)

        cars.sort(key=lambda c: (c.year, -c.price))

        print("Відсортований масив")
        for car in cars:
            print(car)

        search_car = Car(50000, "Золотий", 2019, "Mustang", "Ford")
        print(f"\nШукаємо автомобіль: {search_car}")

        if search_car in cars:
            index = cars.index(search_car)
            print(f"\nЄ в наявності під індексом {index}!")
        else:
            print("Пусто")

if __name__ == "__main__":
    main()
