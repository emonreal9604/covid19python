import pyshorteners
while True:
    enterlink=input("Enter the link\n")
    shortener=pyshorteners.Shortener()
    url=shortener.tinyurl.short(enterlink)
    print(url)
OR
print('URL after shortening --> ', pyshorteners.Shortener().tinyurl.short(url))