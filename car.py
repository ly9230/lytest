class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describ_name(self):
        """返回汽车描述"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """显示汽车里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程设定为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        """增加里程"""
        self.odometer_reading += miles


class Battery:
    """定义一个电池"""

    def __init__(self,battery_size=40):
        """初始化电池属性"""
        self.battery_size = battery_size

    def descirb_battery(self):
        """描述电池信息"""
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size ==65:
            range = 225

        print(f"This car can go about {range} mile on a full charge.")


class ElectricCar(Car):
    """电动车"""

    def __init__(self,make,model,year):
        """
        初始化父类的属性,定义电动车自己的属性
        """
        super().__init__(make,model,year)
        self.battery = Battery()
