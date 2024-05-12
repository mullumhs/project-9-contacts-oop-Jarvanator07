"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.

class Contact:
    total_contacts = 0
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.total_contacts += 1

# Create at least two instances of the Contact class with different data.

contact1 = Contact("John", "0797979797")
contact2 = Contact("Jane", "0787878787")

# Write code that prints out the details of each contact you have created.

print(contact1.name, contact1.phone_number)
print(contact2.name, contact2.phone_number)

