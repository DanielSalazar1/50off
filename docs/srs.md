50 Off - Software Requirements Specification (SRS)
A webapp which allows users to check biggest deals by looking through a list of items which are at minimum 50% off.
User Cases:
(1) When a brand new user visit the site for the very first time, ask the user to enter their country, province and city.
- Page with ability to enter the current location
- Once you save, this is stored in the "localStorage" in the browser (JS). Look into "Token Authentication" code that we've done before and you'll see how to **"SetItem"** and **_"GetItem"_** from "localStorage".
- country
- province
- city
(2) As a user, I can anonymously browse all the deals on the site which are minimum 50% off.
- Two tables: (1) Categories Table, (2) Items Table
- List view on website
- If I click any category, then refresh the table with the latest items.
- If I click on an Item, then load up a description page (details page).
- Somewhere on the GUI, I need to be able to sort by location
- Filter by percent off

- Code:
    - URL: /api/categories
    - METHOD: GET
    - FIELDS:
        - name
    - This will be the list of all the categories in our app
    - URL: /api/items
    - METHOD: GET
    - FIELDS:
         - name
         - original price
         - discounted price
         - percent off
         - company name
         - address
         - is_online
     - FILTERS:
         - percent off
         - discount price
         - (OPTIONAL) company_name
         - is_online
         - country
         - province
         - city
         - category
(3) Regiter
- Look into "Token Authentication" code that we've done before
- Code:
    URL: /api/register
    METHOD: POST
    FIELDS:
        - first name
        - last name
        - userrname
        - email
        - passwordd
(4) Login
- Look into "Token Authentication" code that we've done before
- Code:
    URL: /api/login
    METHOD: POST
    FIELDS:
        - username
        - password
(5) When logged in, user has ability to "Add item to favourites list".
- Code:
    URL: /api/favourites
    METHOD: POST
    Create the item into the authenticated user's favourites list
(6) When logged in, I can see my favourites list
- Code:
    URL: /api/favourites
    METHOD: GET
    Show the list of favourited items for the authenticated user
(7) (OPTIONAL) If an item is in my favourites list, I will receive emails of new offers if there exist in the future.
(8) (DONE) As an Admin, I want to add Items and Categories
- Connect these models to the Django Admin
- Create a super user so as an Admin, I can log into Django Admin and operate the app
