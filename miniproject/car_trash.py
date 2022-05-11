from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('52.78.119.224', 27017, username="sparta", password="test")
db = client.dbsparta


import requests


app = Flask(__name__)
