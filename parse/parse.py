# import datetime
try:
    from dateutil.parser import parse as ps
except:
    cmd = "from dateutil.parser.parse import parse"
    print(f"error on Import {cmd}")


def parse(text):
    try:
        text = (text)
    except:
        pass
    return text
