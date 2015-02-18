__author__ = 'ibrahim'
# import anydbm
# anydbm._defaultmod = __import__('dumbdbm')
import click
import stripe
import local_settings as settings
import shelve

from passlib.hash import sha256_crypt

USERNAME = None
PASSWORD = None
stripe.api_key = settings.APIKEY

@click.command()
def login():
    email = click.prompt('Email', type=str)
    password = click.prompt('Password', hide_input=True)

@click.command()
def signup():
    email = click.prompt('Email', type=str)
    password = click.prompt('Password', hide_input=True)
    c = stripe.Customer.create(email=email)
    db = shelve.open("data")
    db[str(email)] = {"password": sha256_crypt.encrypt(password), "id": c.id}
    db.close()
    click.echo("Account Created Successfully!")
    command()

@click.command()
@click.option('--yene', prompt="fayborom shell $#")
def command(yene):
    COMMAND_DICT = {'login': login, 'signup': signup}
    COMMAND_DICT[yene]()


def start():
    click.echo("""*****************************************
Dalal ak jamm ci fay borom
Bindal sa yene walla \'diapale\':
******************************************\n""")
    command()


if __name__=="__main__":
    start()