from hello import hello

def test_argument():
    assert hello('Shuvkant')=='Hello, Shuvkant'

def test_default():
    for name in ["Shuvkant", "Ramesh", "Hari"]:
                 hello(name)==f"Hello, {name}"
