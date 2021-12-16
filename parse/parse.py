try:
    from dateutil.parser.parse import parse
except:
    cmd = "from dateutil.parser.parse import parse"
    print(f"error on Import {cmd}")


def parse(text):
    return text
