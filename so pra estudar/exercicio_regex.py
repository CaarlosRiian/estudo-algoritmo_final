import re


texto = ''' Encontre o texto dentro da tag h1 abaixa:

<html>
<head><title>Exercícios</title></head>
<body>
<h1>Exercícios</h1>
<table>
<thead>
<th>#</th>
<th>Questão</th>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Primeiro exercício de regex</td>
</tr>
</tbody>
</table>
</html>


Encontrei os endereços de e-mail da seguinte frase
'purple alice@google.com, blah monkey bob@abc.com blah dishwasher, aluisio@ifrn.edu.br
'''
# texto = input('Informe o texto: ')

print(re.findall(r'<[h1]{1,2}>.*<\/[h1]{1,2}>', texto))