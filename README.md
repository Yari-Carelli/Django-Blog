# Django Blog
A simple, fully-functional blog built with Django and Bootstrap4.

#

<img width="700" src="">

#

The live link for the project can be found [HERE]()

#

## Table of Contents
+ [UX](#ux "UX")
  + [Project Purpose](#project-purpose "Project Purpose")
  + [Overview](#overview "Overview")
  + [Communication](#communication "Communication")
  + [Site Goals](#site-goals "Site Goals")
  + [Current User Goals](#current-user-goals "Current User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
+ [User Stories](#user-stories "User Stories")
  + [Admin Stories](#admin-stories "Admin stories")
  + [User Stories](#user-stories "User stories")
+ [Design](#design "Design")
  + [Wireframes](#wireframes "Wireframes")
  + [Typography](#typography "Typography")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
+ [Testing](#testing "Testing")
  + [Manual Testing](#manual-testing "Manual Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")

#

## UX

### Project Purpose:
The purpose of the project is to get a general idea about the working of Django by learning how to build a blog with all the common functionalities such as registering, posting, commenting, and showing a view count.
Building a blog is an excellent first step to get a good grasp over this open-source web framework, written in Python, that follows the model-view-template architectural pattern.

### Learning Outcomes:
1. Create a database-backed Django project and deploy it to Heroku
2. Host uploaded images on a cloud provider
3. Create class-based views in a Django project
4. Use built-in Django generic views
5. Add an authentication back-end
6. Create custom database models
7. Add extra interactivity with Javascript

### Overview
This Blog application built with Django allows users to create, edit and delete posts, and leave comments on a post.

A blog is a web page that is update on a regular basis. Within a blog, registered users share long-form articles that cover topics the target audience may want to read or learn about. It can also include hyperlinks to internal or external web pages to enhance users' experience. Adding images or videos can also make reading your blog a more engaging experience.

- Pages included
  - Homepage, with a hero image, intro section, featured and latest posts sections, and a parallax divider section
  - Category listing with a widgets column
  - Blog page, with a list of all the blog posts, each paginated on a different page
  - Post page, displaying the post's content 

### Communication:
With a clean, easy to follow layout, the users are guided through the features of the website with an ease of navigation.

### Site Goals:
The main goal of a blog is to attract future readers and keep them interested, and to keep current users satisfied and engaged. Coming up with fresh topics can encourage people to keep coming back to the website to read your blog, and register to share their own content and leave comments on posts to be involved in the conversation.

### Current User Goals
Site users purpose is to read about topics they are interested in, and share their views on an individual subject either by posting new content or commenting on existing posts.

### New User Goals
To become instantly engaged with the design of the site, and feel intrigued to explore all it has to offer.

#

## User Stories

### Admin Stories:
#### As the Site Admin:
1. I can add, edit and delete posts so that I can manage the blog content.
2. I can add, edit and delete authors so that I can select which site users can create posts.
3. I can add, edit and delete categories so that I can manage the topics discussed in the blog.

### User Stories:
#### As a Site User:
1. I can register an account so that I can create posts and submit comments.
2. I can view featured and latest posts so that I can recognize what content is either important or has been recently added to the website.
3. I can view a list of all the posts so that I can select which post to open.
4. I can click on a post so that I can read its content.
5. I can edit my posts' details so that I can make corrections or update my posts after they were created.
6. I can delete my posts so that I can remove posts from the website after they were created.
7. As a Site User I can leave comments on a post so that be involved in the conversation.
8. As the Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.
9. I can use the search bar to quickly fetch the posts I am interested in.

#

## Design

The blog's design is minimalistic, and almost all elements are in black and white. It contains 3 HTML page templates, all of them in 7 color variants (pink, red, blue, green, blue, violet, sea blue.). The default color variant is grey.

### Wireframes:

##### Homepage

<img width="700" src="">

##### Blog Page

<img width="700" src="">

##### Post Page

<img width="700" src="">

##### Site Navigation:

<img width="700" src="">

### Database Schema

<img width="700" src="">


### Typography:
The font used for the website is the "Open Sans", sans-serif, and was obtained from the Google Fonts library.

#

## Features

### Existing Features

#### Homepage

<img width="700" src="">

#### Navigation Bar

<img width="700" src="">

##### Blog Page

<img width="700" src="">

##### Post Page

<img width="700" src="">

#### Newsletter

<img width="700" src="">

#### Sidebar Widgets

<img width="700" src="">

#### Search Bar

<img width="700" src="">

#### Footer

<img width="700" src="">

#### Register Page

<img width="700" src="">

#### Sign In Page

<img width="700" src="">

##### Sign Out Page

<img width="700" src="">

##### Create Post Form

<img width="700" src="">

##### Update Post Form

<img width="700" sr="">

##### Delete Post Page

<img width="700" src="">

##### Comments Section

<img width="700" src="">

### Features Left to Implement

#

## Testing

### Manual Testing

- CRUD functionality has been tested for each of the Posts.
 - Comments may only be created.
- All navlinks direct to the correct page.
- Buttons to allow users to edit/delete posts only appear on posts that they have created.
- Users are able to register a new account.
- Users with an existing account are able to sign in.
- Each user has the ability to sign out.
- Site tested using different browsers: opens in Brave, Chrome and Safari without issues.
- All social links open to external pages as intended.

### Validator Testing
- html files pass through the [Nu HTML Checker](https://validator.w3.org/nu/) with no html issues found
- Errors listed only reference {%%} & {{}} tags.

<img width="500" src="">

- CSS files pass through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/) with no issues found.

<img width="500" src="">

- Lighthouse Results

<img width="500" src="">

- Python files passed through [CI Python Linter](https://pep8ci.herokuapp.com/) with no issues found.

<img width="500" src="">

### Unfixed Bugs

To the best of my knowledge, no bugs exist in the website in its current state.

#

## Technologies Used

### Main Languages Used

- HTML5
- CSS3
- Javascript
- Python

### Frameworks, Libraries & Programs Used

- Google Fonts (https://fonts.google.com/)
- Font Awesome (https://fontawesome.com/)
- GitPod
- GitHub (https://github.com/)
- Balsamiq (https://balsamiq.com)
- Am I Responsive? (https://ui.dev/amiresponsive)
- Bootstrap4 (https://getbootstrap.com/)
- Django (https://www.djangoproject.com/)
- DrawSQL (https://drawsql.app/)
- TinyMCE (https://www.tiny.cloud/)
- ElephantSQL (https://www.elephantsql.com/)
- Heroku (https://dashboard.heroku.com/)
- Pexels (https://www.pexels.com/)

### Installed Packages

- 'django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-allauth [(link)](https://django-allauth.readthedocs.io/en/latest/)
- django-crispy-forms[(link)](https://django-crispy-forms.readthedocs.io/en/latest/index.html)

#

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
- Install Django & Gunicorn:
```pip3 install 'django<4' gunicorn```
- Install Django database & psycopg:
```pip3 install dj_database_url psycopg2```
- Install Cloudinary:
```pip3 install dj3-cloudinary-storage```
- Creating the requirements.txt file with the following command:
```pip3 freeze --local > requirements.txt```
- a django project was created using:
```django-admin startproject PROJECT_NAME .```
- the blog app was then created with:
```python3 manage.py startapp app_name```
- which was then added to the settings.py file within our project directory.
- the changes were then migrated using:
```python3 manage.py migrate```
- navigated to [Heroku](www.heroku.com) and created a new app called 'django-blog-yc'.
- added the Heroku Postgres database to the Resources tab.
- navigated to the Settings Tab, to add the following key/value pairs to the configvars:
1. key: SECRET_KEY | value: randomkey
2. key: PORT | value: 8000
3. key: CLOUDINARY_URL | value: API environment variable
4. key: DATABASE_URL | value: value supplied by Heroku
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- add an import os statement for the env.py file.
- added Heroku to the ALLOWED_HOSTS in settings.py
- created the Procfile
- pushed the project to Github
- connected my github account to Heroku through the Deploy tab
- connected my github project repository, and then clicked on the "Deploy" button

#

## Credits

- Mentor [Martina Terlevic](https://github.com/SephTheOverwitch), a constant source of support, providing reassurance, precious advice and patient guidance.
- Code Institute, for providing the “I think therefore I blog” walkthrough project.
- [Stackoverflow](https://stackoverflow.com), an immense source of solutions to every sort of issue, big or small.
