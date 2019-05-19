# TODO-List
2019 Summer Coding Project

## 설치 및 빌드 방법
1. 서버에 git 내용을 받아옵니다.
```Shell
git clone "https://github.com/ase3238/TODO-List/"
```
2-1. django가 설치가 되어있지 않다면 django를 설치하여 줍니다.
설치는 django 공식 사이트를 따라주시면 됩니다.
> https://docs.djangoproject.com/ko/2.2/intro/install/

2-2. 이 프로젝트는 2개의 외부 api를 사용합니다. 이들을 설치해줍니다. (bootsrtap, datetime widget)
```Shell
pip install django-crispy-forms
pip install django-tempus-dominus
```

2-3. 서버를 실행합니다.
```Shell
python3 manage.py runserver
```
