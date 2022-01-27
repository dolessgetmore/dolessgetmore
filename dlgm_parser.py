import datetime
try:
    from dateutil.parser import parse
except:
    cmd = """
    error on "from dateutil.parser.parse import parse"
    install module below before use.
    -------------------
    pip install dateutil
    -------------------
    """
    print(f"error on Import {cmd}")

class Date:
    def __init__(self, input_value):
        self.date = parse(input_value).date()
        self.str = self.date.strftime("%Y-%m-%d")

class Parser:

    version = '220127_1426'

    def __init__(self, text = None):
        self.input_type = type(text)
        self.input_value = text

    def date(self, input_value = None):
        if not input_value:
            input_value = self.input_value
        self.date = Date(input_value)
        return self.date

    def int(self, input_value = None):
        if not input_value:
            input_value = self.input_value
        self.date = Date(input_value)
        return self.date


if __name__=="__main__":
    # dt = parse('2022-01-01')
    # print(dt)
    pass