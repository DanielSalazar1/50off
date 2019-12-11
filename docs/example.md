As a user, I can anonymously browse all the deals on the site which are minimum 50% off.

```bash
winpty http http://127.0.0.1:8000/api/categories

winpty http http://127.0.0.1:8000/api/items 


winpty http --form POST http://127.0.0.1:8000/api/register   first_name="Daniel"   last_name="Cardenas"   email=daniel@daniel.com   username="daniel123"   password=daniel123

winpty http --form POST http://127.0.0.1:8000/api/login username=daniel1234   password=daniel1234

winpty http http://127.0.0.1:8000/api/favourites 'Authorization: Token 56f90412196ea8e8866779829b2f3af791f94979'

MY_PASSWORD: 56f90412196ea8e8866779829b2f3af791f94979


openssl base64 -in export.xml > export.xml.base64

winpty http --form POST http://127.0.0.1:8000/api/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
python manage.py extract_data_from_xml

winpty http http://127.0.0.1:8000/api/list 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

winpty http http://127.0.0.1:8000/api/list/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
```
