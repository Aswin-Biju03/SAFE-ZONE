/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - disaster_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`disaster_management` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `disaster_management`;

/*Table structure for table `accomodation` */

DROP TABLE IF EXISTS `accomodation`;

CREATE TABLE `accomodation` (
  `accomodation_id` int(11) NOT NULL AUTO_INCREMENT,
  `camps_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`accomodation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `accomodation` */

insert  into `accomodation`(`accomodation_id`,`camps_id`,`name`,`phone`,`email`,`image`) values 
(1,1,'hajiraaaaa','8965326963','hajira@gmail.com','static/image/49ac18a2-5613-40a1-96da-d4ac2d806f1aabc.jpg');

/*Table structure for table `camps` */

DROP TABLE IF EXISTS `camps`;

CREATE TABLE `camps` (
  `camps_id` int(11) NOT NULL AUTO_INCREMENT,
  `place_id` int(11) DEFAULT NULL,
  `camp_name` varchar(100) DEFAULT NULL,
  `place_details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`camps_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `camps` */

insert  into `camps`(`camps_id`,`place_id`,`camp_name`,`place_details`) values 
(1,3,'camp 1','fully filled'),
(2,4,'camp 2','partially filled');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` varchar(100) DEFAULT NULL,
  `reciver_id` varchar(100) DEFAULT NULL,
  `chats` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`reciver_id`,`chats`,`date`) values 
(1,'19','18','hai','2024-11-26'),
(2,'19','20','Hai','2024-11-26'),
(3,'22','23','hi ','2024-11-27'),
(4,'22','23','heyy','2024-11-27'),
(5,'22','23','helloi','2024-11-27'),
(6,'23','22','helloi','2024-11-27'),
(7,'23','22','dod','2024-11-27'),
(8,'23','22','helloi','2024-11-27'),
(9,'23','22','hhff','2024-11-27'),
(10,'23','22','can\'t ','2024-11-27'),
(11,'23','22','rithinroy27@gmail.com','2024-11-27'),
(12,'22','23','ok okki','2024-11-27'),
(13,'22','23','heyy','2024-11-27'),
(14,'22','23','hello','2024-11-30');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`reply`,`date`) values 
(1,24,'no water','pending','2024-11-27'),
(2,24,'can\'t','pending','2024-11-27'),
(3,25,'hai','pending','2024-11-30'),
(4,25,'helloi','pending','2024-11-30'),
(5,1,'heyy','solved\r\n','2024-11-30');

/*Table structure for table `counseling_details` */

DROP TABLE IF EXISTS `counseling_details`;

CREATE TABLE `counseling_details` (
  `counselingdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `counselindsection_id` int(11) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`counselingdetails_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `counseling_details` */

/*Table structure for table `counseling_sections` */

DROP TABLE IF EXISTS `counseling_sections`;

CREATE TABLE `counseling_sections` (
  `counselingsection_id` int(11) NOT NULL AUTO_INCREMENT,
  `accomodation_id` int(11) DEFAULT NULL,
  `counsilor_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`counselingsection_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `counseling_sections` */

/*Table structure for table `counselors` */

DROP TABLE IF EXISTS `counselors`;

CREATE TABLE `counselors` (
  `counselors_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`counselors_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `counselors` */

insert  into `counselors`(`counselors_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,4,'anandhu','p','1','12','rithin@gmail.com'),
(2,13,'navin','benny','ekjwhjv','4546135611','rithin@gmail.com');

/*Table structure for table `disasters` */

DROP TABLE IF EXISTS `disasters`;

CREATE TABLE `disasters` (
  `disasters_id` int(11) NOT NULL AUTO_INCREMENT,
  `parameters` varchar(100) DEFAULT NULL,
  `disaster` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`disasters_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `disasters` */

/*Table structure for table `emergency` */

DROP TABLE IF EXISTS `emergency`;

CREATE TABLE `emergency` (
  `emergency_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `emergency_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `emergency` */

insert  into `emergency`(`emergency_id`,`login_id`,`emergency_name`,`phone`,`email`) values 
(8,17,'police','100','police@gmail.com');

/*Table structure for table `emergency_situations` */

DROP TABLE IF EXISTS `emergency_situations`;

CREATE TABLE `emergency_situations` (
  `esituation_id` int(11) NOT NULL AUTO_INCREMENT,
  `place_id` int(11) DEFAULT NULL,
  `situdation` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`esituation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `emergency_situations` */

insert  into `emergency_situations`(`esituation_id`,`place_id`,`situdation`,`date`,`status`,`latitude`,`longitude`,`reply`) values 
(1,4,'no issues','2024-11-27','inactive','0','0','issue solved'),
(2,4,'nothing','2024-11-27','inactive','20','25','solved'),
(3,4,'fhsnm','2024-11-30','inactive','20','12','ga'),
(4,3,'sgcjg','2024-11-30','vbjkj','12','14','pending'),
(5,3,'landslide','2024-11-30','inactive','0','0','pending'),
(6,3,'illness','2024-11-30','active','0','0','pending'),
(7,4,'water rising ','2024-11-30','active','0','0','pending'),
(8,3,'earthquake ','2024-11-30','active','0','0','pending');

/*Table structure for table `free_space` */

DROP TABLE IF EXISTS `free_space`;

CREATE TABLE `free_space` (
  `freespace_id` int(11) NOT NULL AUTO_INCREMENT,
  `camps_id` int(11) DEFAULT NULL,
  `freespace` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`freespace_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `free_space` */

insert  into `free_space`(`freespace_id`,`camps_id`,`freespace`) values 
(1,2,'4'),
(2,1,'8'),
(3,3,'10');

/*Table structure for table `helpfulness` */

DROP TABLE IF EXISTS `helpfulness`;

CREATE TABLE `helpfulness` (
  `helpfulness_id` int(11) NOT NULL AUTO_INCREMENT,
  `issue_id` int(11) DEFAULT NULL,
  `helpfulness` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`helpfulness_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `helpfulness` */

/*Table structure for table `image` */

DROP TABLE IF EXISTS `image`;

CREATE TABLE `image` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `issue_id` int(11) DEFAULT NULL,
  `images` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `image` */

insert  into `image`(`image_id`,`issue_id`,`images`) values 
(1,1,'static/image/d600421b-f935-4cb5-a822-4c37335a23daabc.jpg'),
(2,1,'static/image/2564e251-c2d9-4c88-b3b7-8c6357cd799fabc.jpg'),
(3,1,'static/image/1cc79930-9394-495e-9ccc-6cb02cca0372abc.jpg'),
(4,1,'static/image/f25dbfa2-9145-4ed9-92a0-0215335d0e01abc.jpg');

/*Table structure for table `issues` */

DROP TABLE IF EXISTS `issues`;

CREATE TABLE `issues` (
  `issue_id` int(11) NOT NULL AUTO_INCREMENT,
  `place_id` varchar(100) DEFAULT NULL,
  `issue` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`issue_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `issues` */

insert  into `issues`(`issue_id`,`place_id`,`issue`,`date`,`status`) values 
(1,'3','no curren','2024-11-27','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(17,'police','12345','emergency'),
(4,'anandhu','anandhu@1234A','counselor'),
(20,'jerin','Jerin@1234','volunteer_head'),
(18,'rahul','Rahul123@','volunteer_head'),
(25,'haliya','haliya','user'),
(24,'vivek','vivek','user'),
(19,'manu','Manu@1234','volunteer_head'),
(10,'hiiikl','Asdfg1234@','emergency'),
(11,'wbsvhbwj','1234Asdfg','emergency'),
(13,'wjgyjh','wiuheuA1234','counselor'),
(23,'manum','12345','volunteer'),
(22,'joseph','1234','volunteer');

/*Table structure for table `messages` */

DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `reciver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `messages` */

/*Table structure for table `needs` */

DROP TABLE IF EXISTS `needs`;

CREATE TABLE `needs` (
  `needs_id` int(11) NOT NULL AUTO_INCREMENT,
  `camp_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `needs` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`needs_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `needs` */

insert  into `needs`(`needs_id`,`camp_id`,`type`,`needs`,`details`) values 
(1,1,'cloth','jeans','urgent'),
(2,1,'cloth','jeans','not urgent');

/*Table structure for table `needs_arrangements` */

DROP TABLE IF EXISTS `needs_arrangements`;

CREATE TABLE `needs_arrangements` (
  `needsarrange_id` int(11) NOT NULL AUTO_INCREMENT,
  `needs_id` int(11) DEFAULT NULL,
  `arrangements` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`needsarrange_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `needs_arrangements` */

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `notifications` */

/*Table structure for table `person_issues` */

DROP TABLE IF EXISTS `person_issues`;

CREATE TABLE `person_issues` (
  `personissues_id` int(11) NOT NULL AUTO_INCREMENT,
  `accomodation_id` int(11) DEFAULT NULL,
  `issues` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`personissues_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `person_issues` */

insert  into `person_issues`(`personissues_id`,`accomodation_id`,`issues`) values 
(1,1,'no drinking water'),
(2,3,'cbcjcbx');

/*Table structure for table `place` */

DROP TABLE IF EXISTS `place`;

CREATE TABLE `place` (
  `place_id` int(11) NOT NULL AUTO_INCREMENT,
  `place` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`place_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `place` */

insert  into `place`(`place_id`,`place`,`details`) values 
(3,'elavoor','near to angamali'),
(4,'kakanad','ernakulam');

/*Table structure for table `update_emergency_situations` */

DROP TABLE IF EXISTS `update_emergency_situations`;

CREATE TABLE `update_emergency_situations` (
  `updesitaution_id` int(11) NOT NULL AUTO_INCREMENT,
  `esituation_id` int(11) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `images` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`updesitaution_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `update_emergency_situations` */

insert  into `update_emergency_situations`(`updesitaution_id`,`esituation_id`,`details`,`date`,`images`) values 
(1,2,'nice','2024-11-27','static/image/0742b95b-c99b-4f12-86d7-437ff1d63b5aabc.jpg'),
(2,2,'niceee','2024-11-27','static/image/77fb930a-8422-4484-b70b-d45f98cee512abc.jpg'),
(3,1,'gdgs','2024-11-30','static/image/0bc45ef0-5086-42f3-a1b0-064cb819347babc.jpg');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,25,'hal','iyan','fshj','1236546789','haliyan@gmail.com');

/*Table structure for table `volunteer` */

DROP TABLE IF EXISTS `volunteer`;

CREATE TABLE `volunteer` (
  `volunteer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `place_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`volunteer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `volunteer` */

insert  into `volunteer`(`volunteer_id`,`login_id`,`place_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(6,23,4,'manu','josy','kakanad','5555555555','manu@gmail.com'),
(5,22,4,'joseph','k','kakanad','7388092292','joseph@gmail.com');

/*Table structure for table `volunteer_head` */

DROP TABLE IF EXISTS `volunteer_head`;

CREATE TABLE `volunteer_head` (
  `vhead_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `place_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vhead_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `volunteer_head` */

insert  into `volunteer_head`(`vhead_id`,`login_id`,`place_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(5,19,3,'manuew','josyen','elavoor','3793892823','manuew@gmail.com'),
(4,18,4,'rahul','p','kakanad','4546135611','rahul@gamil.com'),
(6,20,4,'jerin','james','kakanad','5555555555','jerin@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
