
from .apiuser import UsersList

def initialize_routes(api):
    api.add_resource(UsersList, '/users')
