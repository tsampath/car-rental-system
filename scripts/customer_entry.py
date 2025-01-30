from tabulate import tabulate

from rental_services.controllers.customer_controller import CustomerController

class CustomerEntry():
    """Customer Entry for customer related operations."""

    def __init__(self):
        """Initialize CustomerController."""
        self.customer_controller = CustomerController()

    def main(self) -> int:
        """Customer management functionality."""        

        while True:
            print("\nCustomer Management")
            print("1. Search Customers")
            print("2. Add Customer")
            print("3. Back to Main Menu")
            choice = input("Please select an option (1/2/3): ").strip()

            match choice:
                case "1":
                    return_value = self.search_customers()
                    match return_value:
                        case 4:
                            continue
                        case 5:
                            return
                        case _:
                            pass
                case "2":
                    self.add_customer()
                case "3":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def search_customers(self) -> int:
        while True:
            print("1. Search All Customers")
            print("2. Search Customer by Name")
            print("3. Search Customer by Customer ID")
            print("4. Search by Customer Type")
            print("5. Search Customer by Price List")
            print("6. Back to Previous Menu")
            print("7. Back to Main Menu")
            search_choice = input("Please select an option (1/2/3/4/5/6/7): ").strip()
            match search_choice:
                case "1":
                    filtered_customers = self.customer_controller.get_all_customers()
                    if filtered_customers == None:
                        print("System was unable to find any customer")
                    else:
                        print(tabulate(self.convert_customer_entities_to_table(filtered_customers), headers="keys", tablefmt="grid"))
                        self.actions_on_selected_customer()
                case "2":
                    name = input("Please enter name: ").strip()
                    filtered_customers = self.customer_controller.get_customer_by_name(name)
                    if filtered_customers == None:
                        print("System was unable to find any customer as per filter criteria")
                    else:
                        print(tabulate(self.convert_customer_entities_to_table(filtered_customers), headers="keys", tablefmt="grid"))
                        self.actions_on_selected_customer()
                case "3":
                    customer_id = input("Please enter customer id: ").strip()
                    filtered_customer = self.customer_controller.get_customer_by_id(customer_id)
                    if filtered_customer == None:
                        print("System was unable to find any customer as per filter criteria")
                    else:
                        print(tabulate(filtered_customer, headers="keys", tablefmt="fancy_grid"))
                        self.actions_on_selected_customer()
                case "4":
                    print("Please enter customer type: ")
                    customer_type = input("Please select an option (1 -> Individual 2 -> Corporate): ").strip()
                    while True:
                        match search_choice:
                            case "1", "2":
                                filtered_customers = self.customer_controller.get_customers_by_type(int(customer_type))
                                if filtered_customers == None:
                                    print("System was unable to find any customer per filter criteria")
                                else:
                                    print(tabulate(self.convert_customer_entities_to_table(filtered_customers), headers="keys", tablefmt="grid"))
                                    self.actions_on_selected_customer()
                                break
                            case _:
                                print("Invalid choice. Please try again.")

                case "5":
                    print("Please enter price list id: ")
                    price_list = input("Please select an option (1 -> Standard 2 -> Loyal): ").strip()
                    while True:
                        match search_choice:
                            case "1", "2":
                                filtered_customers = self.customer_controller.get_customers_by_price_list(int(price_list))
                                if filtered_customers == None:
                                    print("System was unable to find any customer per filter criteria")
                                else:
                                    print(tabulate(self.convert_customer_entities_to_table(filtered_customers), headers="keys", tablefmt="grid"))
                                    self.actions_on_selected_customer()
                                break
                            case _:
                                print("Invalid choice. Please try again.")
                case "6":
                    return int(search_choice)
                case "7":
                    return int(search_choice)
                case _:
                    print("Invalid choice. Please try again.")
    
    def add_customer(self):
        print("Add a New Customer")

        name = input("Enter customer name: ").strip()
        building_name = input("Enter customer address unit/level/floor: ").strip()
        address_line_1 = input("Enter customer address street number and name: ").strip()
        address_line_2 = input("Enter customer address delivery suburb if any:")
        town = input("Enter address town/city: ")
        customer_type_id = self.validate_integer_input("Enter customer type (1 -> Individual 2 -> Corporate):")
        price_list_id = self.validate_integer_input("Please enter price list(1 -> Standard 2 -> Loyal):")

        # Check if all required fields are filled
        if not (name and building_name and address_line_1 and town):
            print("Error: Customer name, building name, address line 1 and town  are required. Please try again.")
            return

        customer_data = {
            "name": name,
            "building_name": building_name,
            "address_line_1": address_line_1,
            "address_line_2": address_line_2,
            "town": town,
            "customer_type_id": customer_type_id,
            "price_list_id": price_list_id
        }

        self.customer_controller.add_customer(customer_data)
        print(f"Customer added successfully: {customer_data}")

    def actions_on_selected_customer(self):
        while True:
            print("1. Book Car")
            print("2. Update Customer")
            print("3. Delete Customer")
            print("4. Back to Previous Menu")

            action_choice = input("Please select an option (1/2/3/4): ").strip()
            match action_choice:
                case "1":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_customer = self.customer_controller.get_customer_by_customer_id(registration_number)
                    print(tabulate(filtered_customer, headers="keys", tablefmt="fancy_grid"))
                case "2":
                    customer_id = self.validate_integer_input("Please enter customer id: ")
                    filtered_customer = self.customer_controller.get_customer_by_customer_id(customer_id)
                    if filtered_customer == None:
                        print("Customer not found!!")
                    else:
                        self.update_customer(filtered_customer.id, filtered_customer.customer_id)
                        print("Customer was updated successfully")
                        return

                case "3":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_customer = self.customer_controller.get_customer_by_customer_id(registration_number)
                    if filtered_customer == None:
                        print("Customer not found!!")
                    else: 
                        if self.customer_controller.delete_customer_by_id(filtered_customer.id):
                            print("Customer was deleted!!")
                        else:
                            print("Customer was not deleted due to some reason!!")

                case "4":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def update_customer(self, id: str, customer_Id: str):
        print("Update a Customer")
        name = input("Enter customer name: ").strip()
        building_name = input("Enter customer address unit/level/floor: ").strip()
        address_line_1 = input("Enter customer address street number and name: ").strip()
        address_line_2 = input("Enter customer address delivery suburb if any:")
        town = input("Enter address town/city: ")
        customer_type_id = self.validate_integer_input("Enter customer type (1 -> Individual 2 -> Corporate):")
        price_list_id = self.validate_integer_input("Please enter price list(1 -> Standard 2 -> Loyal):")

        # Check if all required fields are filled
        if not (name and building_name and address_line_1 and town):
            print("Error: Customer name, building name, address line 1 and town  are required. Please try again.")
            return

        customer_data = {
            "id": id,
            "customer_id": customer_Id,
            "name": name,
            "building_name": building_name,
            "address_line_1": address_line_1,
            "address_line_2": address_line_2,
            "town": town,
            "customer_type_id": customer_type_id,
            "price_list_id": price_list_id
        }

        if self.customer_controller.update_customer_by_id(id, customer_data) == None:
            print("Customer was not updated due to some issue")
        else:
            print("Customer was updated successfully")


    def validate_integer_input(self, prompt):
        """Utility function to validate integer input."""
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print("Invalid input. Please enter a valid integer.")

    def convert_customer_entities_to_table(self, customers):
        """Convert a list of CustomerEntity objects to a list of dictionaries for tabulation."""
        return [
            {
                "Id": customer.id,
                "Name": customer.name,
                "Unit/Level/Floor": customer.building_name,
                "Street Number and Name": customer.address_line_1,
                "Town": customer.town,
                "Customer Type": 'Individual' if customer.customer_type_id == 1 else 'Corporate',
                "Price List": 'Standard' if customer.price_list_id == 1 else 'Loyal'
            }
            for customer in customers
        ]

#todo: remove this line when testing done
# CustomerEntry().main()
