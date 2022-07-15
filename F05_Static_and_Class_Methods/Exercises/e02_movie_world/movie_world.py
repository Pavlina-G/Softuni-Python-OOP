from customer import Customer
from dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        dvd_capacity = 15
        return dvd_capacity

    @staticmethod
    def customer_capacity():
        customer_capacity = 10
        return customer_capacity

    def add_customer(self, customer: Customer):
        if len(self.customers) >= self.customer_capacity():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) >= self.dvd_capacity():
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_obj_by_id(self.customers, customer_id)
        dvd = self.__find_obj_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_obj_by_id(self.customers, customer_id)
        dvd = self.__find_obj_by_id(self.dvds, dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return '\n'.join([repr(c) for c in self.customers]) + '\n' + '\n'.join([repr(d) for d in self.dvds])


    @staticmethod
    def __find_obj_by_id(list_obj, obj_id):
        for obj in list_obj:
            if obj.id == obj_id:
                return obj

