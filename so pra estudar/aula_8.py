import re 
from pprint import pprint

texto = '''
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.1 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
'''

# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+\)\s+\w+\s+(?=active)', texto)) ((Não Deu certo isso ;-;))

pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Aula Não foi tão produtiva pra mim.
