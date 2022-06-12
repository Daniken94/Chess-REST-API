# Chess-REST-API
It's a simple REST API for checking chess figure moves and their moves validation.

This API running on a flask and doesen't have any restrictions.


## Instalation:

Run the following command in your terminal:

Clone repository using SSH key:

```
git clone git@github.com:Daniken94/Chess-REST-API.git
```
or download 'zip'.

## Requirements:
Python is required !!!


You can install all app from requirements.txt by using command:

```
pip install -r requirements.txt
```
Or you can do it manually by executing the following commands:

```
pip install flask==2.1.2
```
```
pip install flask_restful==0.3.9
```
```
pip install pytest==7.1.2
```

## Execution:

Run the following code in your terminal:

```
python main.py
```
In order to terminate the use and shut down the server it is necessary to run command in your terminal:

```
crtl + c
```

# How it use:


<img src="Daniken94/Chess-REST-API/blob/main/image/chess-board.jpg" width="128"/>




- Crate new folder and new working environment using python/pip.
- Install requirements.txt using pip. `pip install -r requirements.txt`,

- Run Django command `python manage.py makemigrations` to make/prepare migrations,
- Run Django command `python manage.py migrate` to implement migrations,
- Run Django command `python manage.py createsuperuser` and create superuser to can use django admin site,
- Run Cron command `ppython manage.py crontab add` to initial cron task,
- Lastly run App using `python3 manage.py runserver`.