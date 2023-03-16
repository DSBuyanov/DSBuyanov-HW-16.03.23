phonebook = [
    ["Иванов", "Иван", "Иванович", "+7 (999) 111-11-11"],
    ["Петров", "Петр", "Петрович", "+7 (999) 222-22-22"],
    ["Сидоров", "Сидор", "Сидорович", "+7 (999) 333-33-33"]
]

with open("phonebook.txt", "w", encoding='UTF-8') as file:
    for contact in phonebook:
        file.write(", ".join(contact) + "\n")


def change_contact_by_name(name):
    for contact in phonebook:
        if name.lower() in contact[1].lower():
            new_name = input("Enter new name: ")
            new_surname = input("Enter new surname: ")
            new_phone = input("Enter new phone number: ")
            contact[0] = new_surname
            contact[1] = new_name
            contact[2] = new_name + "ович"
            contact[3] = new_phone
            print("Contact has been updated successfully!")
            break
    else:
        print("Contact not found.")

# Функция редактирования контакта закоментирована:
# name = input("Enter name to change: ")
# change_contact_by_name(name)

def delete_contact_by_name(name, surname):
    for i, contact in enumerate(phonebook):
        if name.lower() in contact[1].lower() and surname.lower() in contact[0].lower():
            del phonebook[i]
            print("Contact has been deleted successfully!")
            break
    else:
        print("Contact not found.")


name = input("Enter name to delete: ")
surname = input("Enter surname to delete: ")
delete_contact_by_name(name, surname)

with open("phonebook.txt", "w", encoding='UTF-8') as file:
    for contact in phonebook:
        file.write(", ".join(contact) + "\n")
