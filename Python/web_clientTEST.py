# import necessary modules
import sys
from urllib.parse import urlparse
from socket import *

# obtain the two parameters from commend line
#param_url = "http://www.u.arizona.edu/~weichen/MIS543/test.html"
param_url = sys.argv[1]
param_file = sys.argv[2]

# parse the url 
url_parsed = urlparse(param_url)

# you can obtain the following attributes from url_parsed
#param_url = 'http://www.eller.arizona.edu:2016/index.html'
# url_parsed.hostname: Hostname = 'www.eller.arizona.edu'
# url_parsed.port: port number = 2016
# url_parsed.path: path of the file = '/index.html'

s = socket(AF_INET, SOCK_STREAM)

if url_parsed.port == None:
    port = 80
else:
    port = url_parsed.port

##### your code goes here ... #####

# 1. Construct the address and port number
s.connect((url_parsed.hostname, port))

# 2. Construct the http GET request (with Host and Connection headers)
req_str = "GET " + url_parsed.path + " HTTP/1.0\r\n\r\n"
s.send(req_str.encode())

# 3. Connect to the server, and read the response
data = s.recv(4096, MSG_WAITALL)
#print(data)

# 4. Save the body of the HTTP response to param_file (skip the header)
header, body = data.split(b"\r\n\r\n")
headerdecode = header.decode()
headercheck = headerdecode.split("\r\n")
if headercheck[0] == "HTTP/1.1 200 OK":
    file= open(param_file, "wb")
    file.write(body)
    file.close()
    
else:
   # 5. If the HTTP response is anything rather than 200 OK, write the response header to param_file
   file = open(param_file, "w")
   file.write(headercheck[0])
   file.close
   
# 6. Close the connection and the file
s.close

print("\nFinishing downloading ...")