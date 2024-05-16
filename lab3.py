"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
class Contact:
    total_contacts = 0
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        Contact.total_contacts += 1


# 2. Add a check_email method to check if the email contains an '@'
def check_email(self):
    if '@' in self.email:
        return True
        print(f"The email does contain an @")
    else:
        return False
        print(f"the email does not contain an @")
# 3. Add a check_phone_number method to check if the phone number contains a '+'
def check_phone_number(self):
        if '+' in self.phone_number:
            return True
            print(f"The phone number does contain a +")
        else:
            return False
            print(f"the phone number does not contain a +")
# 3. Create a class method get_contact_count to retrieve the number of contacts
@classmethod
def get_contact_count(cls):
    return cls.total_contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
contact1 = Contact("John", "0797979797", "john@gmail.com")
contact2 = Contact("Jane", "0787878787", "jane@gmail.com")
# 5. Call your new instance method on one Contact and print the result
print(contact1.check_email())
# 6. Use the class method to print out the total number of contacts