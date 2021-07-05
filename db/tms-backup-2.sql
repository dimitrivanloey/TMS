-- -------------------------------------------------------------
-- TablePlus 4.0.0(370)
--
-- https://tableplus.com/
--
-- Database: d5ajj12b9grk8
-- Generation Time: 2021-06-30 17:39:22.0010
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."unit_logs_enable_entry";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS unit_logs_enable_entry_id_seq;

-- Table Definition
CREATE TABLE "public"."unit_logs_enable_entry" (
    "id" int4 NOT NULL DEFAULT nextval('unit_logs_enable_entry_id_seq'::regclass),
    "date_added" timestamptz NOT NULL,
    "status" varchar(41) NOT NULL,
    "venue" varchar(18),
    "comments" text NOT NULL,
    "enable_id" int4 NOT NULL,
    CONSTRAINT "unit_logs_enable_ent_enable_id_a7d4566a_fk_unit_logs" FOREIGN KEY ("enable_id") REFERENCES "public"."unit_logs_enable"("id"),
    PRIMARY KEY ("id")
);

INSERT INTO "public"."unit_logs_enable_entry" ("id", "date_added", "status", "venue", "comments", "enable_id") VALUES
(5, '2021-01-06 15:21:21.267721+00', 'Failed Battery', 'Kempton Park', 'no lights', 62),
(6, '2021-01-06 15:43:54.350262+00', 'Stick', 'Kempton Park', '', 6),
(7, '2021-01-06 16:24:35.048938+00', 'Stick', 'Kempton Park', '', 39),
(8, '2021-01-06 17:19:51.837555+00', 'Missing', 'Kempton Park', '', 50),
(9, '2021-01-06 17:20:13.50247+00', 'Stick', 'Kempton Park', '', 55),
(10, '2021-01-06 17:48:36.835458+00', 'Stick', 'Kempton Park', '', 39),
(11, '2021-01-06 17:50:51.454283+00', 'Stick', 'Kempton Park', '', 61),
(12, '2021-01-06 18:21:46.236032+00', 'No Solid White', 'Kempton Park', '', 56),
(13, '2021-01-06 18:21:56.232051+00', 'No Solid White', 'Kempton Park', '', 57),
(14, '2021-01-07 11:25:27.991054+00', 'Connector Broken', 'Kempton Park', '', 64),
(15, '2021-01-07 11:39:45.104515+00', 'In Repair', 'Kempton Park', '', 57),
(16, '2021-01-08 09:07:47.349908+00', 'In Refurb - Send for mechanical repair', NULL, '', 89),
(17, '2021-01-13 20:07:05.573948+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 50),
(18, '2021-01-19 13:30:08.83497+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 6),
(19, '2021-01-19 13:30:27.146614+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 54),
(20, '2021-01-19 14:01:10.401182+00', 'On Course - Racing: Not to course', 'Exeter', '', 122),
(21, '2021-01-19 14:01:24.474099+00', 'On Course - Racing: Not to course', 'Exeter', '', 86),
(22, '2021-01-19 14:01:37.146595+00', 'On Course - Racing: Not to course', 'Exeter', '', 119),
(23, '2021-01-19 14:25:32.882308+00', 'On Course - Racing: Not to course', 'Exeter', '', 73),
(24, '2021-01-19 14:26:04.239355+00', 'On Course - Racing: Not to course', 'Exeter', '', 126),
(25, '2021-01-19 14:26:16.954348+00', 'On Course - Racing: Not to course', 'Exeter', '', 124),
(26, '2021-01-19 14:26:31.058443+00', 'On Course - Racing: Not to course', 'Exeter', '', 16),
(27, '2021-01-19 14:26:48.350397+00', 'On Course - Racing: Not to course', 'Exeter', '', 75),
(28, '2021-01-19 14:27:16.753807+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 45),
(29, '2021-01-19 14:28:00.456761+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 55),
(30, '2021-01-19 14:54:34.663886+00', 'On Course - Racing: Not to course', 'Exeter', '', 67),
(31, '2021-01-19 14:54:50.035172+00', 'On Course - Racing: Not to course', 'Exeter', '', 77),
(32, '2021-01-19 14:55:17.089392+00', 'On Course - Racing: Not to course', 'Exeter', '', 50),
(33, '2021-01-19 14:55:30.946373+00', 'On Course - Racing: Not to course', 'Exeter', '', 76),
(34, '2021-01-19 14:55:48.478215+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 20),
(35, '2021-01-19 14:56:06.5327+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 43),
(36, '2021-01-19 14:56:28.834318+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 6),
(37, '2021-01-19 14:56:48.038242+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 46),
(38, '2021-01-19 15:22:05.771544+00', 'On Course - Racing: Not to course', 'Exeter', '', 123),
(39, '2021-01-19 15:24:08.402485+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 29),
(40, '2021-01-19 15:55:08.788585+00', 'On Course - Racing: Not to course', 'Exeter', '', 97),
(41, '2021-01-19 15:55:20.604431+00', 'On Course - Racing: Not to course', 'Exeter', '', 122),
(42, '2021-01-19 15:55:42.996661+00', 'On Course - Racing: Not to course', 'Exeter', '', 86),
(43, '2021-01-20 13:01:11.965742+00', 'On Course - Racing: Not to course', 'Newbury', '', 50),
(44, '2021-01-20 13:02:16.143339+00', 'On Course - Racing: Not to course', 'Newbury', '', 67),
(45, '2021-01-20 13:34:32.688356+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 35),
(46, '2021-01-20 13:34:59.667622+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 88),
(47, '2021-01-20 14:08:14.570132+00', 'On Course - Racing: Not to course', 'Newbury', '', 127),
(48, '2021-01-20 14:09:03.876388+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 45),
(49, '2021-01-20 14:09:24.997909+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 43),
(50, '2021-01-20 14:09:39.245636+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 51),
(51, '2021-01-20 14:39:03.860679+00', 'On Course - Racing: Not to course', 'Newbury', '', 72),
(52, '2021-01-21 13:59:59.413423+00', 'On Course - Racing: Not to course', 'Wincanton', '', 121),
(53, '2021-01-21 14:01:19.877039+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 72),
(54, '2021-01-21 14:01:38.221203+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 6),
(55, '2021-01-21 14:29:13.164009+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 54),
(56, '2021-01-21 14:29:26.052355+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 37),
(57, '2021-01-21 15:03:12.645589+00', 'On Course - Racing: Not to course', 'Wincanton', '', 127),
(58, '2021-01-21 15:03:27.214655+00', 'On Course - Racing: Not to course', 'Wincanton', '', 123),
(59, '2021-01-21 15:04:11.948857+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 43),
(60, '2021-01-21 15:04:26.964651+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 39),
(61, '2021-01-25 16:56:15.114162+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 8),
(62, '2021-01-25 17:19:53.757125+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 54),
(63, '2021-01-25 18:47:57.68766+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 27),
(65, '2021-01-30 16:59:22.323929+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 86),
(66, '2021-01-30 17:37:08.138252+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 11),
(67, '2021-02-03 14:23:30.057803+00', 'In Refurb - Send for mechanical repair', 'Kempton Park', '', 54),
(68, '2021-02-04 09:50:00.691511+00', 'In Refurb - Send for mechanical repair', NULL, '', 45),
(69, '2021-02-04 09:59:16.730624+00', 'In Refurb - Send for mechanical repair', NULL, '', 72),
(70, '2021-02-04 12:38:13.625302+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 6),
(71, '2021-02-04 12:38:48.625508+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 32),
(72, '2021-02-04 12:39:19.562252+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 28),
(73, '2021-02-04 14:20:37.11764+00', 'On Course - Racing: Not to course', 'Wincanton', '', 73),
(74, '2021-02-04 14:27:00.064973+00', 'On Course - Racing: Not to course', 'Wincanton', '', 97),
(75, '2021-02-04 14:27:28.402359+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 39),
(76, '2021-02-04 14:28:04.803617+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 43),
(77, '2021-02-06 13:07:40.152255+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 126),
(78, '2021-02-06 13:07:54.013935+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 83),
(79, '2021-02-06 13:08:08.966407+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 116),
(80, '2021-02-06 13:22:07.654974+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 11),
(81, '2021-02-06 13:57:04.187484+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 55),
(83, '2021-02-06 14:48:48.993876+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 125),
(84, '2021-02-06 14:53:49.888308+00', 'On Course - Racing: Not to course', 'Sandown Park', '', 69),
(85, '2021-02-06 14:59:19.56803+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 46),
(86, '2021-02-09 17:20:45.200447+00', 'In Refurb - Send for mechanical repair', NULL, 'needs reflashing', 91),
(87, '2021-02-11 12:41:31.023286+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 50),
(88, '2021-02-11 12:42:02.738556+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 9),
(89, '2021-02-11 13:21:16.298843+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 127),
(90, '2021-02-11 14:13:55.960591+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 117),
(91, '2021-02-11 15:15:47.809551+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 77),
(92, '2021-02-11 15:16:22.907105+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 75),
(93, '2021-02-11 15:16:46.910675+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 97),
(94, '2021-02-18 12:39:56.743759+00', 'On Course - Racing: Not to course', 'Leicester', '', 127),
(95, '2021-02-18 13:37:01.150516+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 69),
(96, '2021-02-18 13:37:36.841097+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 25),
(128, '2021-02-19 13:12:20.245596+00', 'On Course - Test: No Solid White', 'Kelso', 'no lights', 85),
(129, '2021-02-19 15:31:01.120825+00', 'On Course - Racing: Stuck on track', 'Kelso', '', 126),
(130, '2021-02-20 12:37:43.353082+00', 'On Course - Test: No Solid White', 'Wincanton', '', 10),
(131, '2021-02-20 12:38:03.55589+00', 'On Course - Test: No Solid White', 'Wincanton', 'no lights', 46),
(132, '2021-02-20 12:38:23.555865+00', 'On Course - Test: No Solid White', 'Wincanton', 'no lights', 55),
(133, '2021-02-20 12:38:37.531731+00', 'On Course - Test: No Solid White', 'Wincanton', '', 123),
(134, '2021-02-20 12:39:04.364134+00', 'On Course - Test: No Solid White', 'Wincanton', 'no lights', 123),
(135, '2021-02-20 12:39:23.030544+00', 'On Course - Test: No Solid White', 'Wincanton', 'no lights', 95),
(136, '2021-02-20 12:40:18.956519+00', 'On Course - Test: No Solid White', 'Wincanton', 'no lights', 121),
(137, '2021-02-20 13:13:20.441041+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 25),
(138, '2021-02-20 13:13:40.018926+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 35),
(139, '2021-02-20 13:58:55.543934+00', 'On Course - Racing: Not to course', 'Wincanton', '', 131),
(140, '2021-02-20 13:59:12.776826+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 28),
(141, '2021-02-20 14:17:47.549909+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 61),
(142, '2021-02-20 14:18:03.133125+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 69),
(143, '2021-02-20 14:18:18.773154+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 39),
(144, '2021-02-20 14:34:45.494965+00', 'On Course - Racing: Not to course', 'Wincanton', '', 5),
(145, '2021-02-20 14:55:35.421059+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 25),
(146, '2021-02-20 15:21:45.162648+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 60),
(147, '2021-02-20 15:22:22.851222+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 40),
(148, '2021-02-20 16:04:12.390411+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 88),
(149, '2021-02-21 13:59:36.100266+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 89),
(150, '2021-02-21 14:00:14.85581+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 25),
(151, '2021-02-22 13:46:13.825611+00', 'On Course - Racing: Stuck on track', 'Carlisle', '', 116),
(153, '2021-02-23 12:33:10.666023+00', 'On Course - Racing: Not to course', 'Taunton', '', 41),
(154, '2021-02-23 12:33:29.530393+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 132),
(155, '2021-02-23 13:02:40.516718+00', 'On Course - Racing: Not to course', 'Taunton', '', 43),
(156, '2021-02-23 13:03:01.933929+00', 'On Course - Racing: Not to course', 'Taunton', '', 10),
(157, '2021-02-23 13:03:26.614026+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 39),
(158, '2021-02-23 13:03:44.163065+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 120),
(159, '2021-02-23 13:04:22.029239+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 53),
(160, '2021-02-23 13:07:27.103161+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 16),
(161, '2021-02-23 13:07:44.255312+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 7),
(162, '2021-02-23 14:08:33.990022+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 35),
(163, '2021-02-23 14:31:37.705155+00', 'On Course - Racing: Not to course', 'Taunton', '', 28),
(164, '2021-02-23 14:31:55.535938+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 51),
(165, '2021-02-23 14:32:10.421037+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 5),
(166, '2021-02-23 15:08:40.635737+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 6),
(168, '2021-02-23 15:46:29.930038+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 23),
(169, '2021-02-23 15:46:40.478818+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 88),
(170, '2021-02-24 17:20:47.326912+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 131),
(171, '2021-02-24 17:21:05.788955+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 119),
(172, '2021-02-24 17:21:30.699047+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 127),
(173, '2021-02-24 17:22:09.372013+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 79),
(174, '2021-02-24 17:22:27.894615+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 73),
(175, '2021-02-24 17:22:42.545886+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 59),
(176, '2021-02-24 17:23:02.628146+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 36),
(177, '2021-02-24 17:51:31.161817+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 39),
(178, '2021-02-24 17:52:12.948711+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 25),
(179, '2021-02-24 18:19:57.13197+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 29),
(180, '2021-02-24 20:00:25.16903+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 55),
(181, '2021-02-24 20:00:43.837075+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 122),
(182, '2021-02-26 12:38:11.702394+00', 'On Course - Racing: Not to course', 'Exeter', '', 121),
(183, '2021-02-26 12:38:59.00258+00', 'On Course - Racing: Not to course', 'Exeter', '', 122),
(184, '2021-02-26 12:39:34.532231+00', 'On Course - Racing: Not to course', 'Exeter', '', 22),
(185, '2021-02-26 12:39:57.038732+00', 'On Course - Racing: Not to course', 'Exeter', '', 34),
(186, '2021-02-26 13:06:57.345587+00', 'On Course - Racing: Not to course', 'Exeter', '', 120),
(187, '2021-02-26 13:07:22.937429+00', 'On Course - Racing: Not to course', 'Exeter', '', 95),
(188, '2021-02-26 13:07:40.010355+00', 'On Course - Racing: Not to course', 'Exeter', '', 117),
(189, '2021-02-26 13:08:07.698099+00', 'On Course - Racing: Not to course', 'Exeter', '', 89),
(190, '2021-02-27 13:25:45.444243+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 131),
(191, '2021-02-27 13:26:13.539459+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 48),
(192, '2021-02-27 13:26:45.511377+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 25),
(193, '2021-02-27 13:56:40.599255+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 39),
(194, '2021-02-27 13:57:13.947244+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 55),
(195, '2021-02-27 14:30:37.680481+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 77),
(196, '2021-02-27 14:31:25.449195+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 6),
(197, '2021-02-27 15:06:06.903598+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 38),
(198, '2021-02-27 15:06:27.074915+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 36),
(199, '2021-02-27 16:29:59.141413+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 44),
(200, '2021-03-01 15:11:48.819776+00', 'On Course - Racing: Not to course', 'Ayr', '', 126),
(201, '2021-03-01 15:12:19.35722+00', 'On Course - Racing: Stuck on track', 'Ayr', '', 137),
(202, '2021-03-03 13:40:16.80767+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 53),
(203, '2021-03-03 13:40:43.40249+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 84),
(204, '2021-03-03 13:41:09.935215+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 72),
(205, '2021-03-03 13:41:33.122055+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 71),
(206, '2021-03-03 13:42:00.665883+00', 'On Course - Racing: Stuck on track', 'Wincanton', '', 10),
(207, '2021-03-05 13:21:29.740155+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 39),
(208, '2021-03-05 15:29:13.459307+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 35),
(209, '2021-03-05 15:29:38.819725+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 25),
(210, '2021-03-06 13:06:39.223824+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 96),
(211, '2021-03-06 13:07:41.107239+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 97),
(212, '2021-03-06 13:08:05.371775+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 10),
(213, '2021-03-06 13:08:28.476347+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 9),
(214, '2021-03-06 13:56:23.602456+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 50),
(215, '2021-03-09 12:38:36.112935+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 53),
(216, '2021-03-09 12:39:09.378713+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 39),
(217, '2021-03-09 12:39:29.277171+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 36),
(218, '2021-03-09 13:07:43.352949+00', 'On Course - Racing: Not to course', 'Exeter', '', 77),
(219, '2021-03-09 13:08:33.32192+00', 'On Course - Racing: Not to course', 'Exeter', '', 95),
(220, '2021-03-09 13:08:58.475593+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 6),
(221, '2021-03-09 13:09:19.294705+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 66),
(222, '2021-03-09 14:12:20.684988+00', 'On Course - Racing: Not to course', 'Exeter', '', 111),
(223, '2021-03-09 14:12:43.366709+00', 'On Course - Racing: Not to course', 'Exeter', '', 131),
(224, '2021-03-09 14:12:43.583336+00', 'On Course - Racing: Not to course', 'Exeter', '', 131),
(225, '2021-03-09 14:13:10.095966+00', 'On Course - Racing: Not to course', 'Exeter', '', 127),
(226, '2021-03-09 14:13:35.833704+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 45),
(227, '2021-03-09 14:14:01.568615+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 71),
(228, '2021-03-09 14:47:53.228302+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 132),
(229, '2021-03-09 15:18:39.018352+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 69),
(230, '2021-03-10 16:41:09.253029+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 121),
(231, '2021-03-10 17:23:01.692296+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 6),
(232, '2021-03-10 17:23:17.630995+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 8),
(233, '2021-03-10 17:23:35.008379+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 7),
(234, '2021-03-10 18:23:35.973894+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 120),
(235, '2021-03-10 18:24:00.051085+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 72),
(236, '2021-03-10 18:24:52.186909+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 39),
(237, '2021-03-10 18:25:09.568688+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 89),
(238, '2021-03-10 18:53:05.516063+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 131),
(239, '2021-03-10 18:53:45.39049+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 108),
(240, '2021-03-10 19:20:48.442918+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 121),
(241, '2021-03-10 19:21:03.200875+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 7),
(242, '2021-03-10 19:51:25.92423+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 52),
(243, '2021-03-12 15:58:32.52775+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 7),
(244, '2021-03-15 14:49:30.739966+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 123),
(245, '2021-03-15 14:49:43.540924+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 77),
(246, '2021-03-15 15:18:27.315657+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 51),
(247, '2021-03-15 15:18:44.933433+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 127),
(248, '2021-03-15 16:13:45.774234+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 15),
(249, '2021-03-15 16:13:57.512757+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 34),
(250, '2021-03-15 16:14:08.489109+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 90),
(251, '2021-03-15 16:14:23.486807+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 7),
(252, '2021-03-15 16:24:57.747036+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 23),
(253, '2021-03-15 16:48:26.151433+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 29),
(254, '2021-03-15 16:48:39.924319+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 36),
(255, '2021-03-15 16:48:59.062448+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 18),
(256, '2021-03-15 16:49:11.014652+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 51),
(257, '2021-03-15 17:15:35.671919+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 46),
(258, '2021-03-15 17:15:46.216955+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 53),
(259, '2021-03-15 17:16:02.619252+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 124),
(260, '2021-03-16 14:57:55.98926+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 23),
(261, '2021-03-16 14:58:15.449158+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 88),
(262, '2021-03-16 14:58:30.201386+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 58),
(263, '2021-03-16 14:58:51.408821+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 25),
(264, '2021-03-17 14:44:05.675746+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 7),
(297, '2021-03-20 13:36:31.142241+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 58),
(298, '2021-03-20 13:36:55.944849+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 42),
(299, '2021-03-22 14:23:32.006242+00', 'On Course - Test: No Solid White', 'Kelso', '', 85),
(300, '2021-03-22 16:05:14.297537+00', 'On Course - Racing: Stuck on track', 'Kelso', '', 126),
(301, '2021-03-23 14:15:17.290682+00', 'On Course - Racing: Not to course', 'Taunton', '', 124),
(302, '2021-03-23 14:15:39.36429+00', 'On Course - Racing: Not to course', 'Taunton', '', 90),
(303, '2021-03-23 14:15:56.138947+00', 'On Course - Racing: Not to course', 'Taunton', '', 40),
(304, '2021-03-23 14:16:11.206314+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 69),
(305, '2021-03-23 14:16:24.314094+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 48),
(306, '2021-03-23 14:43:37.163774+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 42),
(307, '2021-03-23 14:44:14.563901+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 88),
(308, '2021-03-23 15:19:22.346255+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 28),
(309, '2021-03-23 15:19:34.866769+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 25),
(310, '2021-03-23 15:19:47.625984+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 54),
(311, '2021-03-23 15:20:01.155774+00', 'On Course - Racing: Not to course', 'Taunton', '', 75),
(312, '2021-03-23 15:20:16.61694+00', 'On Course - Racing: Not to course', 'Taunton', '', 51),
(313, '2021-03-23 15:57:10.623957+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 22),
(314, '2021-03-23 15:57:33.36807+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 38),
(315, '2021-03-23 15:57:46.267149+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 133),
(316, '2021-03-23 16:09:14.457364+00', 'On Course - Racing: Not to course', 'Taunton', '', 54),
(317, '2021-03-23 16:09:41.182976+00', 'On Course - Racing: Not to course', 'Taunton', '', 123),
(318, '2021-03-23 16:16:19.775272+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 24),
(319, '2021-03-23 16:19:16.490131+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 7),
(320, '2021-03-23 16:19:39.827812+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 75),
(321, '2021-03-23 16:29:57.496008+00', 'On Course - Racing: Stuck on track', 'Wetherby', '', 51),
(322, '2021-03-23 16:56:53.341078+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 53),
(323, '2021-03-23 16:57:03.235581+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 37),
(324, '2021-03-23 16:57:15.665041+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 30),
(325, '2021-03-26 12:40:22.204903+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 30),
(326, '2021-03-26 14:09:05.140726+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 83),
(327, '2021-03-26 14:38:39.473275+00', 'On Course - Racing: Stuck on track', 'Musselburgh', '', 21),
(328, '2021-03-26 14:48:22.285386+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 22),
(329, '2021-03-26 15:26:32.719754+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 47),
(330, '2021-03-26 15:41:58.901837+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 86),
(331, '2021-03-26 15:42:55.58725+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 70),
(332, '2021-03-26 15:43:28.343278+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 67),
(333, '2021-03-26 16:17:46.287802+00', 'On Course - Racing: Not to course', 'Musselburgh', '', 85),
(334, '2021-03-27 14:09:14.896352+00', 'On Course - Racing: Stuck on track', 'Kelso', '', 126),
(335, '2021-03-27 17:47:01.674039+00', 'On Course - Racing: Stuck on track', 'Newbury', '', 66),
(336, '2021-04-08 12:52:55.65486+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 25),
(337, '2021-04-08 12:53:23.478994+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 29),
(338, '2021-04-08 12:53:39.143386+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 64),
(339, '2021-04-08 12:54:02.926182+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 30),
(340, '2021-04-08 13:32:07.654448+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 20),
(341, '2021-04-08 13:32:20.898915+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 40),
(342, '2021-04-08 14:04:07.891272+00', 'On Course - Racing: Stuck on track', 'Aintree', '', 46),
(343, '2021-04-15 12:32:13.152968+00', 'On Course - Racing: Not to course', 'Cheltenham', '', 117),
(344, '2021-04-15 14:04:25.028839+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 51),
(345, '2021-04-15 14:16:22.682075+00', 'On Course - Racing: Not to course', 'Cheltenham', '', 83),
(346, '2021-04-15 14:24:59.522616+00', 'On Course - Racing: Stuck on track', 'Cheltenham', '', 125),
(347, '2021-04-21 16:38:13.314278+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 28),
(348, '2021-04-21 16:38:26.308601+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 89),
(349, '2021-04-21 16:38:41.12937+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 37),
(350, '2021-04-21 17:01:18.073489+00', 'On Course - Racing: Not to course', 'Taunton', '', 71),
(352, '2021-04-21 17:03:37.160266+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 8),
(353, '2021-04-21 17:38:54.627623+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 46),
(354, '2021-04-21 17:39:08.203092+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 96),
(355, '2021-04-21 17:39:26.837706+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 58),
(356, '2021-04-21 17:39:39.549678+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 35),
(357, '2021-04-21 17:39:57.636625+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 42),
(358, '2021-04-21 17:40:22.117066+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 24),
(359, '2021-04-21 18:07:00.156949+00', 'On Course - Racing: Stuck on track', 'Taunton', '', 15),
(360, '2021-04-22 18:04:03.388059+00', 'On Course - Racing: Not to course', 'Exeter', '', 96),
(361, '2021-04-22 18:04:21.953854+00', 'On Course - Racing: Stuck on track', 'Exeter', '', 16),
(362, '2021-04-24 13:42:17.013645+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 37),
(363, '2021-04-24 15:24:14.075113+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 75),
(364, '2021-04-24 15:24:30.937143+00', 'On Course - Racing: Stuck on track', 'Sandown Park', '', 48),
(365, '2021-04-24 15:24:43.336349+00', 'On Course - Racing: Stuck on track', 'Haydock', '', 58),
(366, '2021-04-30 12:42:51.293612+00', 'On Course - Racing: Not to course', 'Goodwood', '', 131),
(367, '2021-04-30 12:43:20.593959+00', 'On Course - Racing: Not to course', 'Goodwood', '', 95),
(368, '2021-05-05 17:15:32.842282+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 96),
(369, '2021-05-05 17:16:24.781682+00', 'On Course - Racing: Not to course', 'Kempton Park', '', 75),
(370, '2021-05-05 17:16:38.642731+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 133),
(371, '2021-05-13 10:10:00.697472+00', 'In Refurb - Send for mechanical repair', NULL, '', 55),
(372, '2021-05-13 12:21:41.493501+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 30),
(373, '2021-05-13 12:21:54.101539+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 86),
(374, '2021-05-13 12:22:21.385936+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 138),
(375, '2021-05-13 13:46:59.753331+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 60),
(376, '2021-05-13 13:47:25.488346+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 139),
(377, '2021-05-13 13:47:38.481895+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 53),
(378, '2021-05-13 13:47:49.72567+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 33),
(379, '2021-05-18 08:28:05.109403+00', 'In Refurb - Broken beyond repair', NULL, '', 67),
(380, '2021-05-21 13:28:52.969961+00', 'On Course - Racing: Stuck on track', 'Haydock', '', 35),
(381, '2021-05-26 19:02:14.748961+00', 'On Course - Racing: Stuck on track', 'Warwick', '', 37),
(382, '2021-05-31 12:37:47.325559+00', 'On Course - Racing: Stuck on track', 'Huntingdon', '', 46),
(383, '2021-05-31 12:38:04.453728+00', 'On Course - Racing: Stuck on track', 'Huntingdon', '', 39),
(384, '2021-05-31 12:38:31.093838+00', 'On Course - Racing: Stuck on track', 'Huntingdon', '', 44),
(385, '2021-05-31 12:38:43.191817+00', 'On Course - Racing: Stuck on track', 'Huntingdon', '', 7),
(386, '2021-05-31 12:38:54.536765+00', 'On Course - Racing: Stuck on track', 'Huntingdon', '', 147),
(387, '2021-05-31 12:39:06.17148+00', 'On Course - Racing: Stuck on track', 'Huntingdon', '', 9),
(388, '2021-06-02 17:18:00.542849+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 42),
(389, '2021-06-02 17:18:13.695832+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 48),
(390, '2021-06-02 17:18:29.720603+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 138),
(391, '2021-06-02 17:19:05.751668+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 29),
(392, '2021-06-02 17:19:21.575637+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 132),
(393, '2021-06-02 17:19:38.946943+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 30),
(394, '2021-06-02 17:49:21.970277+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 15),
(395, '2021-06-02 17:49:53.53424+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 51),
(396, '2021-06-02 17:50:06.121642+00', 'On Course - Racing: Stuck on track', 'Kempton Park', '', 7),
(397, '2021-06-08 14:34:55.665252+00', 'Out of Service and Returned for Refurb', NULL, '', 10),
(398, '2021-06-11 16:24:57.063146+00', 'On Course - Racing: Stuck on track', 'Goodwood', '', 29),
(399, '2021-06-11 16:33:50.01679+00', 'On Course - Racing: Not to course', NULL, 'Fairyhouse', 170),
(400, '2021-06-11 16:34:12.475146+00', 'On Course - Racing: Not to course', NULL, 'Fairyhouse', 158),
(401, '2021-06-11 18:38:18.315475+00', 'On Course - Racing: Stuck on track', 'Goodwood', '', 43),
(402, '2021-06-23 14:05:57.10638+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 53),
(403, '2021-06-23 14:06:18.402628+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 154),
(404, '2021-06-23 14:06:33.723497+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 147),
(405, '2021-06-23 14:06:53.147984+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 162),
(406, '2021-06-23 14:07:08.138415+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 35),
(407, '2021-06-23 14:07:55.302198+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 31),
(408, '2021-06-23 14:08:11.081036+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 171),
(409, '2021-06-23 14:08:30.445548+00', 'On Course - Racing: Stuck on track', 'Salisbury', '', 42);