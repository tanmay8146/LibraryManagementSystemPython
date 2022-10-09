-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 09, 2022 at 01:25 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `libsysdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` varchar(11) NOT NULL,
  `f_name` varchar(32) NOT NULL,
  `l_name` varchar(32) NOT NULL,
  `address_one` varchar(56) NOT NULL,
  `address_two` varchar(56) NOT NULL,
  `post_code` varchar(16) NOT NULL,
  `mobile_no` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `f_name`, `l_name`, `address_one`, `address_two`, `post_code`, `mobile_no`) VALUES
('00', 'Tanmay', 'Sarkar', 'Siliguri', 'West Bengal', '734013', '6294181848'),
('01', 'Priya', 'Mrug', 'Coochbehar', 'West Bengal', '736101', '7047918278'),
('02', 'Anuj', 'Ghosh', 'Siliguri', 'West Bengal', '734011', '7679885140'),
('03', 'Meghdeep', 'Dutta', 'Jalpaiguri', 'West Bengal', '735224', '6295368851');

-- --------------------------------------------------------

--
-- Table structure for table `bookshelf`
--

CREATE TABLE `bookshelf` (
  `bookid` varchar(10) NOT NULL,
  `bookname` varchar(64) DEFAULT NULL,
  `authorname` varchar(32) DEFAULT NULL,
  `edition` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dbcli_login`
--

CREATE TABLE `dbcli_login` (
  `id` varchar(11) DEFAULT NULL,
  `f_name` varchar(32) NOT NULL,
  `login_id` varchar(16) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dbcli_login`
--

INSERT INTO `dbcli_login` (`id`, `f_name`, `login_id`, `password`) VALUES
('02', 'Anuj Ghosh', 'anujghosh', '5252'),
('03', 'Meghdeep Dutta', 'meghdeepdutta', '7171'),
('01', 'Priya Mrug', 'priyamrug', '8181'),
('00', 'Tanmay Sarkar', 'tanmayxd', 'blue81');

-- --------------------------------------------------------

--
-- Table structure for table `lecturers`
--

CREATE TABLE `lecturers` (
  `tch_id` varchar(11) NOT NULL,
  `f_name` varchar(32) DEFAULT NULL,
  `l_name` varchar(32) DEFAULT NULL,
  `address_one` varchar(56) DEFAULT NULL,
  `address_two` varchar(56) DEFAULT NULL,
  `post_code` varchar(16) DEFAULT NULL,
  `mobile_no` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lecturers`
--

INSERT INTO `lecturers` (`tch_id`, `f_name`, `l_name`, `address_one`, `address_two`, `post_code`, `mobile_no`) VALUES
('00', 'Ratnankur', 'Majumdar', 'Siliguri', 'West Bengal', '734011', '9832085378'),
('01', 'Debarati', 'Maitra', 'Siliguri', 'West Bengal', '734011', '9832072707'),
('02', 'Antara', 'Parai', 'Jalpaiguri', 'West Bengal', '735135', '9830520231'),
('03', 'Nilanjan', 'Das', 'Siliguri', 'West Bengal', '734012', '9733658418'),
('04', 'Tumpa', 'Banerjee', 'Siliguri', 'West Bengal', '734012', '9883057767'),
('05', 'Mrinal', 'Das', 'Siliguri', 'West Bengal', '734017', '9832350155'),
('06', 'Rubi', 'Ghosh', 'Siliguri', 'West Bengal', '734019', '8918924194');

-- --------------------------------------------------------

--
-- Table structure for table `lib`
--

CREATE TABLE `lib` (
  `member` varchar(16) NOT NULL,
  `prn_id` int(11) NOT NULL,
  `id` varchar(11) NOT NULL,
  `f_name` varchar(32) NOT NULL,
  `l_name` varchar(32) NOT NULL,
  `address_one` varchar(56) NOT NULL,
  `address_two` varchar(56) NOT NULL,
  `post_code` varchar(16) NOT NULL,
  `mobile_no` varchar(16) NOT NULL,
  `book_id` varchar(16) NOT NULL,
  `book_title` varchar(56) NOT NULL,
  `author` varchar(56) NOT NULL,
  `date_borrowed` varchar(56) NOT NULL,
  `date_due` varchar(56) NOT NULL,
  `days_on_book` varchar(16) NOT NULL,
  `late_return_fine` varchar(16) NOT NULL,
  `date_overdue` varchar(16) NOT NULL,
  `final_price` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lib`
--

INSERT INTO `lib` (`member`, `prn_id`, `id`, `f_name`, `l_name`, `address_one`, `address_two`, `post_code`, `mobile_no`, `book_id`, `book_title`, `author`, `date_borrowed`, `date_due`, `days_on_book`, `late_return_fine`, `date_overdue`, `final_price`) VALUES
('Admin', 202200, '00', 'Tanmay', 'Sarkar', 'Siliguri', 'West Bengal', '734013', '6294181848', 'B002', 'Introduction to Machine Learning with Python', 'Andreas Muller', '2022-10-06 09:37:17.836837', '2022-10-21 09:37:17.836837', '15', 'Rs. 100', 'NULL', 'Rs. 1000'),
('Admin', 202201, '1', 'Priya', 'Mrug', 'Coochbehar', 'West Bengal', '736101', '7047918278', 'B008', 'Machine Learning for Dummies', 'John Paul Mueller', '2022-10-08 16:33:11.191986', '2022-10-23 16:33:11.191986', '15', 'Rs. 90', 'NULL', 'Rs. 1900'),
('Admin', 202202, '02', 'Anuj', 'Ghosh', 'Siliguri', 'West Bengal', '734011', '7679885140', 'B007', 'Effective Java', 'Joshua Bloch', '2022-10-04 01:42:21.746083', '2022-10-19 01:42:21.746083', '15', 'Rs. 40', 'NULL', 'Rs. 1700'),
('Admin', 202203, '03', 'Meghdeep', 'Dutta', 'Jalpaiguri', 'West Bengal', '735224', '6295368851', 'B005', 'Data Science For Dummies', 'Lillian Pierson', '2022-10-04 01:43:24.732867', '2022-10-19 01:43:24.732867', '15', 'Rs. 90', 'NULL', 'Rs. 1100'),
('Student', 202204, '45', 'Niladri', 'Paul', 'Siliguri', 'West Bengal', '734101', '7407959932', 'B006', 'Brief History of Time', 'Stephen Hawking', '2022-10-05 11:56:08.793061', '2022-10-20 11:56:08.793061', '15', 'Rs. 150', 'NULL', 'Rs. 2100'),
('Student', 202205, '7', 'Deep', 'Sengupta', 'Siliguri', 'West Bengal', '734101', '6295000007', 'B003', 'Head First C', 'Dawn Griffiths', '2022-10-05 14:37:34.043690', '2022-10-20 14:37:34.043690', '15', 'Rs. 29', 'NULL', 'Rs. 1600'),
('Lecturer', 202206, '1', 'Debarati', 'Maitra', 'Siliguri', 'West Bengal', '734011', '9832072707', 'B003', 'Head First C', 'Dawn Griffiths', '2022-10-06 09:39:29.716322', '2022-10-21 09:39:29.716322', '15', 'Rs. 29', 'NULL', 'Rs. 1600');

-- --------------------------------------------------------

--
-- Table structure for table `librarians`
--

CREATE TABLE `librarians` (
  `libr_id` int(11) NOT NULL,
  `f_name` varchar(32) DEFAULT NULL,
  `l_name` varchar(32) DEFAULT NULL,
  `lib_dept` varchar(16) DEFAULT NULL,
  `address_one` varchar(56) DEFAULT NULL,
  `address_two` varchar(56) DEFAULT NULL,
  `post_code` varchar(16) DEFAULT NULL,
  `mobile_no` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `librarians`
--

INSERT INTO `librarians` (`libr_id`, `f_name`, `l_name`, `lib_dept`, `address_one`, `address_two`, `post_code`, `mobile_no`) VALUES
(901, 'Aditya', 'Sharma', 'Central', 'Siliguri', 'West Bengal', '734012', '7098770701'),
(902, 'Rajdeep', 'Mohanta', 'BBA', 'Siliguri', 'West Bengal', '734017', '7098770899'),
(903, 'Tamal', 'Sarkar', 'BBA', 'Siliguri', 'West Bengal', '734011', '7098770509'),
(904, 'Priyam', 'Biswas', 'BCA', 'Siliguri', 'West Bengal', '734011', '7098810588');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `st_id` varchar(11) NOT NULL,
  `f_name` varchar(32) DEFAULT NULL,
  `l_name` varchar(32) DEFAULT NULL,
  `dept` varchar(16) DEFAULT NULL,
  `address_one` varchar(56) DEFAULT NULL,
  `address_two` varchar(56) DEFAULT NULL,
  `post_code` varchar(16) DEFAULT NULL,
  `mobile_no` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`st_id`, `f_name`, `l_name`, `dept`, `address_one`, `address_two`, `post_code`, `mobile_no`) VALUES
('01', 'Gourab', 'Mitra', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000001'),
('02', 'Binita', 'Das', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000002'),
('03', 'Turjya', 'Roy', 'BCA', 'Kaliyaganj', 'West Bengal', '733129', '6295000003'),
('04', 'Subrat', 'Rajak', 'BCA', 'Haldia', 'West Bengal', '721602', '6295000004'),
('05', 'Shrestha', 'Nandi', 'BCA', 'Maldah', 'West Bengal', '732101', '6295000005'),
('06', 'Ritika', 'Chetri', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000006'),
('07', 'Deep', 'Sengupta', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000007'),
('08', 'Arup', 'Mandal', 'BCA', 'Murshidabad', 'West Bengal', '742149', '6295000008'),
('09', 'Arsalan', 'Rasul', 'BCA', 'Darjeeling', 'West Bengal', '734105', '6295000009'),
('10', '', '', '', '', '', '', ''),
('11', 'Kumari', 'Pranaya', 'BCA', 'Patna', 'Bihar', '800001', '6295000011'),
('12', 'Koushik', 'Roy', 'BCA', 'Jalpaiguri', 'West Bengal', '735121', '6295000012'),
('13', 'Bibek', 'Bagchi', 'BCA', 'Kaliyaganj', 'West Bengal', '733129', '6295000013'),
('14', 'Shibasish', 'Sharmadhikary', 'BCA', 'Jalpaiguri', 'West Bengal', '735135', '6295000014'),
('15', 'Prasandoj', 'Rai', 'BCA', 'Kolkata', 'West Bengal', '700013', '6295000015'),
('16', 'Aneek', 'Chomu', 'BCA', 'Bagdogra', 'West Bengal', '734014', '7098536899'),
('17', 'Rajdeep', 'Banik', 'BCA', 'Siliguri', 'West Bengal', '734405', '6295000017'),
('18', 'Anup', 'Majumdar', 'BCA', 'Maldah', 'West Bengal', '732101', '6295000018'),
('19', 'Amit', 'Sarkar', 'BCA', 'Tufanganj', 'West Bengal', '736159', '6295000019'),
('20', 'Arghyadip', 'Sarkar', 'BCA', 'Howrah', 'West Bengal', '700006', '6295000020'),
('21', 'Bishal', 'Saha', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000021'),
('22', 'Nandini', 'Majumder', 'BCA', 'Siliguri', 'West Bengal', '734104', '6295000022'),
('23', 'Nishita', 'Singh Sardar', 'BCA', 'Kurseong', 'West Bengal', '734203', '6295000023'),
('24', 'Reek', 'Saha', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000024'),
('25', 'Sanglap', 'Dutta', 'BCA', 'Jalpaiguri', 'West Bengal', '735135', '6295000025'),
('26', 'Sirsha', 'Mitra', 'BCA', 'Siliguri', 'West Bengal', '734105', '6295000026'),
('27', 'Nikhil', 'Kumar Bhagat', 'BCA', 'Murshidabad', 'West Bengal', '742149', '6295000027'),
('28', '', '', '', '', '', '', ''),
('29', 'Amlan', 'Mukherjee', 'BCA', 'Siliguri', 'West Bengal', '734107', '6295000029'),
('30', 'Akash', 'Sarkar', 'BCA', 'Tufanganj', 'West Bengal', '736159', '6295000030'),
('31', 'Anup', 'Roy', 'BCA', 'Darjeeling', 'West Bengal', '734110', '6295000031'),
('32', 'Anwesha', 'Bhowmick', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000032'),
('33', 'Parthib', 'Biswas', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000033'),
('34', 'Trishika', 'Prasad', 'BCA', 'Kolkata', 'West Bengal', '700001', '6295000034'),
('35', 'Sovitman', 'Poudel', 'BCA', 'Maldah', 'West Bengal', '732104', '6295000035'),
('36', 'Saumyadeep', 'Sangma', 'BCA', 'Coochbehar', 'West Bengal', '736103', '6295000036'),
('37', 'Debjeet', 'Sinha', 'BCA', 'Bagdogra', 'West Bengal', '73015', '6295000037'),
('38', 'Shiva', 'Kumar Pandit', 'BCA', 'Patna', 'Bihar', '800001', '6295000038'),
('39', 'Anikesh', 'Chettri', 'BCA', 'Kurseong', 'West Bengal', '734220', '6295000039'),
('40', 'Aditya', 'Ranjan', 'BCA', 'Sheohar', 'Bihar', '843329', '6295000040'),
('41', 'Rakesh', 'Halder', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000041'),
('42', 'Kabir', 'Chowdhury', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000042'),
('43', 'Uchchas', 'Saha', 'BCA', 'Chopra', 'West Bengal', '733216', '6295000043'),
('44', 'Tushar', 'Pradhan', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000044'),
('45', 'Niladri', 'Paul', 'BCA', 'Siliguri', 'West Bengal', '734101', '7047959932'),
('46', 'Tanmay', 'Sarkar', 'BCA', 'Siliguri', 'West Bengal', '734013', '6294181848'),
('47', 'Preet', 'Agarwala', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000047'),
('48', 'Swarnadeep', 'Majumder', 'BCA', 'Siliguri', 'West Bengal', '734101', '6295000048'),
('49', 'Sudipta', 'Bhowmik', 'BCA', 'Chopra', 'West Bengal', '733216', '6295000049'),
('50', 'Subhra', 'Sarkar', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000050'),
('51', 'Subhasish', 'Sarkar', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000051'),
('52', 'Anuj', 'Ghosh', 'BCA', 'Siliguri', 'West Bengal', '734011', '7679885140'),
('53', 'Subham', 'Paul', 'BCA', 'Siliguri', 'West Bengal', '734012', '6295000053'),
('54', 'Asmita', 'Sen', 'BCA', 'Siliguri', 'West Bengal', '734011', '6295000054'),
('55', 'Subhamay', 'Debnath', 'BCA', 'Chopra', 'West Bengal', '733216', '6295000055'),
('56', 'Statha', 'Paul', 'BCA', 'Siliguri', 'West Bengal', '734011', '6295000056'),
('57', 'Akash', 'Mahanta', 'BCA', 'Kaliyaganj', 'West Bengal', '733129', '6295000057'),
('58', 'Abhishek', 'Sinha', 'BCA', 'Kishanganj', 'Bihar', '855107', '6295000058'),
('59', 'Souvik', 'Saha', 'BCA', 'Siliguri', 'West Bengal', '734014', '6295000059'),
('60', 'Siddhant', 'Chettri', 'BCA', 'Gangtok', 'Sikkim', '737135', '6295000060'),
('61', 'Sayak', 'Chakraborty', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000061'),
('62', 'Aratrika', 'Roy', 'BCA', 'Jalpaiguri', 'West Bengal', '735134', '6295000062'),
('63', 'Santosh', 'Chettri', 'BCA', 'Darjeeling', 'West Bengal', '734001', '6295000063'),
('64', 'Arbaab', 'Rehman Khan', 'BCA', 'Islampur', 'West Bengal', '733203', '6295000064'),
('65', 'Sanskar', 'Giri', 'BCA', 'Kurseong', 'West Bengal', '734203', '6295000065'),
('66', 'Antarip', 'Dey', 'BCA', 'Siliguri', 'West Bengal', '734011', '6295000066'),
('67', 'Samrat', 'Goshwami', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000067'),
('68', 'Pallab', 'Dutta', 'BCA', 'Islampur', 'West Bengal', '733202', '6295000068'),
('69', 'Samadreeta', 'Mukherjee', 'BCA', 'Siliguri', 'West Bengal', '734011', '6295000069'),
('70', 'Sabyasachi', 'Roy Chowdhury', 'BCA', 'Jalpaiguri', 'West Bengal', '735135', '6295000070'),
('71', 'Meghdeep', 'Dutta', 'BCA', 'Jalpaiguri', 'West Bengal', '735224', '6295368851'),
('72', 'Rajasree', 'Baruri', 'BCA', 'Siliguri', 'West Bengal', '734013', '6295000072'),
('73', 'Megha', 'Singha Roy', 'BCA', 'Oodlabari', 'West Bengal', '735222', '6295000073'),
('74', 'Ritam', 'Kumar Kundu', 'BCA', 'Raiganj', 'West Bengal', '733134', '6295000074'),
('75', 'Jhony', 'Roy', 'BCA', 'Jalpaiguri', 'West Bengal', '735134', '6295000075'),
('76', 'Goldi', 'Ranjan', 'BCA', 'Sheohar', 'Bihar', '843329', '6295000076'),
('77', 'Rajendra', 'Nath Murmu', 'BCA', 'Kaliyaganj', 'West Bengal', '733129', '6295000077'),
('78', 'Dippriya', 'Sarkar', 'BCA', 'Kaliyaganj', 'West Bengal', '733129', '6295000078'),
('79', 'Debratan', 'Mandal', 'BCA', 'Siliguri', 'West Bengal', '734016', '6295000079'),
('80', 'Priyangshu', 'Bhowmick', 'BCA', 'Siliguri', 'West Bengal', '734016', '6295000080'),
('81', 'Priya', 'Mrug', 'BCA', 'Coochbehar', 'West Bengal', '736101', '7047918278'),
('82', 'Debopriyo', 'Ghosh', 'BCA', 'Siliguri', 'West Bengal', '734019', '6295000082');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookshelf`
--
ALTER TABLE `bookshelf`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `dbcli_login`
--
ALTER TABLE `dbcli_login`
  ADD PRIMARY KEY (`login_id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `lecturers`
--
ALTER TABLE `lecturers`
  ADD PRIMARY KEY (`tch_id`);

--
-- Indexes for table `lib`
--
ALTER TABLE `lib`
  ADD PRIMARY KEY (`prn_id`);

--
-- Indexes for table `librarians`
--
ALTER TABLE `librarians`
  ADD PRIMARY KEY (`libr_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`st_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dbcli_login`
--
ALTER TABLE `dbcli_login`
  ADD CONSTRAINT `dbcli_login_ibfk_1` FOREIGN KEY (`id`) REFERENCES `admins` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
