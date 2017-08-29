import re

from util import *
from rulebook import *


class Parser(object):

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')


class TextParser(Parser):

    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.initRules()
        self.initFilters()

    def initRules(self):
        for rule in [ListRule, ListItemRule, TitleRule, HeadingRule,\
                     ParagraphRule]:
            self.addRule(rule())

    def initFilters(self):
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'email')
