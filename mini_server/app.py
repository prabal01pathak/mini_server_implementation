#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, Request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return {"message": "Hello world!"}
