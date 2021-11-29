DATABASES = { 
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE 명',
        'USER': 'DB접속 계정명',
        'PASSWORD': 'DB접속용 비밀번호',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'django-insecure-q$ajp^!d^hro#$-h4ch+&mrw6=dzvcl^o6axz50)=c1vii1q0g'
