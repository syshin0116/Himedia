<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Header
    ================================================== -->
		<div id="nino-headerInner">					
			<nav id="nino-navbar" class="navbar navbar-default" role="navigation">
				<div class="container">

					<!-- Brand and toggle get grouped for better mobile display -->
					<div class="navbar-header">
					<!-- 화면이 작아지면 헤더 메뉴 토글로 바뀐다. -->
						<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nino-navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<!-- 왼쪽 상단 로고부분 -->
						<a href="#" class="navbar-brand" onclick="location.href='/trip/main.jsp'">HITRIP</a>
					</div>

					<!-- Collect the nav links, forms, and other content for toggling -->
					<div class="nino-menuItem pull-right">
						<div class="collapse navbar-collapse pull-left" id="nino-navbar-collapse">
							<ul class="nav navbar-nav">
								<li class="active"><a href="#nino-header">여행지 <span class="sr-only">(current)</span></a></li>
								<li><a href="#nino-story">여행지 추천</a></li>
								<li><a href="#nino-services">통계</a></li>
							</ul>
						</div><!-- /.navbar-collapse -->
						<ul class="nino-iconsGroup nav navbar-nav">
							<li><a href="#" onclick="location.href='/trip/member/loginMain.jsp'" style="font-size: small"><i class="mdi mdi-login nino-icon">로그인</i></a></li>
							<li><a href="#" onclick="location.href='/trip/member/rgstSelect.jsp'" style="font-size: small"><i class="mdi mdi-emoticon-outline nino-icon">회원가입</i></a></li>
						</ul>
					</div>
				</div><!-- /.container-fluid -->
			</nav>
		</div>