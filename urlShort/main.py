import pyshorteners


def shortnen(url):
    s = pyshorteners.Shortener()
    return (s.tinyurl.short(url))
