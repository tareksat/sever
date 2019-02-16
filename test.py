from Database import Database
from Network.server import start_server

from controller import *


Database.initialize()

load_nodes()

start_server()
