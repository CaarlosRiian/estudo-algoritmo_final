import re 
from pprint import pprint

regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}\.\d{2})$",
    flags=re.MULTILINE
)

test_str = '''
    (697.543.426-44
    )

'''

pprint(regex.findall(test_str))