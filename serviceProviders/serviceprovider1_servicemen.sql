-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: serviceprovider1
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
  `contact` varchar(50) NOT NULL,
  `availability` varchar(12) NOT NULL,
  `workExp` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicemen`
--

LOCK TABLES `servicemen` WRITE;
/*!40000 ALTER TABLE `servicemen` DISABLE KEYS */;
INSERT INTO `servicemen` VALUES (1,41,'Ree Alvaro',3,'9935911391','notAvailable',3),(2,29,'Dimitry Leetham',9,'2504172822','available',5),(3,46,'Pauli McKeady',9,'2987070612','available',7),(4,48,'Shepard Siret',10,'6389935926','available',7),(5,43,'Norene Felipe',5,'7238400488','available',10),(6,37,'Benoit Coultard',6,'3141252038','available',7),(7,42,'Lothario Jerrold',8,'8004363724','notAvailable',1),(8,40,'Kennan Martinie',1,'3764758275','notAvailable',2),(9,31,'Consuela Edwin',2,'5788301986','available',10),(10,41,'Faustine Jeanesson',9,'2369174629','available',4),(11,28,'Waldemar Feldberger',10,'7059734763','available',6),(12,32,'Marne Byllam',10,'6076056156','available',6),(13,35,'Emelina Landal',4,'4445415131','notAvailable',10),(14,42,'Dewey Bails',2,'3576844900','notAvailable',1),(15,28,'Cynde Liven',9,'1541553767','available',10),(16,37,'Atlante Meeke',5,'1124748102','notAvailable',9),(17,42,'Kirstyn Spragg',8,'6587420497','notAvailable',9),(18,47,'Malissia Nelsey',9,'2555588975','notAvailable',4),(19,30,'Ash Enright',5,'4801176691','notAvailable',5),(20,26,'Adrien Wishkar',7,'1661875555','available',7),(21,28,'Lela Rushmere',1,'8706122944','available',5),(22,45,'Hubey Mellor',1,'2293726666','notAvailable',3),(23,31,'Clarabelle Myatt',2,'8161808274','available',3),(24,37,'Marlene Houdhury',11,'9235307136','available',8),(25,49,'Crista Saunter',7,'1831877393','notAvailable',4),(26,41,'Kessia Simmons',2,'8109844081','available',9),(27,42,'Janeta Wodeland',6,'4726442811','notAvailable',2),(28,40,'Brynna Gradwell',6,'8119318075','notAvailable',4),(29,49,'Deana Brittan',2,'2401464109','available',8),(30,37,'Austine Kondrat',2,'5643393819','available',9),(31,40,'Harli Blackway',6,'6007579711','notAvailable',6),(32,48,'Winni Bolding',8,'9401996306','notAvailable',7),(33,38,'Elinor Turland',7,'1238237256','available',7),(34,40,'Bird Keysall',7,'6129051323','available',10),(35,39,'Maggy Bengtson',3,'9594739460','available',8),(36,27,'Wilhelmine Kelson',6,'1148350661','notAvailable',2),(37,36,'Jackson Craven',7,'4301635743','available',4),(38,30,'Alberik Thomazin',5,'9335915459','notAvailable',5),(39,36,'Aldous Swiffen',2,'1549308463','notAvailable',8),(40,38,'Cosetta Markl',5,'1358100740','notAvailable',3),(41,28,'Keith Alexsandrowicz',5,'9662665418','notAvailable',10),(42,42,'Fidelio Narbett',6,'5248270481','notAvailable',5),(43,39,'Delmar Choupin',6,'8362544826','notAvailable',5),(44,35,'Ashlan Gooley',9,'1675239225','available',9),(45,33,'Drusi Glede',5,'4743098236','available',6),(46,47,'Bondy Radnage',2,'2559422578','notAvailable',6),(47,25,'Maison Tessington',8,'2212200700','available',8),(48,38,'Glyn Sheach',10,'2632016455','notAvailable',4),(49,43,'Reynolds Beric',6,'6682401744','available',5),(50,41,'Bogart Tarn',6,'7328008877','notAvailable',1),(51,26,'Perkin Kerley',6,'8193060924','available',7),(52,43,'Trina Moresby',5,'1996989474','available',3),(53,38,'Amabelle Gordon-Giles',8,'9807511671','notAvailable',3),(54,50,'Gus Wollacott',11,'1256242134','available',7),(55,37,'Chrissy Myers',2,'7111377768','notAvailable',9),(56,49,'Korry Merigot',1,'1578817940','available',7),(57,26,'Tally Eisold',2,'4346967023','available',2),(58,49,'Myriam Dearth',11,'6723107129','available',9),(59,39,'Mabelle Aimer',10,'7786484083','available',8),(60,40,'Dru Dog',7,'7955811052','notAvailable',5),(61,48,'Lyman Gutowska',9,'1437073590','available',5),(62,29,'Alvan Earingey',2,'1468591365','notAvailable',7),(63,39,'Bryan MacDowall',6,'8601695316','available',2),(64,25,'Sybilla McTeer',4,'3084462933','notAvailable',1),(65,46,'Tiffi Baird',1,'8391710448','available',2),(66,48,'Abram Jeannin',10,'3805039882','available',4),(67,47,'Allistir Seamen',8,'1834805158','available',4),(68,34,'Phil Luggar',5,'9833348953','notAvailable',6),(69,33,'Lola Keeble',9,'2991190701','available',7),(70,47,'Bryce McClarence',4,'9279260956','available',6),(71,46,'Brittani Clewer',6,'6795722719','notAvailable',4),(72,46,'Garnette Heams',2,'5734364545','available',1),(73,32,'Correy Clipston',1,'7186812479','available',2),(74,42,'Cherise Carney',8,'3544695046','available',1),(75,29,'Heida Seviour',9,'2422779700','notAvailable',1),(76,45,'Sven Keenan',10,'8327044803','notAvailable',1),(77,39,'Suzanne Dainton',11,'4834772844','available',4),(78,39,'Jessey Chavey',1,'7835902896','notAvailable',9),(79,43,'Basia Kupker',9,'9737336334','notAvailable',2),(80,50,'Violet Manicom',4,'1567723816','available',7),(81,32,'Caldwell Peagrim',3,'8715842438','notAvailable',3),(82,40,'Foster Derr',6,'5504482438','notAvailable',7),(83,44,'Archer Eardley',3,'4475258058','available',9),(84,45,'Munmro Tollit',6,'6163552210','available',5),(85,33,'Vivi Discombe',3,'8543516604','available',4),(86,32,'Stephenie Winward',3,'3007513464','notAvailable',8),(87,25,'Lonny Ander',11,'9241492657','notAvailable',4),(88,29,'Donica Hanley',8,'4966369377','available',2),(89,42,'Iggie Gegg',1,'4723067699','available',6),(90,31,'Donny Canniffe',7,'4318559889','notAvailable',9),(91,47,'Milt Bisson',11,'5177009321','notAvailable',3),(92,32,'Portie Woollaston',5,'2109572023','notAvailable',3),(93,40,'Norrie Dullard',3,'6363845862','notAvailable',4),(94,42,'Lorant Clausewitz',7,'9625129902','notAvailable',9),(95,27,'Cortney Mabbett',8,'1093198820','available',1),(96,28,'Arlina McOrkil',8,'2832706771','notAvailable',2),(97,46,'Ailey Barsby',10,'4409275624','available',6),(98,39,'Lukas Cracknall',11,'3224781960','notAvailable',4),(99,31,'Quincy Kulver',10,'5035388285','notAvailable',8),(100,29,'Vivien Iacoboni',10,'2101976754','notAvailable',1);
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
