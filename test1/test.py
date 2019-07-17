import urllib.request
import re
with urllib.request.urlopen('https://profs.info.uaic.ro/~gdt/') as response:
    html = str(response.read(),encoding='utf-8')

match = re.search(r'href=[\'"]?([^\'" >]+)', html)
if match:
    print(match.group(0))