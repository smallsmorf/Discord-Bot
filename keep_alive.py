from flask import Flask
from threading import Thread
import random


app = Flask('')

@app.route('/')
def main():
	return 'Im in!'

def run():
  app.run(
		host='0.0.0.0',
		port=8080
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()