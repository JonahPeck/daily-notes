import hashlib
import os
import click
from dotenv import load_dotenv

load_dotenv() #placed in this folder so any script can have access once a username is used

def get_username():
    """Prompt the user for their name and return it."""
    username = click.prompt("Welcome! What's your name?", type=str)
    click.echo(f"Welcome, {username}!")
    return username.lower()


# def hash_username(username, salt=None):

#     if salt is None:
#         salt = os.urandom(16)

#     username_salt = salt + username.encode('utf-8')

#     sha256_hash = hashlib.sha256()

#     sha256_hash.update(username_salt)

#     hashed_username = sha256_hash.hexdigest()

#     return hashed_username, salt

# username = input("What is your name?: ")

# hashed_username, salt = hash_username(username)
# salt_hex = salt.hex()

# print(f"Original username: {username}")
# print(f"Salt:  {salt_hex}")
# print(f"hashed username: {hashed_username}")
