

# PART 1

def part1():

    print("Part 1: Discount Prices")

    def Student_Discount(price):
        return price - (price * .10)

    def Reg_Discount(price):
        price = Student_Discount(price)
        return price - (price * .05)

    orig_price = 100
    disc_price = Reg_Discount(orig_price)
    print("Original price:", orig_price)
    print("Dicounted price:", disc_price)

# PART 2
    
def part2():

    print("\nPart 2: Lambda Expression")
    print((lambda x : x * (x + 5) ** 2)(5))

# PART 3
    
def part3():

    print("\nPart 3: Discount List of Prices")

    def Discount_Ten(price):
        return price - (price * .10)
    
    prod_prices = [15.99, 49.99, 25.49, 30.20, 12.59, 24.95]
    print("Original prices:", prod_prices)
    prod_prices = list(map(Discount_Ten, prod_prices))
    print("Discounted prices:", prod_prices)

# PART 4
    
def part4():

    print("\nPart 4: Object-Oriented Programming")

    class Computer:
        processor = ''
        cores = 0
        price = 0

        def __init__(self, processor, cores, price):
            self.processor = processor
            self.cores = cores
            self.price = price

        def Display_Specs(self):
            print("Processor:", self.processor)
            print("Number of cores:", self.cores)
            print("Price: $" + str(self.price))

        def Get_Processor(self):
            return self.processor
        
        def Get_Cores(self):
            return self.cores
        
        def Get_Price(self):
            return self.price

    class Desktop(Computer):
        power_draw = 0

        def __init__(self, processor, cores, price, power):
            self.processor = processor
            self.cores = cores
            self.price = price
            self.power_draw = power

        def Display_Specs(self):
            print("Processor:", self.processor)
            print("Number of cores:", self.cores)
            print("Price: $" + str(self.price))
            print("Power draw:", self.power_draw, "watts")

        def Get_Power_Draw(self):
            return self.power_draw

    class Laptop(Computer):
        battery_capacity = 0

        def __init__(self, processor, cores, price, battery):
            self.processor = processor
            self.cores = cores
            self.price = price
            self.battery_capacity = battery

        def Display_Specs(self):
            print("Processor:", self.processor)
            print("Number of cores:", self.cores)
            print("Price: $" + str(self.price))
            print("Battery Capacity:", self.battery_capacity, "mWh")   

        def Get_Battery_Capacity(self): 
            return self.battery_capacity

    my_laptop = Laptop("Intel Core I5", 12, 500, 12000)
    my_laptop.Display_Specs()
    print()
    print(my_laptop.Get_Cores(), "Cores", my_laptop.Get_Processor(), "processor", my_laptop.Get_Price(), "Dollars", my_laptop.Get_Battery_Capacity(), "mWh")

# PART 5
        
def part5():

    print("\nPart 5: Overloading Operators")

    class Variable:

        def __init__(self, v):
            self.value = v

        def __mul__(self, other):
            return self.Get_Value() + other.Get_Value()
        
        def Set_Value(self, v):
            self.value = v

        def Get_Value(self):
            return self.value
    
    var1 = Variable(5)

    var2 = Variable(6)

    print(var1 * var2)

    

# MAIN
    
part1()
part2()
part3()
part4()
part5()