# OpenO1 Private module 

"""
BOT <=> GITHU DL LINKS (api)
"""

then = None

"""
ERROR CODES :

0 : False
1 : True
2 : Product(s) still not available 

"""

def get(type, object:str):
    type_exist(type)  
    if then == False:
        print(f"Type {type} doesn't match with any of written types. (Code 0)")
    if type == "web":    
        return f'https://github.com/OpenO1/frameworks/releases/download/0.2/{object}.css'
    elif type == "python":
        return f'https://github.com/OpenO1/frameworks/releases/download/0.2/{object}.py'

def type_exist(type):
    global then
    if isinstance(type, str) == False:
        then = False

def goto_source(type):
    return f'https://github.com/OpenO1/frameworks/main/{type}'

def list():
    listing = "Available frameworks:\n Section: Web\n - post\n Section: Python\n - openo1-linker"

''' USAGE EXAMPLE
get('web','post')
'''
