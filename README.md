#Flask Project GetAGrip's Website#

##Dependencies##
You may `sudo pip install` all of these:  
stripe  
flask==0.9  
sqlalchemy==0.7.9  
flask-sqlalchemy==0.16  
sql-alchemy-migrate  
flask-whooshalchemy==0.54a  
flask-wtf  
pytz==2013b  
flask-babel==0.8  
flup  

##Database Scripts

All database models are in the models.py file contained in the app directory. If you edit that file and need to migrate the database, there is a script in the root directory that you can run to do so. Just enter `python db_migrate.py` and it will upgrade the version. There are other scripts like db_downgrade that are self explanatory.

##Stripe
I was using the stripe API to process the payments. I didn't have any of the payment information entered in but go to https://stripe.com to create an account and look at the docs. They're very straightforward and they have flask specific docs at https://stripe.com/docs/checkout/guides/flask