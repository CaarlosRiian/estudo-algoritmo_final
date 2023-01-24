import re 

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div>
'''
print(re.findall(r'<[pdiv]{1,3}>', texto))

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto)) # Mostra o que ta dentro da variavel texto com as tags html
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto)) # Mostra o que ta dentro da variavel texto com as tags html menos a ultima, pelo fato de não ter nada dentro.