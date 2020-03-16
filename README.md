# koalitie
Portfolio website (koalitie.com)

# Setup instruction

Backend

1. Clone Project
2. Run `pip install -r requirements.txt` command
3. Run `python manage.py migrate` command
4. Create superuser using  `python manage.py createsuperuser` command
5. Run the server `python manage.py runserver`

Frontend

1. Go to `frontend/static/assets` directory
2. Run `npm install`


# Setup pages in admin

1. after creating superuser, got to `localhost:8000/admin` and login
2. create a page for works, blogs, tutorial, about, and contacts. The pages should be a child of the home page. 
3. On creating the pages, you are asked to choose the type of page. Choose the page type with `index` name on it . Ex. `works index page`, `blogs index page`, etc. 


