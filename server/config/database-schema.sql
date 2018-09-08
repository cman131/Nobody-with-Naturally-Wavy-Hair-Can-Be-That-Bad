CREATE TABLE `Deck` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `Deck_Card` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `deckid` bigint(20) NOT NULL,
  `cardid` varchar(100) NOT NULL,
  `count` int(20) DEFAULT 1 NOT NULL,
  PRIMARY KEY (`id`)
 ) Engine=InnoDB DEFAULT CHARSET utf8;
CREATE TABLE `Side_Card` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `deckid` bigint(20) NOT NULL,
  `cardid` varchar(100) NOT NULL,
  `count` int(20) DEFAULT 1 NOT NULL,
  PRIMARY KEY (`id`)
 ) Engine=InnoDB DEFAULT CHARSET utf8;
CREATE TABLE `Card` (
  `id` varchar(100) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL,
  `imageUrl` varchar(250) DEFAULT NULL,
  `cmc` bigint(10) DEFAULT NULL,
  `power`  varchar(250) DEFAULT NULL,
  `toughness` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) Engine=InnoDB DEFAULT CHARSET utf8;
