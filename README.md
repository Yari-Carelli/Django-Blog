# Django Blog
A simple, fully-functional blog built with Django and Bootstrap4.

The live link for the project can be found [HERE](https://django-blog-yc.herokuapp.com/)

#

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


### User Stories

#### As the Site Admin:
1. I can add, edit and delete posts so that I can manage the blog content.
2. I can add, edit and delete authors so that I can select which site users can create posts.
3. I can add, edit and delete categories so that I can manage the topics discussed in the blog.

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
10. I can use the contact form to submit enquiries to the site's staff members.

#

### Features Left to Implement

- Update/Delete comments
- Newsletter subscription form
- Like/Unlike posts/comments
- Tags widget
- Contact form where users can enter their name, email address, and message, and the website will email the message to the staff (with the user's email as the reply-to)
- Use the social apps feature of AllAuth to add single sign-on functionality using Google, Facebook, or another authentication provider

#

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
- Bootstrap4 (https://getbootstrap.com/)
- Django (https://www.djangoproject.com/)
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

The site was deployed to Heroku following the instructions below.

Django Deployment Instructions:

In the Terminal:

1. Install Django and Gunicorn:
```pip3 install 'django<4' gunicorn```
2. Install supporting libraries:
```pip3 install dj_database_url psycopg2```
3. Install Cloudinary Libraries:
```pip3 install dj3-cloudinary-storage```
4. Create requirements file:
```pip3 freeze --local > requirements.txt```
5. Create Project:
```django-admin startproject PROJECT_NAME .```
6. Create App:
```python3 manage.py startapp APP_NAME```

In settings.py:

7. Add to installed apps:
```
INSTALLED_APPS = [
…
'APP_NAME',
]
```

In the Terminal:

8. Migrate changes:
```python3 manage.py migrate```

In ElephantSQL:

9. Log in to your ElephantSQL account
10. Click “Create New Instance”
11. Set up your plan:
   - Give your plan a Name (this is commonly the name of the project)
   - Select the Tiny Turtle (Free) plan
   - You can leave the Tags field blank
12. Click “Select Region” (Note: If you receive a message saying "Error: No cluster available in your-chosen-data-center yet", choose another region)
13. Click “Review”, then click “Create instance”
14. Return to the ElephantSQL dashboard and click on the database instance name for this project
15. Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://

In Heroku:

16. Create new Heroku App:
```APP_NAME, Location = Europe```
17. Open the "Settings" tab
18. Click "Reveal Congig Vars" (Note: The value should be the ElephantSQL database url you copied in the previous step)

In Gitpod:

19. Create new env.py file on top level directory
20. Import os library
```import os```
21. Set environment variables:
```os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"```
22. Add in Secret Key:
```os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"```

In Heroku:

23. Add Secret Key to Config Vars
```SECRET_KEY, “randomSecretKey”```

In settings.py:
24. Reference env.py:
```
import os
import dj_database_url

if os.path.isfile("env.py"):
   import env
```
25. Remove the insecure secret key and replace (links to the SECRET_KEY variable on Heroku)
```SECRET_KEY = os.environ.get('SECRET_KEY')```
26. Comment out the old Databases section:
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
```
27. Add new Databases section (links to the DATATBASE_URL variable on Heroku):
```
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
``` 

In the Terminal:

28. 
```python3 manage.py migrate```

In Cloudinary:

29. Copy your CLOUDINARY_URL:
```From Cloudinary Dashboard```

In env.py:

30. Add Cloudinary URL:
```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

In Heroku:

31. Add Cloudinary URL to Heroku Config Vars:
```COUDINARY_URL, cloudinary://************************``` 
32. Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment)
```DISABLE_COLLECTSTATIC, 1```

In settings.py:

33. Add Cloudinary Libraries to installed apps (Note: order is important):
```
INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    …,
]
```
34. Tell Django to use Cloudinary to store media and static files (place under the Static files note):

```
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

```
35. Link file to the templates directory in Heroku
(place under the BASE_DIR line):
```TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')```
36. Change the templates directory to TEMPLATES_DIR
(place within the TEMPLATES array)

```
TEMPLATES = [
    {
        …,
        'DIRS': [TEMPLATES_DIR],
       …,
            ],
        },
    },
]
```
37. Add Heroku Hostname to ALLOWED_HOSTS:
```ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]```

In Gitpod:

38. Create static and templates folders on top level directory
39. Create Procfile on the top level directory

In Procfile:

40. Add code:
```web: gunicorn PROJ_NAME.wsgi```

In the Terminal:

41. After saving all files, add, commit and push:
```git add .```
```git commit -m “...”```
```git push```

In Heroku:

42. Click on "Deploy" tab, select Github as deployment method, on main branch, and deploy content manually

#
