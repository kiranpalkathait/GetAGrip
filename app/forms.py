from flask.ext.wtf import Form, TextField, BooleanField, IntegerField
from flask.ext.wtf import Required, Email

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class ContactForm(Form):
    name = TextField('name', validators = [Required(message="*Sorry, the name field is required. ")])
    email = TextField('email', validators = [Required(message="*Sorry, the email field is required"), Email(message="Sorry, the email you entered is not valid. ")])
    body = TextField('body', validators = [Required(message="*Sorry, the body field is required")])

class ProductForm(Form):
    name = TextField('name', validators = [Required()])
    stock = IntegerField('stock', validators=[Required()])
    image = TextField('image', validators=[Required()])
    price = IntegerField('price', validators=[Required()])
