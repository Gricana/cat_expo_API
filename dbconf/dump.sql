--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: api_breed; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.api_breed (id, name) FROM stdin;
2	Шотландская вислоухая
3	Британская короткошерстная
4	Бенгальская
5	Сиамская
6	Абиссинская
7	Русская голубая
8	Сибирская
9	Невская маскарадная
10	Короткошерстный ориентал
11	Корниш-рекс
13	Русская голубая12
14	Русская голубая 52
1	Мейн-кун
\.


--
-- Data for Name: api_color; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.api_color (id, name) FROM stdin;
58	Песочный
59	Cеребристый
60	Белый
61	Серый
62	Рыжий
63	Сиамский
64	Трехцветный
65	Серовато-голубой
66	Черепаховый
67	Серо-бежевый
68	Темно-серый
69	Бежевый
70	Черный
71	Рыэе-коричневый
72	Темно-рыжий
73	Бело-серый
74	Снежно-белый
75	Тигровый
76	Кремовый
77	Дымчатый
78	white
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1
pbkdf2_sha256$870000$BlVrorPrzwnmZXEG7RnSkq$E2p5niYZ1uU3q725OjsiDSkOy2QXXj4iBFTZCum2jzM=	\N	f	test27367213			example@icloud.com	f	t	2024-09-30 21:11:50.64214+03
2
                                                                                         pbkdf2_sha256$870000$kvXI7Psmdm0MR8wxEJkXri$x4b947r0OMC6UtZfDAwcViFImxK0f1mW6kS6/bz/8xo=	\N	f	test273672163			example1@icloud.com	f	t	2024-09-30 21:12:54.551582+03
4	pbkdf2_sha256$870000$jySWEpuvwGRiapdPTXTJpk$JHTJXYR8JRwodkrd
                                                                                                                                                                                  /ZfOlweE66kPKG4XVPu0GGQtNGE=	\N	f	test225163			example3@icloud.com	f	t	2024-10-01 14:12:37.354715+03
\.


--
-- Data for Name: api_cat; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.api_cat (id, color_id, age, description, breed_id, owner_id) FROM stdin;
1	59	36	Очень общительная и активная кошка. Любит играть с мячиками и лазить по когтеточкам. Хорошо ладит с другими животными и детьми, отличается добродушным нравом. Всегда приветствует хозяев при входе и часто мурлыкает. Эта кошка обожает исследовать новые пространства и прятаться в неожиданных местах.	2	4
2	60	48	Ласковая и спокойная кошка, предпочитающая проводить время в тишине и уюте. Часто отдыхает на подоконнике и наблюдает за птицами на улице. Отличается уравновешенным характером, любит обниматься и сидеть на руках. Может часами спать на коленях хозяев.	5	4
3	61	60	Настоящий охотник, даже в условиях квартиры. Всегда активно играет, прыгнет за игрушками, никогда не сидит на месте. Обожает проводить время на балконе, наблюдая за окружающим миром. Несмотря на активность, к вечеру становится невероятно ласковой.	2	2
4	62	30	Веселая и игривая кошка, очень дружелюбная и любопытная. Любит компанию людей и других животных. Всегда готова поучаствовать в играх и может забавно выпрашивать внимание. Её весёлый нрав делает её идеальной спутницей для активных семей.	8	1
5	63	72	Умиротворенная кошка, которая обожает уютные места и теплые пледы. Хорошо приспосабливается к домашней жизни и предпочитает размеренные и спокойные будни. Может долго сидеть в одном месте, наблюдая за происходящим вокруг.	4	4
6	64	20	Обожает играть с водой и часто «помогает» хозяевам мыть посуду или полы. Эта кошка обладает живым характером, но при этом умеет расслабляться и наслаждаться покоем. Любит внимательное отношение и ласку, хорошо уживается с другими животными.	7	2
7	65	12	Игривый и смелый котенок, который любит исследовать каждый уголок дома. Несмотря на возраст, уже проявляет характер лидера, не боится новых людей и охотно идет на контакт. Его игривость сочетается с ласковым и добрым характером.	6	2
8	66	54	Мягкий и добродушный питомец, обожающий нежные прикосновения и долгие часы сна. Отличается спокойным нравом, очень редко проявляет агрессию или беспокойство. Идеальный компаньон для спокойной жизни в доме, не требует особого ухода.	9	4
9	67	40	Ласковый и дружелюбный кот, который всегда находится рядом с хозяевами. Любит обниматься и проводит много времени на руках. Несмотря на свою привязанность, не навязчив и иногда предпочитает побыть в одиночестве. Легко обучается простым трюкам.	3	1
10	68	68	Независимый и спокойный кот, который предпочитает проводить время в одиночестве. Хотя любит ласку, но только тогда, когда сам этого захочет. Обожает наблюдать за происходящим с высоты, иногда может быть немного ленивым.	10	2
11	69	34	 Эта кошка – настоящий аристократ. Любит порядок и тишину, всегда аккуратно использует свои вещи. Обожает, когда ей уделяют внимание, но всегда сдержанно выражает свои эмоции. Идеально подходит для спокойной и размеренной жизни в квартире.	1	1
12	70	26	Очень игривый кот, который обожает внимание и активные игры. Никогда не сидит на месте, всегда находится в движении. Хорошо ладит с детьми и другими животными, может подолгу играть с игрушками и ловить мячики.	5	4
13	71	46	Ласковая кошка, которая любит проводить время на руках у хозяев. Хорошо чувствует настроение человека и может подойти для успокоения, если это необходимо. Легко адаптируется к новым условиям и быстро привыкает к новым людям.	7	4
16	78	16	Very playful kitten	13	4
14	72	58	Очень внимательная кошка, которая любит наблюдать за всем, что происходит вокруг. Часто сидит на подоконнике или в высоких местах, следя за движением на улице. Не очень активна, предпочитает спокойствие и уютные уголки.	11	2
15	73	15	Игривый и дружелюбный кот, который любит быть в центре внимания. Отлично ладит с детьми и не боится шума и новых людей. Обожает бегать по дому и прятаться в самых неожиданных местах, а также часто выпрашивает угощения.	8	1
17	74	64	Эта кошка отличается спокойным и уравновешенным характером. Любит проводить время в тишине, сидя на мягком кресле или на коленях у хозяев. Очень ласковая, легко привязывается к людям, но не навязчива.	11	1
18	75	52	Независимая и своенравная кошка, которая любит проводить время в одиночестве. Часто сидит на возвышенностях, наблюдая за происходящим. Очень чистоплотна и аккуратна, не любит лишнего внимания, но при этом способна подарить много любви своему хозяину.	7	2
24	77	325	Пример описания	1	4
\.


