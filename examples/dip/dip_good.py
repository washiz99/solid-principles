from abc import ABCMeta, abstractmethod, abstractproperty

class IDocument(metaclass=ABCMeta):

    @abstractproperty
    def content(self):
        pass

class Document(IDocument):

    def __init__(self, content):
        self._content = content
    
    @property
    def content(self):
        return self._content

class Newspaper(IDocument):

    def __init__(self, content):
        self._content = content
    
    @property
    def content(self):
        return 'News: ' + self._content

class IFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format(self, doc: IDocument):
        pass

class HtmlFormatter(IFormatter):

    def format(self, doc: IDocument):
        return '<h1>' + doc.content + '</h1>'

class XmlFormatter(IFormatter):

    def format(self, doc: IDocument):
        return '<xml>' + doc.content + '</xml>'

class Printer:

    def __init__(self, formatter: IFormatter):
        self.formatter = formatter

    def print(self, doc: IDocument):
        formatted_doc = self.formatter.format(doc)
        print(formatted_doc)



doc = Document('Dependency inversion principle')

# print html
html_formatter = HtmlFormatter()
html_printer = Printer(html_formatter)
html_printer.print(doc)

# print xml
xml_formatter = XmlFormatter()
xml_printer = Printer(xml_formatter)
xml_printer.print(doc)

news = Newspaper('DIP')
xml_printer.print(news)
