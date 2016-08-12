/*
SQLyog Community v12.2.4 (32 bit)
MySQL - 10.1.13-MariaDB : Database - my_cart
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`my_cart` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `my_cart`;

/*Table structure for table `dataitem` */

DROP TABLE IF EXISTS `dataitem`;

CREATE TABLE `dataitem` (
  `wish_id` bigint(30) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(30) unsigned NOT NULL,
  `wish_name` varchar(20) NOT NULL,
  `wish_price` double NOT NULL,
  `wish_date` datetime DEFAULT NULL,
  PRIMARY KEY (`wish_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `dataitem` */

insert  into `dataitem`(`wish_id`,`user_id`,`wish_name`,`wish_price`,`wish_date`) values 
(1,7,'I-Phone',64.99,'2016-07-30 22:25:42'),
(7,7,'I-Phone',64.99,'2016-07-31 12:40:49'),
(8,7,'Laptop',250.99,'2016-07-31 12:52:00'),
(9,7,'Keyboard',40.99,'2016-07-31 12:52:03'),
(10,7,'Apple Desktop',949.99,'2016-07-31 12:52:07'),
(11,7,'Smart Watch',239.99,'2016-07-31 12:52:10'),
(12,7,'Mouse',10.99,'2016-07-31 12:52:13');

/*Table structure for table `user_tbl` */

DROP TABLE IF EXISTS `user_tbl`;

CREATE TABLE `user_tbl` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_username` varchar(45) NOT NULL,
  `user_email` varchar(45) NOT NULL,
  `user_password` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=Aria AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 PAGE_CHECKSUM=1;

/*Data for the table `user_tbl` */

insert  into `user_tbl`(`user_id`,`user_username`,`user_email`,`user_password`) values 
(8,'D','d@d.com','123'),
(7,'C','c@c.com','123'),
(9,'E','e@e.com','123'),
(10,'F','f@f.com','123'),
(11,'G','g@g.com','123');

/* Procedure structure for procedure `sp_createUser` */

/*!50003 DROP PROCEDURE IF EXISTS  `sp_createUser` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    IF ( SELECT EXISTS (SELECT 1 FROM tbl_user WHERE user_email = p_username) ) THEN
     
        SELECT 'Username Exists !!';
     
    ELSE
     
        INSERT INTO tbl_user
        (
            user_username,
            user_email,
            user_password
        )
        VALUES
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END */$$
DELIMITER ;

/* Procedure structure for procedure `sp_GetWishByUser` */

/*!50003 DROP PROCEDURE IF EXISTS  `sp_GetWishByUser` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_GetWishByUser`(
    IN p_userid BIGINT)
BEGIN
	SELECT * FROM dataitem WHERE user_id = p_userid;
    END */$$
DELIMITER ;

/* Procedure structure for procedure `_addwish` */

/*!50003 DROP PROCEDURE IF EXISTS  `_addwish` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `_addwish`(IN p_userid BIGINT , IN p_wishname VARCHAR(15) , IN p_price DOUBLE)
BEGIN
	INSERT INTO dataitem(
        user_id,
        wish_name,
        wish_price,
        wish_date
	)
	VALUES
	(
        p_userid,
        p_wishname,
        p_price,
        NOW()
	);
    END */$$
DELIMITER ;

/* Procedure structure for procedure `_createuser` */

/*!50003 DROP PROCEDURE IF EXISTS  `_createuser` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `_createuser`(IN p_username VARCHAR(30),IN p_useremail VARCHAR(35), IN p_password VARCHAR(20) )
BEGIN

	IF ( SELECT EXISTS (SELECT 1 FROM user_tbl WHERE user_email = p_useremail) ) THEN
     
		SELECT 'Username Exists !!';
        ELSE
		
	INSERT INTO user_tbl
        (
            user_username,
            user_email,
            user_password
        )
        VALUES
        (
            p_username,
            p_useremail,
            p_password
        );
     
    END IF;


    END */$$
DELIMITER ;

/* Procedure structure for procedure `_validloginId` */

/*!50003 DROP PROCEDURE IF EXISTS  `_validloginId` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `_validloginId`(IN p_useremail VARCHAR(20) )
BEGIN
	SELECT * FROM user_tbl WHERE user_email = p_useremail;	
    END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