--
-- Data for Name: api_rating; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.api_rating (id, rating, cat_id, user_id) FROM stdin;
2	4	18	4
4	5	9	4
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	api	rating
8	api	breed
9	api	cat
10	api	color
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add rating	7	add_rating
26	Can change rating	7	change_rating
27	Can delete rating	7	delete_rating
28	Can view rating	7	view_rating
29	Can add breed	8	add_breed
30	Can change breed	8	change_breed
31	Can delete breed	8	delete_breed
32	Can view breed	8	view_breed
33	Can add cat	9	add_cat
34	Can change cat	9	change_cat
35	Can delete cat	9	delete_cat
36	Can view cat	9	view_cat
37	Can add color	10	add_color
38	Can change color	10	change_color
39	Can delete color	10	delete_color
40	Can view color	10	view_color
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-09-30 20:54:59.805002+03
2	auth	0001_initial	2024-09-30 20:55:00.675576+03
3	admin	0001_initial	2024-09-30 20:55:00.859009+03
4	admin	0002_logentry_remove_auto_add	2024-09-30 20:55:00.874277+03
5	admin	0003_logentry_add_action_flag_choices	2024-09-30 20:55:00.89001+03
6	contenttypes	0002_remove_content_type_name	2024-09-30 20:55:00.919338+03
7	auth	0002_alter_permission_name_max_length	2024-09-30 20:55:00.933223+03
8	auth	0003_alter_user_email_max_length	2024-09-30 20:55:00.94836+03
9	auth	0004_alter_user_username_opts	2024-09-30 20:55:00.965179+03
10	auth	0005_alter_user_last_login_null	2024-09-30 20:55:00.981518+03
11	auth	0006_require_contenttypes_0002	2024-09-30 20:55:00.992611+03
12	auth	0007_alter_validators_add_error_messages	2024-09-30 20:55:01.006421+03
13	auth	0008_alter_user_username_max_length	2024-09-30 20:55:01.062919+03
14	auth	0009_alter_user_last_name_max_length	2024-09-30 20:55:01.082165+03
15	auth	0010_alter_group_name_max_length	2024-09-30 20:55:01.099506+03
16	auth	0011_update_proxy_permissions	2024-09-30 20:55:01.118022+03
17	auth	0012_alter_user_first_name_max_length	2024-09-30 20:55:01.13274+03
18	sessions	0001_initial	2024-09-30 20:55:01.276293+03
19	api	0001_initial	2024-09-30 23:28:40.112181+03
20	api	0002_alter_cat_breed	2024-09-30 23:31:02.449432+03
21	api	0003_alter_cat_age	2024-09-30 23:35:08.761401+03
22	api	0003_auto_20241001_1714	2024-10-01 20:32:13.569193+03
25	api	0004_color_alter_breed_name_alter_cat_age_and_more	2024-10-01 20:39:47.321039+03
26	api	0005_auto_20241001_1740	2024-10-01 20:45:10.553508+03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin_mail_importer
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Name: api_breed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.api_breed_id_seq', 16, true);


--
-- Name: api_cat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.api_cat_id_seq', 24, true);


--
-- Name: api_color_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.api_color_id_seq', 78, true);


--
-- Name: api_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.api_rating_id_seq', 4, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 4, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_mail_importer
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- PostgreSQL database dump complete
--

