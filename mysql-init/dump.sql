-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hospitalmanagementsystem
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int NOT NULL,
  `doctor_id` int NOT NULL,
  `appointment_date` datetime NOT NULL,
  `purpose` text,
  PRIMARY KEY (`appointment_id`),
  KEY `doctor_id` (`doctor_id`),
  KEY `appointments_ibfk_1` (`patient_id`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`) ON DELETE CASCADE,
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (9,14,7,'2024-04-25 18:53:00','Routine Checkup'),(10,9,8,'2023-11-01 10:00:00','Consultation'),(11,10,9,'2023-11-01 11:00:00','Follow-up Visit'),(12,11,10,'2023-11-01 12:00:00','Annual Physical Exam'),(13,12,7,'2023-11-02 09:00:00','Vaccination'),(14,13,8,'2023-11-02 10:00:00','Health Screening'),(15,14,9,'2023-11-02 11:00:00','Routine Checkup'),(16,15,10,'2023-11-02 12:00:00','Consultation'),(17,16,7,'2023-11-03 09:00:00','Follow-up Visit'),(18,17,8,'2023-11-03 10:00:00','Annual Physical Exam'),(19,18,9,'2023-11-03 11:00:00','Vaccination'),(20,19,10,'2023-11-03 12:00:00','Health Screening'),(21,9,7,'2024-04-27 21:19:00','Check Up'),(22,19,10,'2024-05-08 13:14:00','Post Check Up');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `billing`
--

DROP TABLE IF EXISTS `billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billing` (
  `bill_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `bill_date` date NOT NULL,
  `payment_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`bill_id`),
  KEY `billing_ibfk_1` (`patient_id`),
  CONSTRAINT `billing_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing`
--

LOCK TABLES `billing` WRITE;
/*!40000 ALTER TABLE `billing` DISABLE KEYS */;
INSERT INTO `billing` VALUES (5,8,200.00,'2023-10-01','Paid'),(6,9,300.00,'2023-10-02','Pending'),(7,8,150.00,'2023-10-01','Paid'),(8,9,300.00,'2023-10-01','Pending'),(9,10,200.00,'2023-10-02','Pending'),(10,11,250.00,'2023-10-02','Paid'),(11,12,180.00,'2023-10-03','Paid'),(12,13,220.00,'2023-10-03','Paid'),(13,14,140.00,'2023-10-04','Pending'),(14,15,350.00,'2023-10-04','Paid'),(15,16,400.00,'2023-10-05','Pending'),(16,17,190.00,'2023-10-05','Pending'),(17,18,210.00,'2023-10-06','Paid'),(18,19,330.00,'2023-10-06','Pending');
/*!40000 ALTER TABLE `billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `specialty` varchar(255) NOT NULL,
  `contact_info` varchar(255) DEFAULT NULL,
  `room_number` varchar(50) DEFAULT NULL,
  `availability` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`),
  FULLTEXT KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (7,'Dr. Alice Johnson','Cardiology','555-1010','Room 101','Weekdays 9 AM to 5 PM'),(8,'Dr. Bob Lee','Pediatrics','555-2020','Room 202','Weekdays 10 AM to 6 PM'),(9,'Dr. Clara Zhou','Orthopedics','555-3030','Room 303','Weekdays 8 AM to 4 PM'),(10,'Dr. David Kim','Neurology','555-4040','Room 404','Weekdays 7 AM to 3 PM');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(50) NOT NULL,
  `contact_info` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `emergency_contact_name` varchar(255) DEFAULT NULL,
  `emergency_contact_phone` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  FULLTEXT KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (8,'John Doe','1980-07-10','Male','555-0123','123 Elm St, Yourtown','johndoe@example.com','Jane Doe','555-0124'),(9,'Jane Smith','1992-11-30','Female','555-5678','456 Oak St, Othertown','janesmith@example.com','John Smith','555-5679'),(10,'Alice Johnson','1982-03-15','Female','555-0101','100 Main St, New City','alice.johnson@example.com','Carol Johnson','555-0102'),(11,'Bob Smith','1975-07-20','Male','555-0201','200 Oak St, Old Town','bob.smith@example.com','Tom Smith','555-0202'),(12,'Carmen Lopez','1990-11-30','Female','555-0301','300 Pine St, Lakeside','carmen.lopez@example.com','Maria Lopez','555-0302'),(13,'David Tan','1988-01-25','Male','555-0401','400 Cedar St, Hillcrest','david.tan@example.com','Susan Tan','555-0402'),(14,'Eva Patel','1995-05-17','Female','555-0501','500 Elm St, Riverside','eva.patel@example.com','Anil Patel','555-0502'),(15,'Frank Wu','1978-09-12','Male','555-0601','600 Birch St, Sunnyvale','frank.wu@example.com','Lily Wu','555-0602'),(16,'Grace Kim','1985-12-09','Female','555-0701','700 Maple St, Westwood','grace.kim@example.com','James Kim','555-0702'),(17,'Henry O\'Neill','1980-04-22','Male','555-0801','800 Spruce St, Eastside','henry.oneill@example.com','Emma O\'Neill','555-0802'),(18,'Isla Santos','1993-02-13','Female','555-0901','900 Pine St, Northgate','isla.santos@example.com','Jose Santos','555-0902'),(19,'Jake Lee','1986-06-18','Male','555-1001','1000 Willow St, Southbank','jake.lee@example.com','Anna Lee','555-1002'),(20,'Dakota Wagner','2024-04-23','Male','6617448698','123 Maple Ave','wagner@gmail.com','Samantha L Longtin','6613336666');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-02 20:41:54