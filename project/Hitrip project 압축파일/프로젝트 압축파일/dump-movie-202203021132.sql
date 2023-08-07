-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: movie
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `mId` varchar(100) NOT NULL,
  `mPw` varchar(100) NOT NULL,
  `mEmail` varchar(100) NOT NULL,
  `mPhone` varchar(100) NOT NULL,
  UNIQUE KEY `member_un` (`mId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES ('1','1','1','1'),('2','1','1','1'),('3','1','1','1'),('4','1','1','1'),('5','1','1','1'),('6','1','1','1'),('7','1','1','1'),('8','1','1','1'),('root','1234','1234','1234');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `mvId` int(11) NOT NULL AUTO_INCREMENT,
  `mvTitle` varchar(100) NOT NULL,
  `mvTime` varchar(100) NOT NULL,
  `mvSection` varchar(100) NOT NULL,
  `mvRating` double DEFAULT NULL,
  `mvSummary` longtext,
  `mvImg` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mvId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'스파이더맨','9,12,15','1,4,5',4.2,'<br>감독 : 존 왓츠 / 배우 : 톰 홀랜드 ,  젠데이아 콜먼 ,  베네딕트 컴버배치 ,  존 파브로 ,  제이콥 배덜런 ,  마리사 토메이 ,  알프리드 몰리나<br>장르 : 액션, 어드벤처, SF / 기본 : 12세 이상, 148분, 미국<br>개봉 : 2021.12.15<br><br>영화 <스파이더맨: 노 웨이 홈>은 정체가 탄로난 스파이더맨 \'피터 파커\'(톰 홀랜드)가 문제를 해결하기 위해 \'닥터 스트레인지\'(베네딕트 컴버배치)의 도움을 받던 중 뜻하지 않게 멀티버스가 열리게 되고,이를 통해 \'닥터 옥토퍼스\'(알프리드 몰리나) 등 각기 다른 차원의 숙적들이 나타나며 사상 최악의 위기를 맞게 되는 이야기를 그린 마블 액션 블록버스터.','https://img.cgv.co.kr/Movie/Thumbnail/Poster/000084/84949/84949_320.jpg'),(2,'언차티드','10,12,15','2,4,5',4.5,'<br>감독 : 루벤 플레셔 / 배우 : 톰 홀랜드 ,  마크 월버그 ,  소피아 알리 ,  타티 가브리엘 ,  안토니오 반데라스<br>장르 : 액션, 어드벤처 / 기본 : 12세 이상, 116분, 미국<br>개봉 : 2022.02.16<br><br>모든 것을 걸었다면 세상 누구보다 빠르게 찾아야 한다!<br>평범한 삶을 살던 ‘네이선’(톰 홀랜드)은 인생을 바꿀 뜻밖의 제안을 받는다.<br>그의 미션은 위험한 트레져 헌터 ‘설리’(마크 월버그)와 함께 사라진 형과 500년 전 잃어버린 천문학적인 가치를 지닌 트레져를 찾아내는 것.<br><br>그러나 몬카다(안토니오 반데라스)의 위협과 추격 속,<br>누구보다 빠르게 미지의 세계에 닿기 위해 결단을 내려야만 하는데…','https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85624/85624_320.jpg'),(3,'라라랜드','10','1,2,3',4.5,'시티옵스타스~','https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85672/85672_320.jpg'),(4,'안테벨룸','13,21','3,4,5',3.7,'<br>감독 : 제라드 부시 ,  크리스토퍼 렌즈 / 배우 : 자넬 모네 ,  잭 휴스턴 ,  지나 말론<br>장르 : 미스터리, 스릴러 / 기본 : 15세 이상, 105분, 미국<br>개봉 : 2022.02.23<br><br>그것이 당신을 지목했고,<br><br>아무도 당신을 구할 수 없다.<br><br>당신은 선택되었다.','https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85581/85581_320.jpg'),(7,'ㅁㄴㅇㄻㄴㅇㄹ','18,22','asdfasdf',5,'','https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85581/85581_320.jpg');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review` (
  `rId` int(11) NOT NULL AUTO_INCREMENT,
  `mId` varchar(100) NOT NULL,
  `mvId` int(11) NOT NULL,
  `rComment` varchar(100) NOT NULL,
  `rRating` int(11) NOT NULL,
  `mvImg` varchar(100) NOT NULL,
  PRIMARY KEY (`rId`),
  KEY `review_FK` (`mId`),
  CONSTRAINT `review_FK` FOREIGN KEY (`mId`) REFERENCES `member` (`mId`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (1,'1',1,'ㅁㄴㅇㄹ',4,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000084/84949/84949_320.jpg'),(2,'2',1,'ㅁㄴㅇㄹ',5,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000084/84949/84949_320.jpg'),(3,'3',1,'ㅁㄴㅇㄹ',3,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85672/85672_320.jpg'),(4,'4',4,'ㅁㄴㅇㄹ',4,'1'),(5,'5',5,'ㅁㄴㅇㄹ',4,'1'),(6,'6',2,'ㅁㄴㅇㄹ',4,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85624/85624_320.jpg'),(7,'7',2,'ㅁㄴㅇㄹ',3,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85624/85624_320.jpg'),(8,'8',3,'ㅁㄴㅇㄹ',3,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85672/85672_320.jpg'),(9,'root',1,'asdf',1,'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000084/84949/84949_320.jpg'),(13,'root',1,'qweqwerqer',1,'1.img'),(15,'root',1,'asdf',1,'1.img'),(16,'root',1,'피터죽음',1,'1.img'),(17,'root',1,'ㅁㄴㅇㄻㅇㄹㄹㅇㄹㅇㄹㅇㄹㅇㄹㅇ',1,'1.img'),(18,'root',1,'스파이더맨 짱인듯',1,'1.img');
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket` (
  `tId` int(11) NOT NULL AUTO_INCREMENT,
  `mId` varchar(100) NOT NULL,
  `mvId` int(11) NOT NULL,
  `tTime` varchar(100) NOT NULL,
  `tSection` varchar(100) DEFAULT NULL,
  `tSeat` int(11) DEFAULT NULL,
  PRIMARY KEY (`tId`),
  KEY `ticket_FK_1` (`mvId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (3,'kim',2,'10',NULL,1),(4,'root',1,'9',NULL,1),(6,'root',1,'9',NULL,2);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'movie'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-02 11:32:26
