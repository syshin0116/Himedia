<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
  
<c:set var="contextPath" value="${pageContext.request.contextPath}"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

</head>
<body>

	<h2>목록</h2>
			<table class="bluetop">
				<tr>
					<td>아이디</td>
					<td>이름</td>
					<td>URL</td>
					<td>IMG</td>

				</tr>
				<c:forEach var="book" items="${book_list}" varStatus="status">
				<tr>
					<td><a href="${contextPath}/view.jsp?id=${book.id}">${book.name}</a></td>
					<td>${book.name}</td>
					<td>${book.urls}</td>
					<td>${book.img}</td>
					<td><img src = "resources/img/${book.img}"><td>
				</tr>
				</c:forEach>
			</table>
			<button onclick="location.href='${contextPath}/create.jsp'">북 추가 </button>

</body>
</html>