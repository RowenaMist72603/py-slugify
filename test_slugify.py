from slugify import slugify


def test_basic():
    assert slugify("  Hello, World!  ") == "hello-world"
    assert slugify("Café au lait") == "cafe-au-lait"
