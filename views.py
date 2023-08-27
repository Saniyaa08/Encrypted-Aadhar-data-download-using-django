from django.shortcuts import render
from django.http import HttpResponse
import csv
from cryptography.fernet import Fernet
from .models import Person


#def download_persons_csv(request):
    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="mymodel_data.csv"'

    #writer = csv.writer(response)
    #writer.writerow(['f_name','l_name', 'aadhar_number', 'dob', 'gender', 'address'])

    #mymodel_data = Person.objects.all().values_list('f_name','l_name', 'aadhar_number', 'dob', 'gender', 'address')

    #for data in mymodel_data:
        #writer.writerow(data)

    #return response
    
    #persons = Person.objects.all()

    
    #buffer = io.BytesIO()

   
    #writer = csv.writer(buffer)

    
    #writer.writerow(['First Name','Last NAME', 'Encrypted Name', 'Encrypted Aadhar', 'DOB', 'Gender', 'Address', 'Key'])

    
    #key = Fernet.generate_key()
    #cipher_suite = Fernet(key)

    #for person in persons:
        # Encrypt the name and Aadhar number fields
        #encrypted_f_name = cipher_suite.encrypt(person.f_name.encode())
        #encrypted_l_name = cipher_suite.encrypt(person.l_name.encode())
        #encrypted_aadhar = cipher_suite.encrypt(person.aadhar_number.encode())

        # Write the encrypted data to the CSV file
        #writer.writerow([person.f_name,person.l_name, encrypted_f_name, encrypted_f_name,encrypted_aadhar, person.dob, person.gender, person.address, key])

    #response = HttpResponse(buffer.getvalue(), content_type='text/csv')

    #response['Content-Disposition'] = 'attachment;filename=persons.csv'

    #return response
    #return HttpResponse("return this string")
from django.http import HttpResponse
import csv
from cryptography.fernet import Fernet
from .models import Person

def download_persons_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'

    writer = csv.writer(response)
    writer.writerow(['first name','last name', 'aadhar number', 'dob', 'gender', 'address'])

    persons = Person.objects.all()

    # Initialize key and cipher suite
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    for person in persons:
        f_name_enc = cipher_suite.encrypt(person.f_name.encode()).decode()
        l_name_enc = cipher_suite.encrypt(person.l_name.encode()).decode()
        aadhar_number_enc = cipher_suite.encrypt(person.aadhar_number.encode()).decode()
        writer.writerow([f_name_enc, l_name_enc, aadhar_number_enc, person.dob, person.gender, person.address])

    return response
