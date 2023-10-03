-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: serviceprovider4
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `servicemen`
--

DROP TABLE IF EXISTS `servicemen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicemen` (
  `id` int NOT NULL,
  `age` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `serviceId` int NOT NULL,
  `contactNumber` varchar(50) NOT NULL,
  `available` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicemen`
--

LOCK TABLES `servicemen` WRITE;
/*!40000 ALTER TABLE `servicemen` DISABLE KEYS */;
INSERT INTO `servicemen` VALUES (1,30,'Manny Friedman',1,'5368990861','0'),(2,42,'Benyamin Grimsdell',1,'7701815003','1'),(3,36,'Shem Gantz',1,'4007798421','1'),(4,48,'Orin Valsler',1,'6066256882','1'),(5,31,'Nolana Bidgood',1,'9512940126','0'),(6,34,'Reyna Balling',1,'4104958398','1'),(7,32,'Berne Di Frisco',1,'7654089173','1'),(8,40,'Lynette Harlick',1,'3806903911','1'),(9,31,'Lucie Humbee',1,'8715578628','1'),(10,42,'Benedick Creamen',1,'4646128068','1'),(11,33,'Rab Antoshin',1,'4744159922','1'),(12,39,'Nanete Carlson',1,'7578682176','1'),(13,31,'Lynne Spiers',1,'1582923623','1'),(14,42,'Adelaide Dondon',1,'8552235152','1'),(15,42,'Caryl Darben',1,'5933972885','0'),(16,47,'Clerc Lindstedt',1,'3746108675','1'),(17,45,'Brady Elsey',1,'4691727595','1'),(18,48,'Avery Coupman',1,'3147579224','1'),(19,42,'Cecil Killen',1,'6296376593','1'),(20,36,'Glennis Gagen',1,'4275488975','0');
/*!40000 ALTER TABLE `servicemen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29 20:51:03
