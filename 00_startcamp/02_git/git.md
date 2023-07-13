# GIT이란...
> 분산 버전 관리 시스템

## Git의 3가지 영역
1. Working directory
<p>실제 작업 영역</p>

2. Staging Area
<p>중간 준비 영역</p>

3. Repository
<p>저장되는 영역.</p>
<p>버전(commit) 이력이 기록됨</p>

4. commit
<p>변경된 파일들을 저장하는 행위 snapshot이라고도 함</p>


### git 초기화
```bash
$ git init
Initialized empty Git repository in C:/Users/SSAFY/Desktop/python/.git/
```

### 상태 확인 명령어
```bash
$ git status
```

### 스테이징 에어리어에 추가 (GIT ADD)
```bash
$ git add {path}<folder_name>/{README.md}
```

### Repository에 저장하기
```bash
$ git commit -m "commit message"
```

### 기초설정
```bash
$ git config --global user.email {email}
$ git config --global user.name {name}
$ git config --global --list 

user.email= {email}
user.name= {name}
```

### 커밋 기록 확인하기

