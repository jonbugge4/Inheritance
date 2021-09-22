class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone


    def print_person(self):
        print('Name: ', self.__name)
        print('Address: ', self.__address)
        print('Telephone: ', self.__telephone)

class Customer(Person):
    def __init__(self, name, address, telephone, cust_number, on_list):
        Person.__init__(self, name, address, telephone, cust_number,on_list)



        #initalize cust_list
        self.cust_number = cust_number
        self.on_list = on_list

    def print_person





