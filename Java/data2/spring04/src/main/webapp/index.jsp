<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<!-- <link rel="stylesheet" type="text/css" href="resources/css/out.css"> -->
<script type="text/javascript" src="resources/js/out.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<!-- <script type="text/javascript">
call()
//Document Object Model(DOM) tree
//document.ready()
$(function() {
	//JQUERY: 자주 쓰는 자바스크립트 기능을 라이브러리로 만들어 놓은것. 
	//복잡한 문법을 단순화 시켜줌.
	//alert('html이 ram에 모두 로딩되었음.')
	alert("id가 ${user}인 ${name}님 환영합니다.")
})
</script> -->
</head>
<body>
	환영합니다.....
	<br>
	<hr>
	<img src = "resources/img/naver.png">
	<form action="create">
		아이디 : <input type="text" name="id"><br> 
		이름 : <input type="text" name="name"><br>
		URL : <input type="text" name="urls"><br> 
		img : <input type="text" name="img"><br>
		<button>Book 등록 요청</button>
	</form>
	<br>
	<hr color="blue">
	
	<form action="up">
		id: <input type="text" name="id"><br> 
		img : <input type="text" name="img"><br>
		<button>Book 정보 수정</button>
	</form>
	<br>
	<hr color="blue">
	<form action="one.jsp">
		아이디 : <input type="text" name="id" value="${user}"><br>
		<button>Book정보 검색</button>
	</form>
	<a href="one.jsp?id=${user}">${user} 검색 </a>
	<br>
	<hr color="blue">
	<form action="del">
		아이디 : <input type="text" name="id" value="${user}"><br>
		<button>Book 삭제</button>
	</form>
	<a href="del.jsp?id=${user}">
		<button>Book 삭제</button>
	</a>
	<br>
	<hr color="blue">
	<a href="list">
		<button>전체 목록 보기</button>
	</a>
</body>
</html>





