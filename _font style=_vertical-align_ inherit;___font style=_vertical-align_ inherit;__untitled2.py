class Car:
    def __init__(self, make, model, year):
        """
        Ініціалізує об'єкт автомобіля.
        :param make: Марка автомобіля
        :param model: Модель автомобіля
        :param year: Рік випуску автомобіля
        """
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        """
        Повертає рядок з інформацією про автомобіль.
        :return: Рядок у форматі "[рік] [марка] [модель]"
        """
        return f"{self.year} {self.make} {self.model}"


# Приклад використання
if __name__ == "__main__":
    # Створення об'єкта автомобіля
    car = Car("Toyota", "Camry", 2020)

    # Виведення інформації про автомобіль
    print(car.get_info())  # Виведе: "2020 Toyota Camry"
