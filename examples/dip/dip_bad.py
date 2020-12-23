class Document:
    def __init__(self, content):
        self.content = content


class Formatter:
    def format(self, doc: Document):
        return doc.content


class HtmlFormatter:
    def format(self, doc: Document):
        return '<html>' + doc.content + '</html>'


class Printer:
    def print(self, doc: Document):
        formatter = HtmlFormatter()
        formatted_doc = formatter.format(doc)
        print(formatted_doc)


doc = Document('Dependency inversion principle')
printer = Printer()
printer.print(doc)


"""
Printerは、パラメータを、Documentクラスに依存している。
また、フォーマット処理を、HtmlFormatterクラスに依存している。

例えば、Documentクラスではなくて、NewspaperクラスをPrintしたいときはどうするのか？
Htmlフォーマットではなくて、XMLフォーマットで出力したい場合はどうするのか？

DIPを守ることで解決できる。
"""