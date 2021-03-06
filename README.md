# Fallout-Blog

## Keys
1. [Deployment](#deployment)
2. [Steps](#steps)
3. [Style](#style)


# IMPORTANT!
During the development of this project I ran into a few errors that took a few days to fix. I also have very poor time management and struggled to hit the deadline. About 60% of the project is finished, I understand that it wont be enough to pass, I will try again next time round.  
Also as a disclaimer. Due to time restraints The majority of the accounts code was following from a tutorial linked below. It is not my code.  
[account-section](https://www.youtube.com/watch?v=DtUBrBbGMxU&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=10)

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
django-allauth

<a name="steps"></a>
# Steps
First I installed the initial items I would need, once I did that I created the project and the app for this workspace.  
I went straight to the models.py page as I wanted to write my post model for the project so I could access it from the admin side of the website.  
I then wrote a couple of test posts in the back end, one was set to published and the other was draft, This was so I could set up only showing the published posts to users. I then created a simple view for the homepage, created a index and base.html, and everything up with a url.  
I used bootstrap, google fonts and fontawesome on the base.html page and extended it's use across all webpages. Using these features allowed me to to use custom fonts, icons and a whole range of bootstrap html and css. I also created my own style.css file in the static folder, This allowed me to edit and style code to my liking.  
Creating the Comment model allowed me to add comments to posts, I first added it to the admin section of the website and wrote some posts from the back end, once it was working in the back end, I wrote the view for the comments and built a form for commenting, then I added it to the post_detail.html page. From there users are now able to leave comments on posts, by just entering their name and their comment. I have also included a comment counter as it will let users know how popular a post is via the number of comments it has.  
Then it was creating catgories for the blog posts, after writing a model for categories, it was just a case of using a context processor to display the category dropdown menu across all pages on the website.  
Once the dropdown functionality was in place I went on to adding a functional search bar to the navigation bar. To achieve this I created it's own html page so that when the user clicks search it will take them to the page with any possible matches inside. I created a view that looks for any words within the title of the page and return the results. The results page will also show users how many (if any) results were found.  
I used django all auth for the account features. I created a new app named accounts to store everything to do with user accounts. Instead of following the generic forms that come with django and all auth, I decided to edit them and write them out myself. I did have some help in doing this and the code for the register form is largely taken from a source I found on stack overflow, it will be linked at the bottom of this page. 

<a name="style"></a>
# Style
I checkout out similar websites and popular website designs and decided to go with colors similar to Facebook as I felt that it was sleek and simple without looking bare and lazy. I kept the design the same on each page to keep things the same throughout, this improves UI as it offers continuity within the project. The color scheme is blue and white. As previously mentioned, I followed Facebook's color style. I did add some smaller styles such as expanding navbar icons upon hover, highlighting items when hovering over them and styling clickable links to make sure the users know they are clickable.


# Help 
https://www.gitpod.io/blog/gitpodify/  

https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/  

https://docs.djangoproject.com/en/4.0/ref/class-based-views/  

https://docs.djangoproject.com/en/3.2/topics/pagination/  

https://github.com/Benjamin-Joe/falloutblog  