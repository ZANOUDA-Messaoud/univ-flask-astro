/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.5.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: astro_db
-- ------------------------------------------------------
-- Server version	10.5.29-MariaDB-0+deb11u1

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
-- Table structure for table `appareil`
--

DROP TABLE IF EXISTS `appareil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `appareil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marque` varchar(50) DEFAULT NULL,
  `modele` varchar(50) DEFAULT NULL,
  `date_sortie` varchar(20) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `categorie` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appareil`
--

LOCK TABLES `appareil` WRITE;
/*!40000 ALTER TABLE `appareil` DISABLE KEYS */;
INSERT INTO `appareil` VALUES (1,'Canon','EOS 250D','2018',3,'Amateur'),(2,'Nikon','D3500','2018',3,'Amateur'),(3,'Sony','Alpha A6000','2014',3,'Amateur'),(4,'Canon','EOS 90D','2019',4,'Amateur sérieux'),(5,'Nikon','D7500','2016',4,'Amateur sérieux'),(6,'Sony','Alpha A6700','2023',4,'Amateur sérieux'),(7,'Canon','EOS R5','2020',5,'Professionnel'),(8,'Nikon','Z9','2021',5,'Professionnel'),(9,'Sony','Alpha A1','2021',5,'Professionnel'),(10,'Sony','Alpha A7 III','2018',5,'mirrorless'),(11,'Nikon','D850','2017',4,'DSLR'),(12,'Canon','EOS R6','2020',5,'mirrorless');
/*!40000 ALTER TABLE `appareil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(120) NOT NULL,
  `titre` varchar(120) NOT NULL,
  `description` text DEFAULT NULL,
  `date_upload` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `photo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo`
--

LOCK TABLES `photo` WRITE;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo` VALUES (1,'sample_0.jpg','Lune brillante','Belle photo de la lune en haute résolution','2026-04-17 15:02:45',1),(2,'sample_1.jpg','Orion','La constellation d\'Orion capturée avec mon télescope','2026-04-17 15:02:45',1),(3,'sample_2.jpg','Voie Lactée','Magnifique vue de la Voie Lactée au-dessus des montagnes','2026-04-17 15:02:45',2),(4,'sample_3.jpg','Éclipse Solaire','Éclipse solaire totale en grand-angle','2026-04-17 15:02:45',2);
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telescope`
--

DROP TABLE IF EXISTS `telescope`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `telescope` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marque` varchar(50) DEFAULT NULL,
  `modele` varchar(50) DEFAULT NULL,
  `date_sortie` varchar(20) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `categorie` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telescope`
--

LOCK TABLES `telescope` WRITE;
/*!40000 ALTER TABLE `telescope` DISABLE KEYS */;
INSERT INTO `telescope` VALUES (1,'Meade','Adventure Scope 40mm','2019',3,'Télescopes pour enfants'),(2,'National Geographic','50mm Refractor','2020',3,'Télescopes pour enfants'),(3,'Celestron','StarPointer 50mm','2018',3,'Télescopes pour enfants'),(4,'Celestron','NexStar 8SE','2014',4,'Automatisés'),(5,'Meade','LX90 GoTo','2015',4,'Automatisés'),(6,'Sky-Watcher','AllView CyberSynth','2021',4,'Automatisés'),(7,'Dobson','SkyQuest XT12','2015',5,'Télescopes complets'),(8,'Celestron','CPC 925','2016',5,'Télescopes complets'),(9,'Orion','SpaceProbe 260mm','2019',5,'Télescopes complets'),(10,'Sky-Watcher','Skymax 127','2016',4,'Maksutov-Cassegrain'),(11,'Orion','SkyQuest XT10','2015',5,'Dobsonian');
/*!40000 ALTER TABLE `telescope` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'mess','scrypt:32768:8:1$YxZ8MA8b4HsPKmBF$acd6ea053507965c57ef5b06f8020be7c0839fba09d2ac1a210a88419a6b816a75107c685a851f39a168226a5ee227394f44ab2f6eb749cf61e7f5a781b856aa'),(2,'astronome','scrypt:32768:8:1$B2AULtgoArt4tqSX$4fc801da5f74598fe0fbec98bd47ca2cdf13bfe8c749d5f66495beef6e8fb4b64dcf78471348b261d6e07f52282120e33d0e663c6a4cde311b5f5c17d44b79b5'),(3,'observateur','scrypt:32768:8:1$kNTAquMbGZb7cPCB$bc12bc8e221c2614422dd08b368a0b7d1ede92ebc21a84eb1960fc2a308e744bb32658903f355596b96c8272b54b31845e8509be0cd422b4698879bc97e885ba');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-17 15:19:53
