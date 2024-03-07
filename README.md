# Sending Emails with Django!

## Guide:

#### After the repo has been cloned, you need to install some dependencies. Follow the steps so you can run the project and try yourself.

#### The following commands should be entered into your terminal in order:

1. **pipenv install**
2. **pipenv shell**
3. **pipenv install Django**
4. **pipenv install python-decouple**
5. **pipenv install django-bootstrap-v5**

First, you are installing a virtual enviroment to run the project. Sencond, you are accessing this enviroment. Then you are downloading the framework and a lib.
Now you have to create a file named '.env'. In this file, you need to write these lines:

EMAIL_HOST_USER=your email address in here <br>
EMAIL_HOST_PASSWORD=your app password in here <br>

The host user is the email address that you want to use. In this project I made with gmail.
To get the host password: just google "'gmail' + 'how to get app password'" and you are fine.

Now, you just have to set the email address that you want to send the message. Go to views.py and inside of the method 'send_mail', add the email address. Just like this:

    send_mail(
            'New Message!',
            f'Message from: {message_name}\nEmail: {message_email}\n\n{message}',
            message_email,
            ['example@gmail.com'],
        )

Once you have done all this stuff, you should be able to run the project correctly.

## If you have any suggestions or doubts, contact with me!

github.com/lucasberenger<br>
https://www.linkedin.com/in/lucas-berenger/
