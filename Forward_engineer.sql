-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema employee_managment_system
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema employee_managment_system
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `employee_managment_system` ;
USE `employee_managment_system` ;

-- -----------------------------------------------------
-- Table `employee_managment_system`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employee_managment_system`.`employee` (
  `emp_id` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(45) NOT NULL,
  `lname` VARCHAR(45) NOT NULL,
  `location` VARCHAR(100) NOT NULL,
  `phone1` VARCHAR(100) NOT NULL,
  `phone2` VARCHAR(45) NULL,
  `sex` VARCHAR(1) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `pass` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`emp_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `employee_managment_system`.`leave`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employee_managment_system`.`leave` (
  `leave_id` INT NOT NULL AUTO_INCREMENT,
  `employee_emp_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `reason` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`leave_id`),
  INDEX `fk_leave_employee_idx` (`employee_emp_id` ASC) VISIBLE,
  CONSTRAINT `fk_leave_employee`
    FOREIGN KEY (`employee_emp_id`)
    REFERENCES `employee_managment_system`.`employee` (`emp_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `employee_managment_system`.`department`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employee_managment_system`.`department` (
  `dep_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `salary_range` VARCHAR(255) NULL,
  `description` LONGTEXT NULL,
  PRIMARY KEY (`dep_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `employee_managment_system`.`salary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employee_managment_system`.`salary` (
  `salary_id` INT NOT NULL AUTO_INCREMENT,
  `amount` INT NULL,
  `bounes` INT NULL,
  `annual` DATE NULL,
  `overtime` DOUBLE NULL,
  `department_dep_id` INT NOT NULL,
  PRIMARY KEY (`salary_id`),
  INDEX `fk_salary_department1_idx` (`department_dep_id` ASC) VISIBLE,
  CONSTRAINT `fk_salary_department1`
    FOREIGN KEY (`department_dep_id`)
    REFERENCES `employee_managment_system`.`department` (`dep_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `employee_managment_system`.`payroll`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employee_managment_system`.`payroll` (
  `payroll_id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `report` LONGTEXT NULL,
  `total_amount` INT NOT NULL,
  `employee_emp_id` INT NOT NULL,
  `leave_leave_id` INT NOT NULL,
  `salary_salary_id` INT NOT NULL,
  `department_dep_id` INT NOT NULL,
  PRIMARY KEY (`payroll_id`),
  INDEX `fk_payroll_employee1_idx` (`employee_emp_id` ASC) VISIBLE,
  INDEX `fk_payroll_leave1_idx` (`leave_leave_id` ASC) VISIBLE,
  INDEX `fk_payroll_salary1_idx` (`salary_salary_id` ASC) VISIBLE,
  INDEX `fk_payroll_department1_idx` (`department_dep_id` ASC) VISIBLE,
  CONSTRAINT `fk_payroll_employee1`
    FOREIGN KEY (`employee_emp_id`)
    REFERENCES `employee_managment_system`.`employee` (`emp_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_payroll_leave1`
    FOREIGN KEY (`leave_leave_id`)
    REFERENCES `employee_managment_system`.`leave` (`leave_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_payroll_salary1`
    FOREIGN KEY (`salary_salary_id`)
    REFERENCES `employee_managment_system`.`salary` (`salary_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_payroll_department1`
    FOREIGN KEY (`department_dep_id`)
    REFERENCES `employee_managment_system`.`department` (`dep_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
