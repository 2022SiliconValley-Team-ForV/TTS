from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent



MY_SECRET = {
    "SECRET_KEY" : 'django-insecure-(#xlu@*$4st!ku5%8nmtx)6k&^o3w*#qnn6rr+bsgr=np@f7pq'
}

MY_DATABASES = {
    'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'tts', 
        'USER': 'root', 
        'PASSWORD': 'password', 
        'HOST': 'localhost',
        'PORT': '3306', 
     } 
}