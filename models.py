from django.db import models
import hashlib
from cryptography.fernet import Fernet


# Create your models here.
class Person(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    aadhar_number=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def as_csv(self):
        # Generate a key for encryption
        key = Fernet.generate_key()

        # Initialize a Fernet encryption object with the key
        f = Fernet(key)

        # Encrypt the Aadhar number, name
        encrypted_aadhar = f.encrypt(self.aadhar_number.encode())
        encrypted_f_name = f.encrypt(self.f_name.encode())
        encrypted_l_name = f.encrypt(self.l_name.encode())
       
        # Return the fields as a CSV string with the key appended
        return f"{encrypted_f_name.decode()},{encrypted_l_name.decode()},{encrypted_aadhar.decode()},{self.dob},{self.gender},{self.address},{key.decode()}"


    def __str__(self):
        return f"{self.f_name} {self.l_name}"