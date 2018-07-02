CREATE TABLE `t_build_business_right` (
  `company_id` varchar(255) NOT NULL DEFAULT '',
  `right_type` varchar(100) DEFAULT NULL,
  `right_code` varchar(255) DEFAULT NULL,
  `right_name` varchar(255) DEFAULT NULL,
  `sign_time` datetime DEFAULT NULL,
  `effective_time` datetime DEFAULT NULL,
  `sign_org` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `t_build_main` (
  `company_id` varchar(255) NOT NULL DEFAULT '',
  `credit_code` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `company_person` varchar(50) DEFAULT NULL,
  `reg_type` varchar(50) DEFAULT NULL,
  `area` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `t_build_register` (
  `company_id` varchar(255) NOT NULL DEFAULT '',
  `name` varchar(50) DEFAULT NULL,
  `id_card` varchar(50) DEFAULT NULL,
  `reg_type` varchar(50) DEFAULT NULL,
  `reg_code` varchar(255) DEFAULT NULL,
  `reg_profession` varchar(50) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  KEY `index_name_company_id` (`name`,`company_id`,`id_card`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;