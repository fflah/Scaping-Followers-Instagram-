# Scaping-Followers-Instagram

## Nomenklatur Dataset ##
Atribut       | Penjelasan
------------- | -------------
username         | username ig follower

## Setup run.py ##

- Buat virtual environment -> python -m venv env
- Activate environment -> source env/bin/activate (linux dan mac)
- Install requirement.txt ->  pip install -r requirements.txt
- Untuk mendapatkan cookie.json, silakan baca https://fajrulfalah18.medium.com/melewati-sistem-auth-website-di-selenium-emang-bisa-8d88a8a177e8
- Masukan cookie.json pada variabble COOKIE_PATH
- Masukan url profile yang akan di-scraping data follower nya pada variable URL_PROFILE
- Jalankan -> python run.py