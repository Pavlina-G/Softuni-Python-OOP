class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        r = 1
        for x in args:
            r *= x
        return r

    @staticmethod
    def divide(first_num, *args):
        d = first_num
        for x in args:
            if x == 0:
                raise ValueError('Zero division error!')
            d /= x
        return d

    @staticmethod
    def subtract(first_num, *args):
        s = first_num
        for x in args:
            s -= x
        return s


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
