"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 
import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w$n*&qk^$2g5ki5yi!&=0#kpygbxb5s78^y+o*!b#2d)0(bp8#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eightfortypy',
    
    # allauth 회원가입 가능 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
    
    # django로 감싼 태그 안에 css를 심어주기 위한 패키지 
    'widget_tweaks',
    
]

SITE_ID = 1 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    
]

ROOT_URLCONF = 'backends.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backends.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# pymysql.install_as_MySQLdb() 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test_db',
#         'USER': 'admin',
#         'PASSWORD': '1234',
#         'HOST': 'db',
#         'PORT': '3306',
#     }
# }

# 추후에 웹 모듈 모두 완성하면 이걸로 대체 할 예정

# 기본 데이터베이스
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'frontend/'
STATIC_ROOT = os.path.join(BASE_DIR,'_frontend')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend')
] # 모든 frontend 구역은 메인 backend 디렉토리의 static 디렉토리로 통합시킴 


MEDIA_URL = "upload/"
MEDIA_ROOT = os.path.join(BASE_DIR, "upload")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# allauth에 필요한 요소들 모두 넣어줄 예정 

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
] # allauth 기능을 init 해준다 라는 기능

# 회원가입 모델 
AUTH_USER_MODEL = 'eightfortypy.User'

# 이메일 세팅 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 로그인 / 회원가입 성공했을 시 랜더해줄 옵션 
ACCOUNT_SIGNUP_REDIRECT_URL ='index'
LOGIN_REDIRECT_URL = 'index'
# index 페이지로 옮겨준다

# 로그아웃 진짜 하시겠습니까?! 라는 경고문 없이 바로 로그아웃
ACCOUNT_LOGOUT_ON_GET = True

# 유저닉네임으로 로그인이 아닌 이메일로 설정
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 이메일로 로그인하기 만들기


# 현재는 로그인 및 회원가입을 할때 닉네임으로 설정하게끔 만들었으나 
# 이 옵션을 통해, 닉네임은 선택, 이메일은 필수로 바꾸게 하여 
# 이메일 로그인/ 회원 가입으로 설정을 바꿈
ACCOUNT_EMAIL_REQUIRED = True # 이메일 입력 필수
ACCOUNT_USERNAME_REQUIRED = False

# 로그아웃 없이 웹사이트를 나가도 로그인을 유지시켜줌
ACCOUNT_SESSION_REMEMBER = True
# SESSION_COOKIE_AGE = 3600 # 쿠키 유지시간 1시간 한시간 뒤에는 재 로그인을 해야한다
# 딱히 필요는 없어서 그냥 둠 

# 지금 회원가입 폼을 가서 작성을 하다가 오류가 생기면 비밀번호가 초기화가 되는데
# 조금 번거롭다, 그걸 방지하기 위해서 이 옵션을 추가
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True # 유효성을 만족하지 않더라도 비밀번호가 초기화 되지 않는 옵션

# 이메일 인증 시스템 
ACCOUNT_EMAIL_VARIFICATION = "optional" #인증이 될때까지 로그인은 가능함 원래 default 값으로 줌
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# 로그인 인증이 되었는가 안 되었는가?
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirm"# 유저가 로그인이 됐을 때 렌더링
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirm" # 유저가 로그인이 안 됐을 때 렌더링

#비밀번호 찾기 유효시간 만들기 
PASSWORD_RESET_TIMEOUT_DAYS = 3 # 비밀번호 찾기 유효시간
# 기본적으로 3일이 디폴트 값으로 세팅되어 있다.

# admin창에서 보면 로그인 로그아웃 내역들이 엄청 쌓이는걸 방지시켜줌
ACCOUNT_EMAIL_SUBJECT_PREFIX = "" """ 로그인을 할 때마다 인증내역을 admin으로 보내지는걸 없애려고 '' 공백처리 """

