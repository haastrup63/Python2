class Beer: 
    name = ""
    percentage = 0
    brand = ""

    def __init__(self, name, percentage, brand): 
        self.name = name
        self.percentage = percentage
        self.brand = brand

    def print_beer(self): 
        print(self.name + " " + str(self.percentage) + " " + self.brand)

    def change_percentage(self, new_percentage): 
        self.percentage = new_percentage