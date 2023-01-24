import re 

texto = '''
Prosa ...

teste e Teste

Estou acomodado em algum desses brancos bancos, o dia está fresco e a maré, alta, a estrada engarrafada, o brilho do sol muito intenso, esse cheiro da água salgada me lembra o peixe-carapau e eu aqui sem objectivo, só escrevo... devia escrever sobre essas palmeiras, porque elas me lembram os meus cadernos, porque estão cheias de folhas, eu continuo sorrindo sem motivo nenhum, aqui às pessoas também só correm sem motivo nenhum, até o tempo passa sem motivo nenhum, mas eu sinto que vai sempre faltar algo, sempre faltou algo, por isso desapego-me...

Hoje tenho pouco tempo, então um pouco mais rápido escrevi em prosa...

Prosa ...
'''

print(re.findall(r'Prosa | algo', texto))
print(re.findall(r'P.rosa | algo', texto))
print(re.findall(r'[Tt]este', texto))