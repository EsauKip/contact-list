class Contact:
    """class that generates instances of a contact
    """
    contact_list=[]
    def __init__(self,first_name,last_name,number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email