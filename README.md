# Fallout-Blog

## Keys
1. [Deployment](#deployment)


<a name="deployment"></a>
# Deployment
The first thing I did was deploy this project as it is much easier to deploy early to avoid any issues further down the line with deployment.
This project was deployed to heroku through the following steps:  
Create Heroku app on Heroku  
Add PostgreSQL database to app  
Conntect project to postgres database  
Create env.py file and add in confid vars from Heroku (create secret key)  
Wire up Postgres Database  
Add cloudinary url to env.py  
Add cloudinary to config vars on Heroku   
Add DISABLE_COLLECTSTATIC to config vars on Heroku  
Add static and media file storage to settings file  
Add Databases, DIRS templates and allowed hosts (heroku app name) to settings file  
Create static, media and templates folders  
Create Procfile  
Deploy the project on heroku in the deploy tab inside this app  


# Installed Items
django  
gunicorn  
dj_database_url  
psycopg2  
dj3-cloudinary-storage  
pillow


# Help 
https://www.gitpod.io/blog/gitpodify/

# Steps
First I installed the initial items I would need, once I did that I created the project and the app for this workspace.  
I went straight to the models.py page as I wanted to write my post model for the project so I could access it from the admin side of the website.

