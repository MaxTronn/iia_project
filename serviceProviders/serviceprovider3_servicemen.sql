-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: serviceprovider3
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
INSERT INTO `servicemen` VALUES (1,34,'Lucas McNickle',5,'1529569721','1'),(2,49,'Ginny Spataro',4,'4569230478','1'),(3,35,'Ogdon Diamant',2,'4934968746','1'),(4,40,'Faulkner Derobert',5,'7196201308','0'),(5,39,'Marcelia Simmans',6,'5651301557','0'),(6,43,'Osmond Farnall',1,'8146129324','0'),(7,27,'Dannie Shafto',3,'5863344323','0'),(8,33,'Kennett McIleen',3,'6738863386','1'),(9,42,'Edvard De Beauchamp',5,'4908560582','0'),(10,31,'Sherrie Pickavance',1,'8134975237','1'),(11,34,'Judon Oscroft',4,'9004087305','0'),(12,50,'Sharai Thumim',3,'6083320645','0'),(13,34,'Shaun Howkins',5,'8323759197','0'),(14,34,'Blakelee Royston',1,'3658558296','1'),(15,47,'Rhodie Giamo',5,'7904087745','0'),(16,31,'Kynthia Jolin',2,'4046368129','1'),(17,41,'Paulita Tibalt',2,'3396658394','1'),(18,25,'Brooke Cochrane',4,'9272399380','0'),(19,43,'Hank Mettricke',1,'6087471983','1'),(20,31,'Chad Sahlstrom',2,'2017516921','0'),(21,39,'Sarette Fosserd',1,'6419575302','1'),(22,40,'Annabel Arkil',6,'6337887767','1'),(23,39,'Bryn Lympany',4,'3537053349','0'),(24,42,'Jackquelin Zorzini',3,'3802234152','1'),(25,45,'Gaelan Ruddiman',2,'4309337819','0'),(26,25,'Chip Woolcocks',1,'9623763229','1'),(27,33,'Brina Zecchinelli',1,'4948454847','1'),(28,47,'Kynthia Cardow',6,'5616238238','0'),(29,39,'Carita Aldersey',5,'1812009786','1'),(30,44,'Borden Towndrow',3,'7548358881','1'),(31,49,'Stephenie Chevers',5,'8098317258','0'),(32,30,'Granger Bisco',1,'9401174512','0'),(33,28,'Hirsch Raitie',5,'3086387841','0'),(34,29,'Sidnee Knibbs',5,'4579759263','0'),(35,40,'Elnora McCurrie',3,'6356123298','0'),(36,26,'Inness Backsal',6,'7372508235','1'),(37,41,'Raynell Berrigan',1,'5514821588','1'),(38,50,'Ysabel Egginson',3,'8206177996','0'),(39,49,'Cob Lupson',2,'5274636415','0'),(40,25,'Burnard Whiff',3,'9996113917','0'),(41,39,'Wilie Frazer',1,'9858376293','1'),(42,45,'Dalia Ozelton',4,'2115454969','0'),(43,41,'Tracy Morigan',3,'3155588648','1'),(44,50,'Colline Bourcq',2,'9613928263','1'),(45,45,'Dyana Tattersall',3,'1173473815','1'),(46,37,'Marybelle Hagston',2,'5658843855','0'),(47,44,'Daune Makinson',2,'5954570999','1'),(48,35,'Merle Maccaddie',5,'8567893510','1'),(49,47,'Tierney Grigor',5,'2796479554','0'),(50,32,'Rois McGrath',4,'8154159185','0'),(51,46,'Dore Moral',2,'8437002480','0'),(52,41,'Elinore Shoemark',3,'9271907593','1'),(53,41,'Pail Kleinhausen',6,'7802560524','0'),(54,42,'Bertha Grewar',2,'6528701833','0'),(55,49,'Esdras Fey',3,'5103390998','1'),(56,39,'Janela Dudney',1,'6868696178','1'),(57,29,'Ara Sydry',4,'6143573228','0'),(58,32,'Dani Tuny',4,'3174428670','0'),(59,26,'Claudine Haxley',3,'3161111647','0'),(60,28,'Anneliese Elgey',6,'7775078949','1'),(61,43,'Baudoin Dyne',4,'2253940499','1'),(62,28,'Henderson Bayless',4,'8436707190','0'),(63,45,'Margeaux Loiterton',5,'2212552665','0'),(64,45,'Pietra Sawdy',1,'5098134923','1'),(65,43,'Fidelio Doddrell',4,'9092457291','1'),(66,29,'Windy Tattam',5,'3728593771','0'),(67,31,'Anna-diana Maron',1,'3947315181','0'),(68,41,'Shannon Tuck',4,'2608842285','1'),(69,46,'Lesley Mildenhall',2,'2929503602','1'),(70,44,'Jorey Powner',3,'3836623388','0'),(71,31,'Raimund Dring',2,'1042014545','1'),(72,39,'Tiphani Bean',2,'1898320488','0'),(73,41,'Nico Pygott',6,'7952318777','0'),(74,31,'Hymie Drever',1,'5362443388','0'),(75,33,'Obadiah Hadleigh',2,'8917990635','1'),(76,35,'Clevey Bosward',5,'5446729322','1'),(77,50,'Alexandro Blockwell',3,'2575304192','0'),(78,33,'Dalis Chapelhow',2,'5924962513','1'),(79,46,'Chaddy Blazynski',6,'7022914920','1'),(80,49,'Michaelina Guiot',3,'8818494912','0');
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
