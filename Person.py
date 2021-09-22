import PersonClass as p

def main():

    name = 'John'
    address = '1234 main st'
    telephone = '555-444-3333'
    cust_number = 1234
    on_list_flag = False
    john_person = p.Person(name, address, telephone)

    john_customer = p.Customer(
        name, address, telephone, cust_number, on_list_flag)
   
   
    john_person.print_person()

main()
    
