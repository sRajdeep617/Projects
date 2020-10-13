import pyshorteners

url = input('Enter URL: ')

print('URL after shortening :- ', pyshorteners.Shortener().tinyurl.short(url))
