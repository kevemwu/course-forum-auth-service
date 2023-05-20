from datetime import datetime

from utils import token, crawler, config

ADMIN_USERNAME = config.get_admin_username()
ADMIN_PAASWORD = config.get_admin_password()
EXP_TIME = 30

def login(username, password):
    http_code = 200
    data = {}
    identify = "user"

    # admin login
    if username == ADMIN_USERNAME and password == ADMIN_PAASWORD:
        department = 'admin'
        identify = 'admin'
    else:
        http_code, department = crawler.login(username, password)

    # login successful
    if http_code == 200:
        exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=EXP_TIME)
        jwt = token.encode_jwt(department, identify, exp)
        data = {
            'identify': identify,
            'token': jwt,
            'exp': exp,
            'department': department
        }

    return http_code, data