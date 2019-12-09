# /bin/python3

import os, sys

if os.system('pip freeze | grep requests') == 256:
    os.system('pip install --upgrade pip')
    os.system('pip install requests')



def require_link_download(username, repositorio, file_add):
    import requests
    response = requests.get(f'http://api.github.com/repos/{username}/{repositorio}/contents/{file_add}')
    response = response.json()
    return response['download_url'], response['name']

def download_arq(name, link):
    import requests
    arq = open(f"./{name}", 'w')
    response_download = requests.get(link)
    arq.write(response_download.text)
    arq.close()

if sys.argv[1] == '--help':
    print(""" 
V [username] [repository] [file address] - download archieve for github
    """)
elif sys.argv[1] == 'V':
    link_to_download, name = require_link_download(username=sys.argv[2],
                          repositorio=sys.argv[3],
                          file_add=sys.argv[4])
    download_arq(name=name, link=link_to_download)
    


