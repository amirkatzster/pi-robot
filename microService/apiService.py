import logging
import pika
import sys
from services.queue import queue
import os, shutil
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class actionService(Resource):

    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'actionService'

    
    def get(self, command):
            print(command)
            self.queue = queue()
            channel = self.queue.createChannel()
            channel.basic_publish(self.EXCHANGE_NAME,self.QUEUE_NAME,command)

class sayService(Resource):

    EXCHANGE_NAME = ''
    QUEUE_NAME = 'HebTextToSpeachService'

    def get(self, text):
        print(text)
        self.queue = queue()
        channel = self.queue.createChannel()
        channel.basic_publish(self.EXCHANGE_NAME,self.QUEUE_NAME,text)

    

api.add_resource(actionService, '/action/<string:command>')
api.add_resource(sayService, '/say/<string:text>')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)



