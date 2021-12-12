# Fallout-Blog

## Keys
1. [Deployment](#deployment)
2. [Steps](#steps)
3. [Style](#style)

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
To help with deployment I followed the think before I blog set up section within Code Institute's
video tutorials

# Installed Items
django  
gunicorn  
dj_database_url  
psycopg2  
dj3-cloudinary-storage  
pillow

<a name="steps"></a>
# Steps
First I installed the initial items I would need, once I did that I created the project and the app for this workspace.  
I went straight to the models.py page as I wanted to write my post model for the project so I could access it from the admin side of the website.  
I then wrote a couple of test posts in the back end, one was set to published and the other was draft, This was so I could set up only showing the published posts to users. I then created a simple view for the homepage, created a index and base.html, and everything up with a url.  
I used bootstrap, google fonts and fontawesome on the base.html page and extended it's use across all webpages. Using these features allowed me to to use custom fonts, icons and a whole range of bootstrap html and css. I also created my own style.css file in the static folder, This allowed me to edit and style code to my liking.  
Creating the Comment model allowed me to add comments to posts, I first added it to the admin section of the website and wrote some posts from the back end, once it was working in the back end, I wrote the view for the comments and built a form for commenting, then I added it to the post_detail.html page. From there users are now able to leave comments on posts, by just entering their name and their comment. I have also included a comment counter as it will let users know how popular a post is via the number of comments it has.

<a name="style"></a>
# Style
I checkout out similar websites and popular website designs and decided to go with colors similar to Facebook as I felt that it was sleek and simple without looking bare and lazy. I kept the design the same on each page to keep things the same throughout, this improves UI as it offers continuity within the project. The color scheme is blue and white. As previously mentioned, I followed Facebook's color style. I did add some smaller styles such as expanding navbar icons upon hover, highlighting items when hovering over them and styling clickable links to make sure the users know they are clickable.



# Help 
https://www.gitpod.io/blog/gitpodify/



