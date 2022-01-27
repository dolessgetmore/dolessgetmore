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

class Parser:
    def __init__(self, text):
        self.input_type = type(text)
        self.input_value = text

    def money_value(self, number):
        pass

    def to_datetime(self):
        return parse(self.input_value)

    def parse(self, text):
        try:
            text = (text)
        except:
            pass
        return text

if __name__=="__main__":
    # dt = parse('2022-01-01')
    # print(dt)
    pass