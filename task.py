from abc import ABC, abstractmethod

class BookableItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        
        self.__base_price = 0  
        self.set_base_price(base_price)

    def get_base_price(self):
        return self.__base_price

    def set_base_price(self, price):
        
        if price > 0:
            self.__base_price = price
        else:
            print("Invalid Price! Price must be positive.")

    @abstractmethod
    def calculate_item_cost(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class HotelRoom(BookableItem):
    def __init__(self, name, base_price, bed_size, smoking_allowed):
        super().__init__(name, base_price)
        self.bed_size = bed_size
        self.smoking_allowed = smoking_allowed

    
    def calculate_item_cost(self):
        return self.get_base_price() * 1.15

    def display_details(self):
        smoke = "Allowed" if self.smoking_allowed else "Non-Smoking"
        return f"[Room] {self.name} ({self.bed_size}, {smoke}) - Base: ${self.get_base_price()}"


class SpaService(BookableItem):
    def __init__(self, name, base_price, duration):
        super().__init__(name, base_price)
        self.duration = duration

    def calculate_item_cost(self):
        return self.get_base_price() * 1.20

    def display_details(self):
        return f"[Service] {self.name} ({self.duration} mins) - Base: ${self.get_base_price()}"


class CustomerReservation:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def print_final_bill(self):
        print("\n" + "="*40)
        print("         HOTEL FINAL BILL         ")
        print("="*40)
        total = 0
        for item in self.items:
            cost = item.calculate_item_cost()
            total += cost
            print(f"{item.name:<20} | ${cost:>8.2f}")
        print("-" * 40)
        print(f"{'TOTAL (with tax):':<20} | ${total:>8.2f}")
        print("="*40 + "\n")


def main():
    
    offerings = [
        HotelRoom("Suite 101", 200, "King", False),
        HotelRoom("Room 202", 100, "Twin", True),
        SpaService("Massage", 80, 60),
        SpaService("Sauna", 50, 30)
    ]
    
    res = CustomerReservation()

    while True:
        print("\n--- Hotel Management System ---")
        print("1. View Offerings")
        print("2. Add to Reservation")
        print("3. Print Bill & Checkout")
        print("4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            print("\nAvailable Offerings:")
            for i, item in enumerate(offerings, 1):
                print(f"{i}. {item.display_details()}")
        
        elif choice == '2':
            try:
                idx = int(input("Enter Item Number to add: ")) - 1
                if 0 <= idx < len(offerings):
                    res.add_item(offerings[idx])
                    print(f"Added {offerings[idx].name} to reservation.")
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                # Requirement 5: Error Handling
                print("Error: Please enter a valid numeric ID.")
        
        elif choice == '3':
            if not res.items:
                print("Your reservation is empty!")
            else:
                res.print_final_bill()
                print("Thank you for staying with us!")
                break
        
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()