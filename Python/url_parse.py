# import sys module to fetch the command line arguments
import sys
from urllib.parse import urlparse

# function definition to parse url and store in file
def url_parser(param_url,filename):
    
    url_parsed = urlparse(param_url)
    # parse the url using urlparse from the standard Python library
    # you can obtain the following attributes from url_parsed
    # param_url = 'http://www.eller.arizona.edu:2016/index.html'
    # url_parsed.hostname: Hostname = 'www.eller.arizona.edu'
    # url_parsed.port: port number = 2016
    # url_parsed.path: path of the file = '/index.html'
    # check out the full document of the urlparse module at https://docs.python.org/2/library/urlparse.html

    # Write your code here
    # obtain the attributes: host,port and path from the urlparsed
    if url_parsed.port == None:
        port = 80
    else:
        port = url_parsed.port
    filename = '\n' + "url: " + url + '\n' + "host: " + url_parsed.hostname + '\n' + "path: " + url_parsed.path + '\n' + "port: " + str(url_parsed.port)
    
    # Write your code here
    # Open the file (filename from function parameter)
    # write the url, host, port and path to file    
    return filename

# obtain the command line parameters for url and filename
url = sys.argv[1]
file2save = sys.argv[2]

#function call to parse the url and store in file
stored_file = url_parser(url, file2save)

# display the filename which contains the parsed attributes of the url
print("The parsed attributes are stored in: %s" %stored_file)
file = open(file2save, "a")
file.write(url_parser(url, file2save))
