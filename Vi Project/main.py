class Wine:
    wine_type = {
        "1": "Tinto",
        "2": "Branco",
        "3": "Verde"
    }
    wine_country = {
        "1": "Portugal",
        "2": "France",
        "3": "Italy"
    }
    wine_star = {
        "1": "1 star",
        "2": "2 stars",
        "3": "3 stars",
        "4": "4 stars",
        "5": "5 stars"
    }
    size_map = {
        "1": "Bottle",
        "2": "Glass",
        "3": "Jar"
    }

    def run(self):
        print("Welcome to the Drink Maniacs!\n")
        type = self.get_wine_type()
        country = self.get_country_type()
        stars = self.get_stars_type()
        size = self.get_size()
        print("\nDelicious, great choice! Here is your {} {} {} {}!".format(type, country, stars, size))

    def print_message(self):
        print("\nI'm sorry, I did not understand your preference.\n"
              "Please enter the corresponding number for your response.\n")

    def print_message(self):
        print("\nI'm sorry, I did not understand your preference.\n"
              "Please enter the corresponding number for your response.\n")

    def get_wine_type(self):
        res = input(
            "What type of wine would you like?\n \n1- Tinto \n2- Branco \n3- Verde \n> ")

        if res in self.wine_type:
            return self.wine_type.get(res)
        else:
            self.print_message()
            return self.wine_type()

    def get_country_type(self):
        res = input(
            "From which country would you like?\n \n1- Portugal \n2- France \n3- Italy \n> ")

        if res in self.wine_country:
            return self.wine_country.get(res)
        else:
            self.print_message()
            return self.wine_country_type()

    def get_stars_type(self):
        res = input(
            "Stars would you like to give?\n \n1- 1 star \n2- 2 stars \n3- 3 stars \n4-  4 stars \n5- 5 stars\n> ")

        if res in self.wine_star:
            return self.wine_star.get(res)
        else:
            self.print_message()
            return self.get_stars_type()

    def get_size(self):
        res = input(
            "\nWhat size drink can I get for you?\n \n1- Bottle \n2- Glass \n3- Jar \n> ")
        if res in self.size_map:
            return self.size_map.get(res)
        else:
            self.print_message()
            return self.get_size()


maniacs = Wine()
maniacs.run()
