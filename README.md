# The Beginnersblog
creating a Beginnersblog
Very first step:
          At the start you need to install flask framework......
  get ready....
  create a folder named microblog and install the flask framework in the folder...
  
---> Creating an instance called app of flask with in the __init__.py(microblog folder) file.
---> Create an introduction html named index.html(lets start with creating "hello world" thing) with in the templates      folder(./microblog/app/template/index.html)...
---> I think this pretty lengthy introduction...... next we start creating loginpage so it should have a form that accept the email-ID,for authentication purpose we have openid providers(google,yahoo,AOL......) 
---> Create the forms using a flask extension wtf.... in a forms.py(microblog/app/forms.py) all the forms class will be coded here in the forms.py file.....
---> and in the above same folder create a views.py where authentication and user activity is taken care.......
---> In the login view function login is handeld by openid authentication......
---> where flask extension provide login extension....
---> and then start adding the database thing using My SQlite database
---> Need to create db object in the __init__.py
---> then start creating database classes in the models.py where we have user class and post class...... 
---> Then we have TEMPLATES:
      * 404.html and 500.html : handling the error page....
      * base.html : this is the main html page where other html pages gets extended using block content with in              the'{%' and '%}' which is taken care by jinja extension from flask.
      * edit.html : this is the template where user edit his about and his nickname things...........
      * follower_email.html : this is template that sent to user email-ID so that he knows some other user is                following.... this is handled by SMTPHandlers by default it is provided by python.
      * index.html : this is the home page implimentation of user.
      * login.html : this is where user enter his login details.
      * post.html : this is used to display posts in the home page and the profile page.
      * search_results.html : this provide search bar so that we can find some text that entered in the search bar 
        text found in the posts
      * user.html : used for profile page display
---> config.py : where used to store global variables
---> forms.py : where web forms are created
---> models.py : where databases of classes arecreated.
---> views.py : where openid and logins are managed.
---> decorators.py : where multithread is handled.
The above files are stored within app folder

---> db_create.py : where database is created and it's name is app.db
---> db_downgrade.py : scripts helps in the downgrade of database whenever required.
---> db_upgrade.py : this scripts helps in the upgradation of database.
---> db_migrate.py : this scripts helps in the migration of database.
The above files are stored within microblog folder.
