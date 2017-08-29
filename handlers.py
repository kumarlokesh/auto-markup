class Handler(object):

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method): return method(*args)

    def start(self, name):
        return self.callback('start_', name)

    def end(self, name):
        return self.callback('end_', name)

    def sub(self, name):
        return lambda match: self.callback('sub_', name, match) or match.group(0)


class HTMLHandler(Handler):

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>{0}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href="{0}">{1}</a>'.format(match.group(1), match.group(1))

    def sub_email(self, match):
        return '<a href="mailto:{0}">{1}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data)
