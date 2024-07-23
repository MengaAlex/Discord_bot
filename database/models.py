from tortoise.models import Model
from tortoise.fields import IntField, TextField, DateField, BigIntField

class Endpoints(Model):
    id = IntField(pk=True)
    word = TextField()

    def __str__(self):
        return self.word
    

class Students(Model):
    id = IntField(pk=True)
    firstname = TextField()
    lastname = TextField()
    gender = TextField()
    email = TextField()
    groupp = TextField()
    dateofbirth = DateField()

    class Model():
       dateofbirth = "Дата рождения" 
    
    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.gender}, {self.email}, {self.dateofbirth}"
    
class Feedback(Model):
    id = IntField(pk=True)
    user_id = BigIntField()
    name = TextField()
    email = TextField()
    qestion = TextField()

    def __str__(self):
        return self.qestion