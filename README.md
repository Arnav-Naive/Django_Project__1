<div align="center" id="top"> 

  &#xa0;

</div>

<h1 align="center">Chai Tweet — Django Project</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Arnav-Naive/Django_Project__1?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/Arnav-Naive/Django_Project__1?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Arnav-Naive/Django_Project__1?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/Arnav-Naive/Django_Project__1?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#building_construction-architecture">Architecture</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/Arnav-Naive" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Chai Tweet is a full-stack Twitter-inspired web application built with Django. Users can register, log in, create tweets with optional photo uploads, edit and delete their own tweets, and search tweets by text with keyword highlighting — all rendered server-side using Django templates and Bootstrap 5.

## :sparkles: Features ##

:heavy_check_mark: User Registration & Login with Django Auth\
:heavy_check_mark: Create, Edit, Delete Tweets (ownership protected)\
:heavy_check_mark: Optional Photo Upload per Tweet\
:heavy_check_mark: Search Tweets by Text with Green Keyword Highlight\
:heavy_check_mark: Login Required for Protected Actions\
:heavy_check_mark: Responsive UI with Bootstrap 5\
:heavy_check_mark: Secure Secret Key via python-dotenv

## :rocket: Technologies ##

The following tools were used in this project:

- [Python 3](https://www.python.org/)
- [Django 6](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## :building_construction: Architecture ##

```
Django_Project__1/
├── chaiheadq/               # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tweet/                   # Main app
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── tweet_list.html
│   │   ├── tweet_form.html
│   │   ├── tweet_confirm_delete.html
│   │   └── search_results.html
│   ├── templatetags/
│   │   └── custom_filters.py   # Keyword highlight filter
│   ├── models.py            # Tweet model
│   ├── views.py             # CRUD + search views
│   ├── forms.py             # TweetForm, UserRegistrationForm
│   └── urls.py
├── templates/
│   ├── layout.html          # Base template
│   └── registration/        # Login, logout, register
├── .env                     # Secret key (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── manage.py
```

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python 3](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/Arnav-Naive/Django_Project__1

# Access
$ cd Django_Project__1/chaiheadq

# Create virtual environment
$ python -m venv .venv

# Activate (Windows)
$ .venv\Scripts\activate

# Activate (Mac/Linux)
$ source .venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create .env file in root and add:
# SECRET_KEY=your-secret-key
# DEBUG=True

# Run migrations
$ python manage.py migrate

# Start the server
$ python manage.py runserver

# The server will initialize at http://127.0.0.1:8000/tweet/
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

&#xa0;

<a href="#top">Back to top</a>
