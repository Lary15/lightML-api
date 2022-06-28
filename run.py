from api.endpoints import Peripherals
from flask import Flask
from flask_restful import Api
from tinydb import TinyDB
from repository.tiny_db import TinyDBRepository

#Setup Repository
db = TinyDB("db.json")
repo = TinyDBRepository(db)

# Setup API
app = Flask(__name__)
api = Api(app)

api.add_resource(Peripherals, "/peripherals", resource_class_kwargs={'repo': repo})

if __name__ == '__main__':
  app.run()