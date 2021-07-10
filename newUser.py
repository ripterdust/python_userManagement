class User:
    def __init__(self, first_name, last_name, gender, country, age):
        self.default = 'Unknow'
        self.first_name = first_name or self.default 
        self.last_name = last_name or self.default
        self.gender = gender or self.default
        self.country = country or self.default
        self.age = age or self.default

    def get_data (self):
        return (self.first_name, self.last_name, self.gender, self.country, self.age)