import re

string = 'Este é um teste de expressões teste regulares.'

print(string)
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ACDB' , string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ADC', string))