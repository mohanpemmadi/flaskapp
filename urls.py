# from services import Home, HelloWorld, MyName, MyAge

import services
# from services import *

def all_urls(api):
    api.add_resource(services.HelloWorld, '/welcome') # http://127.0.0.1:5000/welcome
    api.add_resource(services.Home, '/home') # http://127.0.0.1:5000/home
    api.add_resource(services.MyName, '/myname/<string:name>') #  http://127.0.0.1:5000/myname/mohan
    api.add_resource(services.MyAge, '/myage/<int:age>')
    api.add_resource(services.ListAllData,'/list_all_data')