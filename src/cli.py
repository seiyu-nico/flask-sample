from flask import Flask
from commands import commands

app = Flask(__name__)

app.cli.add_command(commands)
