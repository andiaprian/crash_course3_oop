import requests

#Kalau berhasil
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success!, Response = {response.status_code}')
        #print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil Pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'Whoops, ada kesalahan requests {response.status_code}')
    #print(f'Success!', {response}) --> bisa menggunakan cara ini
except Exception as e:
    print('There is an error', e)
print('Program Ended')
