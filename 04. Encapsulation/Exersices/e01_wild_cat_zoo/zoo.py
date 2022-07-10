from F04_Encapsulation.exercises.e01_wild_cat_zoo.animal import Animal
from F04_Encapsulation.exercises.e01_wild_cat_zoo.caretaker import Caretaker
from F04_Encapsulation.exercises.e01_wild_cat_zoo.cheetah import Cheetah
from F04_Encapsulation.exercises.e01_wild_cat_zoo.keeper import Keeper
from F04_Encapsulation.exercises.e01_wild_cat_zoo.lion import Lion
from F04_Encapsulation.exercises.e01_wild_cat_zoo.tiger import Tiger
from F04_Encapsulation.exercises.e01_wild_cat_zoo.vet import Vet
from F04_Encapsulation.exercises.e01_wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self,worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def get_total_salaries(self):
        sum = 0
        for worker in self.workers:
            sum += worker.salary
        return sum

    def pay_workers(self):
        if self.__budget < self.get_total_salaries():
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= self.get_total_salaries()
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def get_total_animal_cost(self):
        sum = 0
        for animal in self.animals:
            sum += animal.money_for_care
        return sum

    def tend_animals(self):
        if self.__budget < self.get_total_animal_cost():
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= self.get_total_animal_cost()
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]

        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]

        result += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'
        result += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'
        result += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return result