import base64
import random
import re
import time

import requests

url = 'http://api.cd1a.cn/index.php/driven10/Scan/scan'

header = {
    "Content-Type": "application/json"
}


def query(chargerId):
    print(f"Querying...{chargerId}")
    end_of_userid_locked = [chr(random.randint(0, 23) + ord('A')) for i in range(3)]
    end_of_userid_locked = ''.join(i for i in end_of_userid_locked)
    userid_locked = "pnCVObhgEn2eOl" + end_of_userid_locked
    userid_locked = base64.b64encode(s=userid_locked.encode('utf8'))
    data = '{"str":"' + chargerId + '}","userid_locked":"' + userid_locked.decode(
        'utf8') + '","version":"4.0.0","platform":"applet"}'
    response = requests.post(url=url, data=data, headers=header)
    print(str(chargerId) + ":" + str(response.json()))
    msg = response.json()['msg']
    if re.search(r'端口被占用', msg) is not None:
        hours = re.findall(r'[0-9]*', msg)
        while '' in hours:
            hours.remove('')
        if len(hours) == 1:
            hours = ['0'] + hours
        return {'status': 1, 'msg': msg, 'time': hours}
    else:
        return {'status': 0, 'msg': msg, 'time': ['0', '0']}


if __name__ == "__main__":
    for id in range(100, 134):
        print(str(id) + " : " + str(query('02342' + str(id))))
