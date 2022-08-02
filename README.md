# sparta_1_week: 스파무비 프로젝트

> 회원이 영화를 추천 받고 평점과 코멘트도 볼 수 있으며 예매 사이트로 바로 날아갈 수 있는 사이트

---

![1659403986581](https://user-images.githubusercontent.com/110365590/182273096-cc26ce49-5599-478a-9ab6-61dc63b6c428.png)


---

## Login
## Sign-up
둘이 한 페이지로 회원가입은 css로 hidden, classname "on"을 이용, 토글로 보이게 하는 것이 목표
- 로그인 / 회원가입/ 로그아웃 만들기 


## Root
> 회원만 서비스를 사용가능하게 만들기 위해서 처음 페이지를 /login로 시작하기 (루트 접속 시 /login으로 redirect 할 필요가 있다.)
- index.html 코드 스니팻을 수정하기  
- 데이터를 크롤링 해서 db에서 영화를 넣기 
- 영화 데이터를 홈페이지("/")에 띄우기
- 영화 예매 사이트의 댓글 크롤링하여 첫번째 것 보여주기

## movie
- 영화 데이터를 불러와 화면 구현하기

## DB, AWS
- Mongo Db 연결하기, EC2연결하기, 최종 파일 업로드, 도메인 연결해 배포하기 
- html파일들을 서로 유기적으로 연결시키기(login -> root , login -> join// 즉 router관리)

---


| 기능 | 방법 | URL router | request | response | 데이터 타입 | 방법 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 로딩 시 영화 가져오기 | get  | /      |                   | db.movies.des  | {영화 이미지, 설명}
| 영화 평점, 가져오기   | get  | /:{id} |                   | db.movies.data | {평점, 리뷰}   
| 예매하러가기          | get  | /:{id} |                   | db.movies.link | {provider, Link}
| 로그인                | post | /login | id,pw(hashed)     | ture, false    | boolean 
| 로그아웃              | post | /      |                   |                |
| 회원가입              | post | /join  | id,pw(hashed)     | alter          |

---
