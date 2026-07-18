from prompt_toolkit.contrib.telnet import protocol

url = input("enter the URL : ")
print(url)

protocol = url.split("://")[0]
print(protocol)

domain = url.split("://")[1]
domain = domain.split('.')[1]
print(domain)

page = url.rpartition("/")[1] + url.rpartition("/")[2]
print(page)