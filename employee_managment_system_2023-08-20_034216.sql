-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: employee_managment_system
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `dep_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `salary_range` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb3_unicode_ci,
  PRIMARY KEY (`dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (4,'Data Analysis Professional','500-100','sssaaaaa'),(5,'Data Analysis Professional','5000-10000','Data Analysis Professional'),(6,'Data Analysis Professional','5000-10000','Data Analysis Professional'),(7,'aaaaaa',NULL,NULL),(8,'Inserted KWRGS','1000-500','adasda'),(9,'Inserted KWRGS',NULL,'adasda');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) COLLATE utf8mb3_unicode_ci NOT NULL,
  `lname` varchar(45) COLLATE utf8mb3_unicode_ci NOT NULL,
  `location` varchar(100) COLLATE utf8mb3_unicode_ci NOT NULL,
  `phone1` varchar(100) COLLATE utf8mb3_unicode_ci NOT NULL,
  `phone2` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `sex` varchar(1) COLLATE utf8mb3_unicode_ci NOT NULL,
  `email` varchar(45) COLLATE utf8mb3_unicode_ci NOT NULL,
  `password` varchar(45) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (2,'Menna','Mohamed','new Cairo','01216545645',NULL,'F','Menna@gmail.com','123'),(4,'qqq','Doe','London','0123456789',NULL,'M','john.doe@gmail.com','456'),(5,'eee','Mohamed','New Cairo','01065216622',NULL,'M','zidan@gmail.com','123'),(6,'UPDATEEEEEEE','KhaledUPDATE','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','123'),(7,'eee','Mohamed','New Cairo','01065216622',NULL,'M','zidan@gmail.com','123'),(8,'qqq','Doe','London','0123456789',NULL,'M','john.doe@gmail.com','456'),(9,'Mahmoud','Khaled','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','123'),(10,'Mahmoud','Khaled','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','1233'),(11,'Mahmoud','Khaled','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','1111'),(12,'Mahmoud','Khaled','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','11'),(13,'flask','Khaled','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','22'),(14,'SSSS','Khaled','Cairo','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','123'),(15,'Mahmoud','Khaled','XXXXX','+201065216442',NULL,'M','mahmoudkhaledwork07@gmail.com','123');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;

--
-- Table structure for table `leave`
--

DROP TABLE IF EXISTS `leave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leave` (
  `leave_id` int NOT NULL AUTO_INCREMENT,
  `employee_emp_id` int DEFAULT NULL,
  `date` date NOT NULL,
  `reason` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`leave_id`),
  KEY `fk_leave_employee_idx` (`employee_emp_id`),
  CONSTRAINT `fk_leave_employee` FOREIGN KEY (`employee_emp_id`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave`
--

/*!40000 ALTER TABLE `leave` DISABLE KEYS */;
INSERT INTO `leave` VALUES (6,6,'2045-09-25','ESA','Sick'),(7,2,'2023-02-23','Sick','Sick'),(8,2,'2023-02-23','Sick','Sick'),(9,2,'2023-02-23','Sick','Sick'),(10,2,'2023-02-23','Sick','Sick'),(11,2,'2023-02-23','Sick','Sick'),(12,2,'2023-02-23','Sick','Sick'),(13,NULL,'2045-09-25','Sick',''),(14,4,'2045-09-25',NULL,NULL);
/*!40000 ALTER TABLE `leave` ENABLE KEYS */;

--
-- Table structure for table `payroll`
--

DROP TABLE IF EXISTS `payroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payroll` (
  `payroll_id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `report` longtext COLLATE utf8mb3_unicode_ci,
  `total_amount` int NOT NULL,
  `employee_emp_id` int DEFAULT NULL,
  `leave_leave_id` int DEFAULT NULL,
  `salary_salary_id` int DEFAULT NULL,
  `department_dep_id` int DEFAULT NULL,
  PRIMARY KEY (`payroll_id`),
  KEY `fk_payroll_employee1_idx` (`employee_emp_id`),
  KEY `fk_payroll_leave1_idx` (`leave_leave_id`),
  KEY `fk_payroll_salary1_idx` (`salary_salary_id`),
  KEY `fk_payroll_department1_idx` (`department_dep_id`),
  CONSTRAINT `fk_payroll_department1` FOREIGN KEY (`department_dep_id`) REFERENCES `department` (`dep_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_payroll_employee1` FOREIGN KEY (`employee_emp_id`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_payroll_leave1` FOREIGN KEY (`leave_leave_id`) REFERENCES `leave` (`leave_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_payroll_salary1` FOREIGN KEY (`salary_salary_id`) REFERENCES `salary` (`salary_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payroll`
--

/*!40000 ALTER TABLE `payroll` DISABLE KEYS */;
INSERT INTO `payroll` VALUES (5,'2021-01-01','Report1',100,2,6,4,5),(6,'2022-01-01','Report2',55555555,4,7,4,4),(7,'2023-01-01','Report3',300,2,6,4,4),(8,'2024-01-01','Report4',400,2,8,5,5),(9,'2025-01-01','Report5',500,2,6,6,4),(10,'2026-01-01','Report6',600,2,6,5,5),(11,'2027-01-01','Report7',700,2,6,4,4),(12,'2028-01-01','Report8',800,2,6,4,5),(13,'2029-01-01','Report9',900,2,6,5,4),(14,'2020-01-01','Report1',100,2,NULL,NULL,NULL),(15,'2021-01-01','Report2',200,2,NULL,NULL,NULL),(16,'2022-01-01','Report3',300,2,NULL,NULL,NULL),(17,'2023-01-01','Report4',400,2,NULL,NULL,NULL),(18,'2024-01-01','Report5',500,2,NULL,NULL,NULL),(19,'2025-01-01','Report6',600,2,NULL,NULL,NULL),(20,'2026-01-01','Report7',700,2,NULL,NULL,NULL),(21,'2027-01-01','Report8',800,2,NULL,NULL,NULL),(22,'2028-01-01','Report9',900,2,NULL,NULL,NULL),(23,'2029-01-01','Report10',1000,2,NULL,NULL,NULL),(24,'2045-09-25','sadadasdasdasd',555,NULL,NULL,5,6),(25,'2045-09-25',NULL,33,5,NULL,5,5);
/*!40000 ALTER TABLE `payroll` ENABLE KEYS */;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `salary_id` int NOT NULL AUTO_INCREMENT,
  `amount` int DEFAULT NULL,
  `bounes` int DEFAULT NULL,
  `annual` date DEFAULT NULL,
  `overtime` double DEFAULT NULL,
  `department_dep_id` int NOT NULL,
  PRIMARY KEY (`salary_id`),
  KEY `fk_salary_department1_idx` (`department_dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (4,11111,300,'2023-03-02',3.5,2),(5,4000,400,'2023-04-02',4.5,2),(6,5000,500,'2023-05-02',5.5,2),(7,6000,600,'2023-06-02',6.5,2),(8,7000,700,'2023-07-02',7.5,2),(9,8000,800,'2023-08-02',8.5,2),(10,9000,900,'2023-09-02',9.5,2),(11,10000,1000,'2023-10-02',10.5,2),(12,222,111,NULL,21,3),(13,222,111,NULL,21,3),(14,222,111,'2022-09-06',21,3),(15,222,NULL,NULL,NULL,7);
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;

--
-- Dumping routines for database 'employee_managment_system'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-20  3:42:22
