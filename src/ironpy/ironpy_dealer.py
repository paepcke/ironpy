#!/usr/bin/env python
'''
Created on Jul 7, 2017

@author: paepcke
'''
import SimpleHTTPServer
import SocketServer
import os
import random


PORT = 8000

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    @classmethod
    def load_packages(cls):
        curr_dir = os.path.dirname(__file__)
        packages_path = os.path.join(curr_dir,'packages.txt')
        with open(packages_path, 'r') as fd:
            CustomHandler.packages = fd.readlines()
                
    def do_GET(self):
        #Sample values in self for URL: http://localhost:8080/jsxmlrpc-0.3/
        #self.path  '/jsxmlrpc-0.3/'
        #self.raw_requestline   'GET /jsxmlrpc-0.3/ HTTP/1.1rn'
        #self.client_address    ('127.0.0.1', 3727)
        if self.path=='/deal':
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(self.deal()) #call sample function here
            return
        else:
            #serve files, and directory listings by following self.path from
            #current working directory
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def deal(self):
        indx = random.randint(0,603)
        return(CustomHandler.packages[indx])


httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),CustomHandler)
CustomHandler.load_packages()

print "serving at port", PORT
httpd.serve_forever()
