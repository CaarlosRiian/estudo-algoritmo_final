import re 

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div>
'''

# cpf = 'a 123.456.789-10 a'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 \3 \4', texto))


'''tags = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\>', texto)
print(tags) ''' 





print('Bixo não entendi quase nada dessa aula ;-; KKKKKK')