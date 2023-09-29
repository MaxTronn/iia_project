-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: serviceprovider2
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
  `FullName` varchar(50) NOT NULL,
  `serviceId` int NOT NULL,
  `contactNumner` varchar(50) NOT NULL,
  `isAvailable` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicemen`
--

LOCK TABLES `servicemen` WRITE;
/*!40000 ALTER TABLE `servicemen` DISABLE KEYS */;
INSERT INTO `servicemen` VALUES (1,35,'Van Postgate',7,'9925653647','no'),(2,25,'Laure Classen',5,'4233097739','yes'),(3,34,'Maxie Scain',2,'6611772901','yes'),(4,29,'Liane Lubomirski',2,'2498907889','yes'),(5,49,'Bree Ciobotaro',2,'1283153323','no'),(6,37,'Carroll Splevin',1,'9371471640','no'),(7,29,'Ferdie Blackwood',3,'1331199711','no'),(8,30,'Ewart Penny',1,'2996551493','yes'),(9,50,'Denni Ilewicz',3,'4997521842','no'),(10,28,'Eada Goundry',2,'1181694051','yes'),(11,45,'Nils Wyrill',4,'2626498355','no'),(12,35,'Link Allport',2,'3454340770','no'),(13,42,'Keary Fintoph',7,'8747310603','yes'),(14,28,'Dean Bardill',6,'3455653653','no'),(15,38,'Anestassia Beed',7,'1097800172','yes'),(16,48,'Katti Paolone',7,'8899726591','no'),(17,32,'Anetta Hattiff',1,'6229738417','no'),(18,48,'Lyndsay Spedroni',2,'4016193702','yes'),(19,27,'Darcy Endacott',4,'8811336495','yes'),(20,32,'Bogart Sutehall',6,'8386410225','yes'),(21,50,'Shawn Burndred',7,'5205704046','no'),(22,47,'Peg Winram',5,'4425122041','yes'),(23,40,'Celesta Jeremiah',5,'5999446514','yes'),(24,31,'Lance Putley',5,'9199119104','no'),(25,49,'Emmalynne Crannis',5,'1239532906','no'),(26,44,'Janessa Piscotti',1,'2425318420','no'),(27,28,'Rodrigo Tolworthy',4,'8224672835','yes'),(28,29,'Tarrance Ferrieri',7,'1541989899','yes'),(29,50,'Filmer Batteson',1,'2654568652','no'),(30,44,'Andrei Gehricke',6,'6484388252','yes'),(31,38,'Pietrek Stener',3,'2625817603','no'),(32,33,'Uta Gross',2,'5792402223','yes'),(33,43,'Shaine Steiner',4,'6846532394','no'),(34,40,'Chaunce Claypole',2,'7573942651','yes'),(35,42,'Alvy Bartoszinski',2,'7686273728','yes'),(36,25,'Niels Smylie',6,'1727035761','yes'),(37,45,'Kirbee Glendza',4,'5755115997','no'),(38,34,'Cad Torre',4,'9763584985','yes'),(39,31,'Kristan Costen',5,'6149940490','yes'),(40,43,'Hillary Milesop',1,'3209012107','no'),(41,27,'Liza Creamer',2,'7214344856','no'),(42,45,'Evan Tankus',3,'8956263268','no'),(43,25,'Gussie Node',6,'6783942434','no'),(44,34,'Dru Barnhill',6,'7412061395','no'),(45,41,'Tades Peploe',3,'4108206627','yes'),(46,26,'Sigmund Abbiss',7,'9414338230','yes'),(47,49,'Sasha Pedroni',3,'6365568982','yes'),(48,34,'Olimpia Beran',7,'1746190956','yes'),(49,26,'Tremain Sargison',1,'7965703582','no'),(50,49,'Nanete Hazelgreave',2,'9675111426','no'),(51,41,'Di Smallcombe',2,'7441993349','no'),(52,25,'Clary Moffet',7,'5116516515','yes'),(53,32,'Fields Fall',6,'9958892753','no'),(54,40,'Jamaal Joontjes',6,'8912200549','yes'),(55,30,'Langsdon Sphinxe',6,'9884096421','no'),(56,35,'Valli Combe',3,'7194342117','yes'),(57,49,'Pascale Ambrogini',4,'1854091521','no'),(58,29,'Gabbey Gavrieli',6,'6243619616','no'),(59,45,'Wolf Surgeoner',3,'7055041546','yes'),(60,31,'Karoline Anstee',6,'2938421185','yes');
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

-- Dump completed on 2023-09-29 20:51:04
