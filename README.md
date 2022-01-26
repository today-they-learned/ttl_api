# TTL_API

## Dev Environment Setting

### 프로젝트 폴더 바로 아래에 .env 파일을 만들고 아래 내용을 넣어주세요.
```
SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_SETTINGS_MODULE=config.settings pylint --load-plugins pylint_django
FRONT_DEV_PORT=3000
```

### 라이브러리 설정하기
```shell
# 가상환경 만들기
> python -m venv venv

# 가상환경 활성화
## Windows
> .\venv\Scripts\activate
## Mac
> source venv/bin/activate

## 라이브러리 설치하기
> pip install -r requirements.txt

## django 실행하기
> python manage.py migrate
> python manage.py runserver
```

### Tip! venv exit하는법
```shell
> deactivate
```

### Third party 설치하는 법

```shell
# 가상환경 활성화 후에!

# 설치
> pip intall blahblah

# 다른 작업자가 이를 알 수 있게, requirements.txt에 반영하기
> pip freeze > requirements.txt
```

### Docker를 이용한 개발 환경 구성

1. 아래 환경변수를 .env파일에 추가로 넣어주세요.

```
# DOCKERIZE SETTINGS
PORT=1234
USE_DOCKER=True

## POSTGRES SETTINGS
POSTGRES_NAME=postgres
POSTGRES_PORT=5123
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

2. `docker-compose up -d --build`

## 문서화 확인하는 방법

[127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger) 또는 [127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 접속하기 
