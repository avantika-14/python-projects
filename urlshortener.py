import pyshorteners
link=input("enter any link:\t")
short=pyshorteners.Shortener()
tiny=short.tinyurl.short(link)
print(tiny)