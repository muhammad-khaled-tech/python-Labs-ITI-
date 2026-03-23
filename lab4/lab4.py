import json

class Person:
    moods = ('happy', 'tired', 'lazy')

    def __init__(self, name, money, healthRate):
        self.name = name
        self.money = money
        self.healthRate = healthRate
        self.mood = Person.moods[0]

    def sleep(self, hours):
        if hours == 7:
            self.mood = Person.moods[0]
        elif hours < 7:
            self.mood = Person.moods[1]
        else:
            self.mood = Person.moods[2]

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            self._velocity = 0

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value
        else:
            self._fuelRate = 0

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = distance * 1.0

        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            covered_distance = self.fuelRate
            remaining = distance - covered_distance
            self.fuelRate = 0
            self.stop(remaining)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance == 0:
            print(f"Arrived! Remaining fuel: {self.fuelRate}%")
        else:
            print(f"Stopped! Remaining distance: {remain_distance}km")


class Employee(Person):
    def __init__(self, name, money, healthRate, id, email, salary, distanceToWork):
        super().__init__(name, money, healthRate)
        self.id = id
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.car = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            self._salary = 1000

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        if 0 <= value <= 100:
            self._healthRate = value
        else:
            self._healthRate = 0 if value < 0 else 100

    def work(self, hours):
        if hours == 8:
            self.mood = Person.moods[0]
        elif hours > 8:
            self.mood = Person.moods[1]
        else:
            self.mood = Person.moods[2]

    def drive(self, distance):
        if self.car:
            self.car.run(60, distance)

    def refuel(self, gasAmount=100):
        if self.car:
            self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        with open("email.txt", "w") as f:
            f.write(f"From: {self.email}\nTo: {to}\nHi, {receiver_name}\n{msg}\nThanks\n{subject}")


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, empId):
        self.employees = [e for e in self.employees if e.id != empId]

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for e in self.employees:
            if e.id == empId:
                return e
        return None

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp: emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp: emp.salary += reward

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, 60)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    def save_to_json(self):
        data = {
            "office_name": self.name,
            "employees": [
                {"id": e.id, "name": e.name, "salary": e.salary} for e in self.employees
            ]
        }
        with open("office_data.json", "w") as f:
            json.dump(data, f)
