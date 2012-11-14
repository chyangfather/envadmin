from mongoengine import *
from ea.settings import DBNAME

connect(DBNAME)

class Employee(Document):
    name = StringField(max_length=50)
    age = IntField(required=False)
