import os

class UserAuthentication:
    def __init__(self, filename="user_data.txt"):
        self._filename = filename

    def _write_to_file(self, data):
        with open(self._filename, "a") as file:
            file.write(data)

    def _read_from_file(self):
        if os.path.exists(self._filename):
            with open(self._filename, "r") as file:
                return file.readlines()
        return []

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        data = f"{username},{password}\n"
        self._write_to_file(data)

        print("Registration successful!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for line in self._read_from_file():
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                print("Login successful!")
                break
        
        else:
            print("Login failed. Please check your username and password.")
            self.login()

    def main_menu(self):
        print("1. Register")
        print("2. Login")
        
        while True:
            choice = input("Select an option (1 or 2): ")

            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    auth_system = UserAuthentication()
    auth_system.main_menu()
