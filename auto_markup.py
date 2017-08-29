import sys
from handlers import *
from parsers import *


handler = HTMLHandler()
parser = TextParser(handler)

parser.parse(sys.stdin)
