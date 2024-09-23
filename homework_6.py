from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    
    def __init__(self, value) :
        self.value = value.capitalize()
        
	


class Phone(Field):
    def __init__(self, value):
        if re.fullmatch(r'\d{10}', value) :
            super().__init__(value)
        else :
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone) :
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone) :
        founded_phone = self.find_phone(phone)
        if founded_phone :
            self.phones.remove(founded_phone)
    
    def edit_phone(self, old_phone, new_phone) :
        founded_phone = self.find_phone(old_phone)
        if founded_phone :
            new_phone = Phone(new_phone)
            self.phones.insert(self.phones.index(founded_phone), new_phone)
            self.phones.remove(founded_phone)
        else :
            raise ValueError
           
    def find_phone(self, phone) :
        for phone_object in self.phones:
            if phone_object.value == phone:
                return phone_object
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record) :
        self.data[record.name.value] = record
    
    def find(self, name) :
        if name in self.data.keys() :
            return self.data[name]
        else :
            return None
    
    def delete(self, name) :
        del self.data[name]
    
    def __str__(self) :
        return f"List of persons : {'; '.join(person for person in self.data )}"
    
        
        
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")