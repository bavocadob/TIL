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
Initialized empty Git repository input.txt C:/Users/SSAFY/Desktop/python/.git/
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
```bash
$ git log
```

### 최근 커밋 수정하기
```bash
$ git commit --amend
#INSERT
#:wq
# write and quit
```

### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# vim을 활용해서 설정 제거하기
# vim git 설정 파일 열기
$ vim ~/.gitconfig
# insert 키: 수정 상태 만들기
# --insert-- 인 상태에서 모든 내용 삭제
# esc: 수정 상태 종료
# :wq
```

### 원격 저장소 git에 등록
```bash
$ git remote add {remote_nickname} {remote_url}
$ git remote -v
```


### 원격 저장소에 업로드
```bash
$ git push origin master
```

### 원격 저장소에 있는 내용 복제
- 첫 Clone 시 
```bash
$ git clone {github_url}
```
- 이미 폴더가 존재할 때
```bash
$ git pull origin master
```

### git ignore
- git에서 추적하지 않을 파일이나 폴더 등록
- .gitignore 파일이용
- [gitignore.io](https://www.toptal.com/developers/gitignore/) 에서자동 생성 지원