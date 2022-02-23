<br />
<div align="center">
    <a href="https://todaytheylearn.com/">
  <img src="https://user-images.githubusercontent.com/70438098/155125625-8a56f73e-47ae-4421-8f64-c11945d65f37.gif" alt="TTL_logo" width="350"/>
    </a>
</div>

<div align="center">
  <h3>모든 TIL을 한 곳에서 모아보세요. 📚</h3>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/socket.io-010101?style=for-the-badge&logo=socket.io&logoColor=white" style="margin: 1px">
	<img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" style="margin: 1px">
  <br/>
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white" style="margin: 1px"/>
	<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white" style="margin: 1px"/>
  <img src ="https://img.shields.io/badge/Swagger-85EA2D.svg?&style=for-the-badge&logo=Swagger&logoColor=white" style="margin: 1px"/>
</div>

<br/>
<br/>

# TTL_API  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftoday-they-learned%2Fttl_api&count_bg=%237186C0&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=TTL&edge_flat=false)](https://hits.seeyoufarm.com)


**목차**
- [서비스 소개](#서비스-소개)
- [서비스 기획 의도](#서비스-기획-의도)
- [메인 기능](#메인-기능)
- [사이트 구조 개요](#사이트-구조-개요)
- [디비 스키마 구조](#디비-스키마-구조)
- [API 구조](#API-구조) 

<br/>

## 📝 서비스 기획 의도

😇 TTL은 아래와 같은 분들을 위해 구상된 아이디어로 시작되었습니다.

1️⃣  열심히 개발 공부를 하고, 배운 것을 정리하고 싶은 사자

2️⃣  Github 잔디를 열심히 키우고 있는 사자

3️⃣  블로그 활동을 꾸준히 하려고 하는 사자

<br />

TIL은 `Today I Learned`의 약자로 그날그날 내가 공부한 것을 정리하는 것을 뜻합니다.

주로 Github이나 Tistory, velog 등에 하루하루 본인이 배운 것들을 기록/정리합니다.

TTL`Today They Learned` Github, Tistory, velog 등 다양한 곳에 나눠져 있는 TIL을 모아서 볼 수 있게 만들어주는 서비스입니다.
또한 TTL에서 글을 작성할 수 있으며 다양한 이모지를 남길 수 있습니다.


<br />

## 📚 메인 기능 

- 기본적인 **TIL 피드/작성/댓글/북마크** 등의 기능을 제공합니다.

- 기존에 Github 또는 Velog에 **작성한 글을 옮겨오는 기능**을 제공합니다.

- TTL에서 굳이 글을 작성하지 않아도, **Github/Velog에 작성한 글을 주기적으로 동기화하는 기능**을 제공합니다.

- TIL에 **다양한 이모지**를 달 수 있습니다.

<br />

## 🗃 사이트 구조 개요

**TTL** 은 프론트엔드와 백엔드가 따로 분리되어 있는 구조입니다.

프론트엔드는 `React.js` 로 개발되었습니다.
백엔드는 `Django` 로 개발되었으며, `django-rest-framework` 를 이용한 API 서버로 구성되어있습니다.

<br />

## 💻 디비 스키마 구조

### 전체 모델 스키마
![서비스 모델 스키마](./docs/total_model.png)

### DB 스키마
![디비 스키마](./docs/model.png)

<br />

## 📡 API 구조

아래 API docs 사이트를 통해 쉽게 확인하실 수 있습니다.
### Swagger
- [Swagger](https://api.todaytheylearn.com/) 

- ![Swagger Example](./docs/ttl_swagger.png)

### Redoc
- [Redoc](https://api.todaytheylearn.com/redoc/)

- ![Redoc Example](./docs/ttl_redoc.png)

<br />

## 🔗 Links

* [웹사이트](https://todaytheylearn.com/)
* [이슈 트래커](https://github.com/today-they-learned/ttl_api/issues)
* [소스코드](https://github.com/today-they-learned/ttl_api)

<br/>

## 👥 BACKEND_PEOPLE

| [김신건](https://github.com/shinkeonkim) | [진승희](https://github.com/Jin409) | [최지현](https://github.com/Jihyun-Choi) |
|:--------:|:--------:|:--------:|
|<img src="https://avatars.githubusercontent.com/u/47373998" width="180" height="160">|<img src="https://avatars.githubusercontent.com/u/77621712" width="180" height="160">|<img src="https://avatars.githubusercontent.com/u/70438098" width="180" height="160"> |

<br/>
