class ContactBot:
    def __init__(self):
        self.contacts = {}

    def input_error(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except KeyError:
                return "Enter user name"
            except (ValueError, IndexError):
                return "Invalid input. Give me name and phone please"

        return wrapper

    @input_error
    def add_contact(self, input_text):
        parts = input_text.split(' ')
        name, phone = parts[1], parts[2]
        self.contacts[name] = phone
        return f"Added contact: {name}, {phone}"

    @input_error
    def change_contact(self, input_text):
        parts = input_text.split(' ')
        name, new_phone = parts[1], parts[2]
        self.contacts[name] = new_phone
        return f"Changed contact: {name}, {new_phone}"

    @input_error
    def get_phone(self, input_text):
        name = input_text.split(' ')[1]
        return f"Phone for {name}: {self.contacts[name]}"

    def show_all(self):
        if not self.contacts:
            return "No contacts found"
        return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def main(self):
        print("How can I help you?")
        while True:
            user_input = input()
            user_input = user_input.lower()
            if user_input in ["good bye", "close", "exit"]:
                print("Good bye!")
                break
            elif user_input.startswith("add "):
                response = self.add_contact(user_input)
            elif user_input.startswith("change "):
                response = self.change_contact(user_input)
            elif user_input.startswith("phone "):
                response = self.get_phone(user_input)
            elif user_input == "show all":
                response = self.show_all()
            else:
                response = "Invalid command. Please try again."
            print(response)
