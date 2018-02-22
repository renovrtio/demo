from urllib.request import urlopen, Request
import urllib
import http

filename = 'urllib.txt'
# r = urlopen('http://www.runoob.com/manual/pythontutorial3/docs/html/stdlib.html#tut-internet-access')
# print(r, type(r))
# for line in r:
#     line = line.decode('utf-8')
#     # print(line, type(line))
#     with open('urllib2_test01.html', 'a', encoding='utf-8') as f_obj:
#     # with open('urllib2_test01.html', 'a') as f_obj:        
#         f_obj.write(line)

##############################################################################################################

url = 'http://www.runoob.com/manual/pythontutorial3/docs/html/stdlib.html#tut-internet-access'
req = Request('http://127.0.0.1:8000')
response_1 = urlopen(req)
# print(response_1.status)
# print(response_1.getheaders(), '\n')
print(response_1.getheader('Server'))
the_page = response_1.read()
# print(response_1.getcode(), '\n')
# print(response_1.info(), '\n')
# print(response_1.geturl(), '\n')
# print(type(the_page), '\n')
with open(filename, 'wb') as f_obj:
    f_obj.write(the_page)

###################################################################################################

# data = {}
# data['name'] = 'WHY'
# data['location'] = 'SDU'
# data['language'] = 'Python'

# url_values = urllib.parse.urlencode(data)
# print(url_values)

# # name=Somebody+Here&language=Python&location=Northampton
# url = 'http://www.example.com/example.cgi'
# full_url = url + '?' + url_values
# data = urlopen(full_url)

