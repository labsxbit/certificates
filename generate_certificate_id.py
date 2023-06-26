import random
import string

def generate_certificate_id(length):
    characters = string.ascii_uppercase + string.digits
    certificate_id = ''.join(random.choice(characters) for _ in range(length))
    return certificate_id

# Example usage: generate a certificate ID with a length of 10 characters
name = input('Enter the name of the candidate : ')
date = input('Enter the data of the completion in DDMMYYYY format : ')

first_two_chars = name[:2]

certificate_id = generate_certificate_id(10)

cert_id = certificate_id + date + first_two_chars
print(cert_id)

