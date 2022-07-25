#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host, port))

while True:
    c, addr = s.accept()
    print("Got a connection request connected successfully")
    c.send("Thanks for connecting")
c.close()
