# Portfolio website

Hello World!

Welcome to my capstone project for Harvard's (https://cs50.harvard.edu/web/2020/) course.

### What is this project all about?

The website serves as a showcase for my past, current, and future works and projects. It is mobile responsive, utilizes Django and JavaScript, and features a NavBar for easy navigation.

Watch a video walkthrough of the website [HERE](https://youtu.be/FfW5DDpolrs)!

### Quickstart

```
# Create new migrations
python3 manage.py makemigration

# Migrate
python3 manage.py migrate

# Start development server 
python3 manage.py runserver

# In browser, navigate to generated URL (typically local host http://127.0.0.1:8000/)
```
To facilitate navigation on the website, I have implemented a user-friendly NavBar. By using the NavBar, visitors can easily access different sections and pages of the app.

As an interesting feature, if the user clicks on my name five times consecutively, it will trigger a redirection to the admin login page. This provides an exclusive access point for the admin to log in and make modifications to the data displayed on the app. The admin login page ensures that only authorized individuals can access and edit the website's content.

By incorporating this functionality, I have created a secure and controlled environment where the admin can conveniently manage the information presented on the app, maintaining the integrity and accuracy of the portfolio.

## Backend

### File Structure

This project follows a typical Django file structure taught in this course. Python code corresponding to each of the app's 'views'  is stored in the file `views.py`. The site's various URL patterns can be found in `urls.py`.  The app's in-built database is built on four tables (User, Profile, Section, and Project) defined in the file `models.py`, with the database saved as `db.sqlite3`. It also has `forms.py` which defines all the user form needed to modify the webpage itself!

The website consists of 9 HTML pages, most of which extend from a layout file (`layout.html`) using Django's templating language. These files are stored in the `templates` directory. `index.html` (the app's default route), displays the about page; `resume.html` displays the current resume I have; `projects.html` displays the works I have done.

The `static` folder contains the css needed for the html pages. The `files` folder has all the media, photo and video, which the user uploads. All the JS code are enclosed in `<script>` tags in the corresponding html files.

Outside of these core files, the app's dependencies can be found in `requirements.txt`.

## Et al.

### Distinctiveness and Complexity

I have developed my own portfolio website from scratch, starting with an empty Django template. Throughout the development process, I have incorporated numerous tools and techniques covered in CS50W. The website includes three additional models alongside Django's User model, enabling it to handle video files and images seamlessly.

The primary purpose of my portfolio website is to showcase my past, current, and future works and projects. I am committed to continually refining and enhancing the website to ensure it remains up to date and relevant.

In addition to meeting CS50W's grading requirements, my portfolio website is designed to be mobile responsive, allowing it to adapt and display optimally on different devices. It extensively utilizes Django and incorporates JavaScript functionalities, as described above.

By combining my technical skills and creativity, I have developed a powerful platform that effectively presents my portfolio and demonstrates my capabilities as a developer.

### Acknowledgements

- W3Schools - [LINK](https://www.w3schools.com/)
- Django's Official Docs - [LINK](https://djangoproject.com)
- TeleportHQ - [LINK](https://teleporthq.io/)
- CS50W - [LINK](https://cs50.harvard.edu/web/2020/)


### About Me

Hi, I'm Matthew Ng! A university student from Singapore! I am passionate in all things IT, in fact I'm studying Computer Science! This project has made me realised that I have a strong liking for the web industry and would very much love to make it my career path when I graduate!

Let's connect!
 - LinkedIn - [LINK](https://www.linkedin.com/in/matthewngdeen/)
 - GitHub - [LINK](https://github.com/macoki07)

<hr>