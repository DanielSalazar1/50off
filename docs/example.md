--------------------------------------------------  DONE -----------------------------------------------------------

# As an Admin, I want to add Items and Categories

## Step 1:
    winpty python manage.py createsuperuser
## Step 2:
    django-admin
    username = daniel
    password = daniel1234
    email = daniel@daniel.com
    name = daniel
    last name = cardenas
## Step 3:
    Create new categories and add items inside django-admin.

# As an user, I can anonymously browse all the deals on the site which are minimum 50% off.

## Step 1:

    Enter to the main page (no extra url needed, just the page link) and browse throughout the website.

#As an user, I want to deploy the categories list and select the one I want.

## Step 1:
    winpty http http://127.0.0.1:8000/api/categories


## Step 2:
    winpty http http://127.0.0.1:8000/api/items

    winpty http http://127.0.0.1:8000/api/images


# Regiter - As an user, I want to register in the website in order to have a profile where to add my favourite items and buy them.

## Step 1:
    winpty http --form POST http://127.0.0.1:8000/api/register   first_name="Daniel"   last_name="Cardenas"   email=a@a.com   username="danielcardenas1"   password=daniel12345

# Login - As an user, I want to register in the website to be able to do a purchase.
  (MY PASSWORD is the token given from "token authentication" for unique profile items)

## Step 1:
    winpty http --form POST http://127.0.0.1:8000/api/login username=danielcardenas1   password=daniel12345

## Step 2:

    winpty http http://127.0.0.1:8000/api/favourites 'Authorization: "token": "07410e0f55f9d45b08c878a9b5d4d339defd8100"



    MY_PASSWORD: "07410e0f55f9d45b08c878a9b5d4d339defd8100"



-------------------------------------------------- TO DO -----------------------------------------------------------

# Set location - When a brand new user visit the site for the very first time, ask the user to enter their country, province and city.

# Step 1:
    Open the website in the main page (no url needed) and set location in the emergent chart.

    - Once you save, this is stored in the "localStorage" in the browser (JS).


# As an user, I can anonymously browse all the deals on the site which are minimum 50% off.

- Two tables: (1) Categories Table, (2) Items Table
- List view on website
- If I click any category, then refresh the table with the latest items.
- If I click on an Item, then load up a description page (details page).
- Somewhere on the GUI, I need to be able to sort by location
- Filter by percent off

























<!--
openssl base64 -in export.xml > export.xml.base64

winpty http --form POST http://127.0.0.1:8000/api/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
python manage.py extract_data_from_xml

winpty http http://127.0.0.1:8000/api/list 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

winpty http http://127.0.0.1:8000/api/list/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
``` -->
