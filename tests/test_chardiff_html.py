from chardiff_html import __version__, chardiff_html


def test_version():
    assert __version__ == "0.1.0"


def test_chardiff_html():
    res = chardiff_html("hoge", "haga")
    assumed = (
        "h"
        '<span style="color: red; background-color: mistyrose">'
        "o"
        "</span>"
        '<span style="color: green; background-color: #e0ffe5">'
        "a"
        "</span>"
        "g"
        '<span style="color: red; background-color: mistyrose">'
        "e"
        "</span>"
        '<span style="color: green; background-color: #e0ffe5">'
        "a"
        "</span>"
    )
    assert res == assumed
