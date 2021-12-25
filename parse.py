import datetime
try:
    from dateutil.parser import parse as ps
except:
    cmd = """
    error on "from dateutil.parser.parse import parse"
    install module below before use.
    -------------------
    pip install dateutil
    -------------------
    """
    print(f"error on Import {cmd}")


def parse(text):
    try:
        text = (text)
    except:
        pass
    return text

if __name__=="__main__":
    dt = parse('2022-01-01')
    print(dt)