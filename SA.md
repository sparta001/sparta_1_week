| 기능 | 방법 | URL router | request | response | 데이터 타입 | 방법 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 로딩 시 영화 가져오기 | get  | /      |           | db.movies      | {영화 이미지, 설명}
| 영화 평점, 가져오기   | get  | /:{id  |           | db.movies.data | {평점, 리뷰}   
| 예매하러가기          | get  | /:{id} |           | db.movies.link | {provider, Link}
| 로그인                | post | /login | id,pw     | ture, false    | boolean 
| 로그아웃              | post | /      |           |                |
| 회원가입              | post | /join  |id,pw      |                |
