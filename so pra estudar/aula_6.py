import re 

cpf = '123.456.789-10'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9-a-zA-Z.-]+', cpf))


