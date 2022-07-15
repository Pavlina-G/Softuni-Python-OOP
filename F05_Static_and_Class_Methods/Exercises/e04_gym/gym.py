from customer import Customer
from equipment import Equipment
from exercise_plan import ExercisePlan
from subscription import Subscription
from trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def adding_object(obj_list, obj):
        if obj in obj_list:
            return
        obj_list.append(obj)
        return obj_list

    def add_customer(self, customer: Customer):
        self.adding_object(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.adding_object(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.adding_object(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.adding_object(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.adding_object(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_obj_by_id(self.subscriptions, subscription_id)
        customer = self.__find_obj_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_obj_by_id(self.trainers, subscription.trainer_id)
        exercise_plan = self.__find_obj_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_obj_by_id(self.equipment, exercise_plan.equipment_id)

        return repr(subscription) + '\n' + \
               repr(customer) + '\n' + \
               repr(trainer) + '\n' + \
               repr(equipment) + '\n' + \
               repr(exercise_plan)

    def __find_obj_by_id(self, obj_list, obj_id):
        for obj in obj_list:
            if obj.id == obj_id:
                return obj

# g = Gym()
# g.add_customer('test')
# print(g.customers)
