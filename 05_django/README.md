# 시작하기 전에...

## 프로젝트 관리
- TIL, 학습하고 있는 각종 폴더, 관통 PJT
- git으로 관리중
    - TIL/**/*.py.....
    - git으로 관리 되지 않아야 할 목록
        - .gitignore

## 가상환경
- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경
- git으로 관리 안한다. -> gitignore
- requirements.txt -> 해당 프로젝트를 위한 독립 환경 목록 구성

- local 작업할 때, 가상환경 안만들고, global에 django 설치하고 작업 진행하면, 매번 똑같은 환경에서 진행하는데 왜 필요할까?

### 가상환경 생성
```bash
# Django 프로젝트 생성 전 루틴 (작업위치 확인하기)

# 1. 가상환경(venv)생성)
$ python -m venv venv
# 2. 가상환경 활성화
$ source venv/Scripts/activate
# 3. Django 설치
$ pip install Django
# 4. 의존성 파일 생성
$ pip freeze > requirements.txt
```


```bash
# 현재 pip 목록을 얼린다.
$ pip freeze > requirements.txt

# requirements.txt를 읽으면서 해당 라이브러리들을 일괄 설치
$ pip install -r requirements.txt
```

```bash
$ django-admin startproject firstpjt .
# firstpjt라는 이름의 프로젝트를 생성하겠다. (. -> 현재 디렉토리에)

$ python manage.py runserver
# manage.py와 동일한 경로에서 명령어를 진행

# 앞으로 장고를 배울때 manage.py + 명령어와 같은 형태를 많이 사용할 것 
```

* 서버를 끄는 명령어 터미널에서 Ctrl + C.
* 서버 종료를 정상적으로 하지 않고 터미널을 강제종료하거나 하는 경우, 서버가 꺼지지 않는 경우가 있으므로 정상적으로 종료할 것.
* 프로젝트 = 애플리케이션의 집합(DB설정, URL연결, 전체 앱 설정 등)
* 애플리케이션 = 독립적으로 작동하는 기능 단위 모듈

```bash
# 앱 생성
$ python manage.py startapp articles
```

* 앱을 생성하고나서 프로젝트 폴더의 settings.py 파일에서 INSTALLES APPS에 앱을 등록해야함
```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### articles app의 메인 페이지 화면에 띄우기
1. client가 요청 보낼 경로 지정하기 -> url
2. 특정 경로에 요청이 왔을 떄, 그 요청에 적절한 처리 하기 (함수) -> views.py
3. 적절한 처리 과정에서 template(html)이 필요하다면, 작성하기 -> template/*.html
4. 작성된 template을 사용자에게 반환하기 -> views에 정의한 함수의 return