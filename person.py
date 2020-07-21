from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def __repr__(self):
        return "Person('{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}'".format(self.first_name, self.last_name, self.birth_date, self.job, self.working_years, self.salary, self.country, self.city, self.gender)
    
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def age(self):
        a = self.birth_date.split('.')
        a = datetime(int(a[2]), int(a[1]), int(a[0]))
        b = datetime(2018,1,1)
        result = b - a
        result = int(result.days/365)
        return result
    
    def work(self):
        if self.gender == 'male':
            return "He is a {}".format(self.job)
        if self.gender == 'female':
            return "She is a {}".format(self.job)
        if self.gender == 'unknown':
            return "Is a {}".format(self.job)
    
    def money(self):
        total = self.working_years * 12 * self.salary
        total = str(total)[::-1]
        total = ' '.join(total[i:i+3] for i in range(0, len(total), 3))[::-1]
        return total

    def home(self):
        return "Lives in {}, {}".format(self.city, self.country)


a = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
print(a.home())