#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

s = socket.socket()
host = socket.gethostname()
s.connect((host, 8000))

print(s.recv(1048))
s.close()
