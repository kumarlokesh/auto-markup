import sys, re
from util import *

print('<html><head><title>...</title></head><body>')

title_created = False
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if not title_created:
        print('<h1>')
        print(block)
        print('</h1>')
        title_created = True
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')
