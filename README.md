Flask Sea Battle
====
Student Project<br>
UWA 2022 Sem-1 CTIS3403 Agile Web Development<br>
Group 75<br>
----
<br>
Setup guide<br>
<br>
<br>

1. in project root directory, make virtual environment<br>

>python -m venv venv<br>

<br>
<br>

2. activate virtual environment

in Linux

>source venv/bin/activate<br>

in Windows 
>venv\Scripts\activate<br>

<br>
if PowerShell shows this

>...venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.<br>

running .ps script is disabled by default<br>
check it<br>

>Get-ExecutionPolicy

should be "Restricted" by default<br>
bypass it<br>
>Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force<br>

after activation, CLI should shows

>(venv)...

<br>
<br>

3. install pip dependencies<br>

>pip install -r requirements.txt<br>

<br>
<br>

4. create database<br>

>flask db init<br>
flask db migrate<br>
flask db upgrade<br>

every time after changing database structure<br>
>flask db migrate<br>
flask db upgrade<br>

<br>
<br>

5. run<br>
>flask run<br>


pages on<br>
http://127.0.0.1:5000
<br>
<br>
manipulate database manually in CLI<br>

>flask shell<br>

<br>

unit test<br>

>test.py

<br>
<br>
<br>
<br>
<br>
currently, in "app.db"<br>
<br>
there are 2 test users<br>
<br>
　　　　password<br>
john　　ura!<br>
node　　wtf<br>
<br>
<br>
<br>
<br>
<br>
each file do what<br>
in ./<br>
game.py　　the main .py<br>
config.py　　configurations for Flask, db etc.<br>
<br>
in ./app<br>
__init__.py　　basic config to run Flask<br>
errors.py　　handling 404 and 500<br>
forms.py　　filling the Jinja2 tags in "login.html" and "register.html"<br>
models.py　　database table<br>
routes.py　　redirecting, game logic<br>
<br>
in ./app/templates<br>
　　.html files with Flask Jinja2 tags<br>
