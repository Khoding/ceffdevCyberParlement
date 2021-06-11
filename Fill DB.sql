#fill Personne
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM Personne WHERE id > 0;
ALTER TABLE Personne AUTO_INCREMENT=1;
INSERT INTO Personne(date_joined, is_staff, is_superuser, password, id, last_name, first_name, Genre, Email, NPA, Localite, username, is_active)
VALUES 
(0,0,0,"Pa$$w0rd",1,"Allemand","Jérémie","Masculin","Jeremie.Allemand@ceff.ch",2533,"Evilard","1",1),
(0,0,0,"Pa$$w0rd",2,"Assunçao","Gaëtan","Masculin","Gaetan.Assuncao@ceff.ch",2345,"Les Breuleux","2",1),
(0,0,0,"Pa$$w0rd",3,"Avalos","Yann","Masculin","Yann.Avalos@ceff.ch",2740,"Moutier","3",1),
(0,0,0,"Pa$$w0rd",4,"Bachmann","Elisa","Féminin","Elisa.Bachmann@ceff.ch",2607,"Cortébert","4",1),
(0,0,0,"Pa$$w0rd",5,"Bane","Erwan","Masculin","Erwan.Bane@ceff.ch",2504,"Biel/Bienne","5",1),
(0,0,0,"Pa$$w0rd",6,"Bassard","Grégory","Masculin","Gregory.Bassard@ceff.ch",2606,"Corgémont","6",1),
(0,0,0,"Pa$$w0rd",7,"Baumgartner","Maël","Masculin","Mael.Baumgartner@ceff.ch",2720,"Tramelan","7",1),
(0,0,0,"Pa$$w0rd",8,"Becker","Quentin","Masculin","Quentin.Becker@ceff.ch",2735,"Malleray","8",1),
(0,0,0,"Pa$$w0rd",9,"Beglieri","Evan","Masculin","Evan.Beglieri@ceff.ch",2504,"Biel/Bienne","9",1),
(0,0,0,"Pa$$w0rd",10,"Besia","Flavien","Masculin","Flavien.Besia@ceff.ch",2017,"Boudry","10",1),
(0,0,0,"Pa$$w0rd",11,"Blanc","Bastien","Masculin","Bastien.Blanc@ceff.ch",2732,"Reconvilier","11",1),
(0,0,0,"Pa$$w0rd",12,"Boillat","Rémy","Masculin","Remy.Boillat@ceff.ch",2610,"St-Imier","12",1),
(0,0,0,"Pa$$w0rd",13,"Bonardo","Quentin","Masculin","Quentin.Bonardo@ceff.ch",2720,"Tramelan","13",1),
(0,0,0,"Pa$$w0rd",14,"Boulahdjar","Ahmed","Masculin","Ahmed.Boulahdjar@ceff.ch",2502,"Biel/Bienne","14",1),
(0,0,0,"Pa$$w0rd",15,"Bourquin","Arnaud","Masculin","Arnaud.Bourquin@ceff.ch",2610,"St-Imier","15",1),
(0,0,0,"Pa$$w0rd",16,"Brechbühler","Julien","Masculin","Julien.Brechbuehler@ceff.ch",2535,"Frinvillier","16",1),
(0,0,0,"Pa$$w0rd",17,"Brossard","Laurent","Masculin","Laurent.Brossard@ceff.ch",2525,"Le Landeron","17",1),
(0,0,0,"Pa$$w0rd",18,"Brossard","Sabrina","Féminin","Sabrina.Brossard@ceff.ch",2504,"Biel/Bienne","18",1),
(0,0,0,"Pa$$w0rd",19,"Brun","Sébastien","Masculin","Sebastien.Brun@ceff.ch",2735,"Bévilard","19",1),
(0,0,0,"Pa$$w0rd",20,"Bünzli","Vladimir","Masculin","Vladimir.Buenzli@ceff.ch",3008,"Bern","20",1),
(0,0,0,"Pa$$w0rd",21,"Bürki","Dylan","Masculin","Dylan.Buerki@ceff.ch",2723,"Mont-Tramelan","21",1),
(0,0,0,"Pa$$w0rd",22,"Capito","Melanie","Féminin","Melanie.Capito@ceff.ch",2610,"St-Imier","22",1),
(0,0,0,"Pa$$w0rd",23,"Carnal","Noah","Masculin","Noah.Carnal@ceff.ch",2720,"Tramelan","23",1),
(0,0,0,"Pa$$w0rd",24,"Cattin","Janis","Masculin","Janis.Cattin@ceff.ch",2504,"Biel/Bienne","24",1),
(0,0,0,"Pa$$w0rd",25,"Celik","Dilan","Masculin","Dilan.Celik@ceff.ch",2502,"Biel/Bienne","25",1),
(0,0,0,"Pa$$w0rd",26,"Chaignat","Mathis","Masculin","Mathis.Chaignat@ceff.ch",2350,"Saignelégier","26",1),
(0,0,0,"Pa$$w0rd",27,"Charpié","Ludovic","Masculin","Ludovic.Charpie@ceff.ch",2515,"Prêles","27",1),
(0,0,0,"Pa$$w0rd",28,"Claro","Esteban","Masculin","Esteban.Claro@ceff.ch",2520,"La Neuveville","28",1),
(0,0,0,"Pa$$w0rd",29,"Coric","Maksim","Masculin","Maksim.Coric@ceff.ch",2534,"Orvin","29",1),
(0,0,0,"Pa$$w0rd",30,"Cudré-Mauroux","Bryan","Masculin","Bryan.Cudre-Mauroux@ceff.ch",2608,"Courtelary","30",1),
(0,0,0,"Pa$$w0rd",31,"Cuénod Zanuttig","Jean-Paul","Masculin","Jean-Paul.CuenodZanuttig@ceff.ch",2208,"Les Hauts-Geneveys","31",1),
(0,0,0,"Pa$$w0rd",32,"Da Cruz Lopes","Rafael","Masculin","Rafael.DaCruzLopes@ceff.ch",2504,"Biel/Bienne","32",1),
(0,0,0,"Pa$$w0rd",33,"Dadém","Vicky","Masculin","Vicky.Dadem@ceff.ch",2502,"Biel/Bienne","33",1),
(0,0,0,"Pa$$w0rd",34,"De Marco","Allan","Masculin","Allan.DeMarco@ceff.ch",2504,"Biel/Bienne","34",1),
(0,0,0,"Pa$$w0rd",35,"De Marco","Nolan","Masculin","Nolan.DeMarco@ceff.ch",2504,"Biel/Bienne","35",1),
(0,0,0,"Pa$$w0rd",36,"De Oliveira Jorge","Tiago","Masculin","Tiago.DeOliveiraJorge@ceff.ch",2720,"Tramelan","36",1),
(0,0,0,"Pa$$w0rd",37,"Delli Santi","Valerio","Masculin","Valerio.DelliSanti@ceff.ch",2504,"Biel/Bienne","37",1),
(0,0,0,"Pa$$w0rd",38,"Devanthéry","Noa","Masculin","Noa.Devanthery@ceff.ch",2345,"Les Breuleux","38",1),
(0,0,0,"Pa$$w0rd",39,"Di Benedetto","Lorenzo","Masculin","Lorenzo.DiBenedetto@ceff.ch",2560,"Nidau","39",1),
(0,0,0,"Pa$$w0rd",40,"Di Caprio","Louis","Masculin","Louis.DiCaprio@ceff.ch",2603,"Péry","40",1),
(0,0,0,"Pa$$w0rd",41,"Di Gaetano","Kylian","Masculin","Kylian.DiGaetano@ceff.ch",2504,"Biel/Bienne","41",1),
(0,0,0,"Pa$$w0rd",42,"Dobbs","Jack","Masculin","Jack.Dobbs@ceff.ch",2610,"St-Imier","9000",1),
(0,0,0,"Pa$$w0rd",43,"D'Ostuni","Gabriel","Masculin","Gabriel.D'Ostuni@ceff.ch",2504,"Biel/Bienne","42",1),
(0,0,0,"Pa$$w0rd",44,"Droz","Loan","Masculin","Loan.Droz@ceff.ch",2720,"Tramelan","43",1),
(0,0,0,"Pa$$w0rd",45,"Ebanelli","Dario","Masculin","Dario.Ebanelli@ceff.ch",2553,"Safnern","44",1),
(0,0,0,"Pa$$w0rd",46,"Flückiger","Jonas Emmanuel","Masculin","JonasEmmanuel.Flueckiger@ceff.ch",2555,"Brügg BE","45",1),
(0,0,0,"Pa$$w0rd",47,"Frick","Gabriel","Masculin","Gabriel.Frick@ceff.ch",2503,"Biel/Bienne","46",1),
(0,0,0,"Pa$$w0rd",48,"Froidevaux","Julien","Masculin","Julien.Froidevaux@ceff.ch",2732,"Reconvilier","47",1),
(0,0,0,"Pa$$w0rd",49,"Geara","Kevin","Masculin","Kevin.Geara@ceff.ch",2610,"St-Imier","48",1),
(0,0,0,"Pa$$w0rd",50,"Gerber","Anouchka","Féminin","Anouchka.Gerber@ceff.ch",2732,"Reconvilier","49",1),
(0,0,0,"Pa$$w0rd",51,"Gerber","Thomas","Masculin","Thomas.Gerber@ceff.ch",2720,"Tramelan","50",1),
(0,0,0,"Pa$$w0rd",52,"Gianoli","Kenzo","Masculin","Kenzo.Gianoli@ceff.ch",2610,"Les Pontins","51",1),
(0,0,0,"Pa$$w0rd",53,"Good","Noah","Masculin","Noah.Good@ceff.ch",2534,"Orvin","52",1),
(0,0,0,"Pa$$w0rd",54,"Grasset","John","Masculin","John.Grasset@ceff.ch",2503,"Biel/Bienne","53",1),
(0,0,0,"Pa$$w0rd",55,"Gürsültür","Emre","Masculin","Emre.Guersueltuer@ceff.ch",2345,"Les Breuleux","54",1),
(0,0,0,"Pa$$w0rd",56,"Hadorn","Raphaël","Masculin","Raphael.Hadorn@ceff.ch",2610,"St-Imier","55",1),
(0,0,0,"Pa$$w0rd",57,"Hafez","Ward","Masculin","Ward.Hafez@ceff.ch",2720,"Tramelan","56",1),
(0,0,0,"Pa$$w0rd",58,"Hazeraj","Ekuran","Masculin","Ekuran.Hazeraj@ceff.ch",2520,"La Neuveville","57",1),
(0,0,0,"Pa$$w0rd",59,"Hazeraj","Herdison","Masculin","Herdison.Hazeraj@ceff.ch",2520,"La Neuveville","58",1),
(0,0,0,"Pa$$w0rd",60,"Huber","Mallory","Masculin","Mallory.Huber@ceff.ch",2710,"Tavannes","59",1),
(0,0,0,"Pa$$w0rd",61,"Jeandupeux","Romaine","Féminin","Romaine.Jeandupeux@ceff.ch",2720,"Tramelan","61",1),
(0,0,0,"Pa$$w0rd",62,"Kinkio","Mathéo","Masculin","Matheo.Kinkio@ceff.ch",2516,"Lamboing","62",1),
(0,0,0,"Pa$$w0rd",63,"Kueviakoe","Kevin","Masculin","Kevin.Kueviakoe@ceff.ch",2504,"Biel/Bienne","63",1),
(0,0,0,"Pa$$w0rd",64,"Kukiele","Joel Nzila","Masculin","JoelNzila.Kukiele@ceff.ch",2503,"Biel/Bienne","64",1),
(0,0,0,"Pa$$w0rd",65,"Leite Serra","Fabio","Masculin","Fabio.LeiteSerra@ceff.ch",2504,"Biel/Bienne","65",1),
(0,0,0,"Pa$$w0rd",66,"Lenardon","Arnaud","Masculin","Arnaud.Lenardon@ceff.ch",2720,"Tramelan","66",1),
(0,0,0,"Pa$$w0rd",67,"L'Epée","Thibault","Masculin","Thibault.L'Epee@ceff.ch",2520,"La Neuveville","67",1),
(0,0,0,"Pa$$w0rd",68,"Leydecker","Malo","Masculin","Malo.Leydecker@ceff.ch",2520,"La Neuveville","68",1),
(0,0,0,"Pa$$w0rd",69,"Liechti","Kevin","Masculin","Kevin.Liechti@ceff.ch",2718,"Lajoux JU","69",1),
(0,0,0,"Pa$$w0rd",70,"Magnin","Nicolas","Masculin","Nicolas.Magnin@ceff.ch",2345,"Les Breuleux","70",1),
(0,0,0,"Pa$$w0rd",71,"Maître","Arnaud","Masculin","Arnaud.Maitre@ceff.ch",2743,"Eschert","71",1),
(0,0,0,"Pa$$w0rd",72,"Martin","Alix","Masculin","Alix.Martin@ceff.ch",2720,"Tramelan","72",1),
(0,0,0,"Pa$$w0rd",73,"Mathez","Quentin","Masculin","Quentin.Mathez@ceff.ch",2720,"Tramelan","73",1),
(0,0,0,"Pa$$w0rd",74,"Matter","Ernesto","Masculin","Ernesto.Matter@ceff.ch",2603,"Péry","74",1),
(0,0,0,"Pa$$w0rd",75,"Mbida","Daniel Ghislain","Masculin","DanielGhislain.Mbida@ceff.ch",2743,"Eschert","75",1),
(0,0,0,"Pa$$w0rd",76,"Méroz","Bastien","Masculin","Bastien.Meroz@ceff.ch",2613,"Villeret","76",1),
(0,0,0,"Pa$$w0rd",77,"Miron","Robert-Gabriel","Masculin","Robert-Gabriel.Miron@ceff.ch",2610,"St-Imier","77",1),
(0,0,0,"Pa$$w0rd",78,"Mischler","Noé","Masculin","Noe.Mischler@ceff.ch",2610,"St-Imier","78",1),
(0,0,0,"Pa$$w0rd",79,"Mukandanga","Noah","Masculin","Noah.Mukandanga@ceff.ch",2732,"Reconvilier","79",1),
(0,0,0,"Pa$$w0rd",80,"Naine","Yann","Masculin","Yann.Naine@ceff.ch",2743,"Eschert","80",1),
(0,0,0,"Pa$$w0rd",81,"Naylor","Natasha Shiwen","Féminin","NatashaShiwen.Naylor@ceff.ch",2503,"Biel/Bienne","893405",1),
(0,0,0,"Pa$$w0rd",82,"Neli","Fadil","Masculin","Fadil.Neli@ceff.ch",3018,"Bern","81",1),
(0,0,0,"Pa$$w0rd",83,"Ouattara","Marie-Victoire","Féminin","Marie-Victoire.Ouattara@ceff.ch",3065,"Bolligen","82",1),
(0,0,0,"Pa$$w0rd",84,"Özkul","Alp Rushtu","Masculin","AlpRushtu.Oezkul@ceff.ch",2740,"Moutier","83",1),
(0,0,0,"Pa$$w0rd",85,"Pagnon","Emma","Féminin","Emma.Pagnon@ceff.ch",2720,"Tramelan","84",1),
(0,0,0,"Pa$$w0rd",86,"Pahud","Natalia","Féminin","Natalia.Pahud@ceff.ch",2720,"Tramelan","85",1),
(0,0,0,"Pa$$w0rd",87,"Paiva Costa","Diogo","Masculin","Diogo.PaivaCosta@ceff.ch",2610,"St-Imier","86",1),
(0,0,0,"Pa$$w0rd",88,"Paratore","Elian","Masculin","Elian.Paratore@ceff.ch",2504,"Biel/Bienne","87",1),
(0,0,0,"Pa$$w0rd",89,"Péquignot","Steve","Masculin","Steve.Pequignot@ceff.ch",2615,"Sonvilier","88",1),
(0,0,0,"Pa$$w0rd",90,"Petruzzo","Vitoandrea","Masculin","Vitoandrea.Petruzzo@ceff.ch",2502,"Biel/Bienne","89",1),
(0,0,0,"Pa$$w0rd",91,"Petter","Nathanaël","Masculin","Nathanael.Petter@ceff.ch",2722,"Les Reussilles","90",1),
(0,0,0,"Pa$$w0rd",92,"Portal","Timo","Masculin","Timo.Portal@ceff.ch",2610,"St-Imier","91",1),
(0,0,0,"Pa$$w0rd",93,"Pugnant-Gros","Gaël","Masculin","Gael.Pugnant-Gros@ceff.ch",2740,"Moutier","92",1),
(0,0,0,"Pa$$w0rd",94,"Ramey","Arthur","Masculin","Arthur.Ramey@ceff.ch",2710,"Tavannes","93",1),
(0,0,0,"Pa$$w0rd",95,"Ramos Figueiredo","Daniela","Féminin","Daniela.RamosFigueiredo@ceff.ch",2516,"Lamboing","94",1),
(0,0,0,"Pa$$w0rd",96,"Rossier","Adrien Matthieu","Masculin","AdrienMatthieu.Rossier@ceff.ch",2503,"Biel/Bienne","Zzz",1),
(0,0,0,"Pa$$w0rd",97,"Roth","Valentino","Masculin","Valentino.Roth@ceff.ch",2503,"Biel/Bienne","97",1),
(0,0,0,"Pa$$w0rd",98,"Rutscho","Julien","Masculin","Julien.Rutscho@ceff.ch",2608,"Courtelary","pabo",1),
(0,0,0,"Pa$$w0rd",99,"Salzmann","Kevin","Masculin","Kevin.Salzmann@ceff.ch",2735,"Champoz","99",1),
(0,0,0,"Pa$$w0rd",100,"Schmocker","Kevin","Masculin","Kevin.Schmocker@ceff.ch",2502,"Biel/Bienne","100",1),
(0,0,0,"Pa$$w0rd",101,"Schumacher","Alexandre","Masculin","Alexandre.Schumacher@ceff.ch",2515,"Prêles","101",1),
(0,0,0,"Pa$$w0rd",102,"Schwab","Nicolas","Masculin","Nicolas.Schwab@ceff.ch",2616,"Renan BE","bogoss",1),
(0,0,0,"Pa$$w0rd",103,"Schwendimann","Julien","Masculin","Julien.Schwendimann@ceff.ch",2615,"Sonvilier","103",1),
(0,0,0,"Pa$$w0rd",104,"Seuret","Samy","Masculin","Samy.Seuret@ceff.ch",2740,"Moutier","104",1),
(0,0,0,"Pa$$w0rd",105,"Sormasor","Zekria","Masculin","Zekria.Sormasor@ceff.ch",2605,"Sonceboz-Sombeval","105",1),
(0,0,0,"Pa$$w0rd",106,"Spychiger","Lyâm","Masculin","Lyam.Spychiger@ceff.ch",2515,"Prêles","106",1),
(0,0,0,"Pa$$w0rd",107,"Stucki","Anthony","Masculin","Anthony.Stucki@ceff.ch",2605,"Sonceboz-Sombeval","107",1),
(0,0,0,"Pa$$w0rd",108,"Taillard","Johan","Masculin","Johan.Taillard@ceff.ch",2720,"Tramelan","108",1),
(0,0,0,"Pa$$w0rd",109,"Tigossi","Maximilien","Masculin","Maximilien.Tigossi@ceff.ch",2345,"Les Breuleux","109",1),
(0,0,0,"Pa$$w0rd",110,"Tockè","Christelle","Féminin","Christelle.Tocke@ceff.ch",2502,"Biel/Bienne","110",1),
(0,0,0,"Pa$$w0rd",111,"Tormos","Elias","Masculin","Elias.Tormos@ceff.ch",2503,"Biel/Bienne","111",1),
(0,0,0,"Pa$$w0rd",112,"Vasques","Dario","Masculin","Dario.Vasques@ceff.ch",2603,"Péry","112",1),
(0,0,0,"Pa$$w0rd",113,"Viatte","Colin","Masculin","Colin.Viatte@ceff.ch",2350,"Saignelégier","113",1),
(0,0,0,"Pa$$w0rd",114,"Villat","Jonas","Masculin","Jonas.Villat@ceff.ch",2720,"Tramelan","114",1),
(0,0,0,"Pa$$w0rd",115,"Voirol","Vincent","Masculin","Vincent.Voirol@ceff.ch",2720,"Tramelan","115",1),
(0,0,0,"Pa$$w0rd",116,"Wahli","Ocean","Masculin","Ocean.Wahli@ceff.ch",2740,"Moutier","116",1),
(0,0,0,"Pa$$w0rd",117,"Walzer","David","Masculin","David.Walzer@ceff.ch",2720,"Tramelan","117",1),
(0,0,0,"Pa$$w0rd",118,"Zweiacker","Noah","Masculin","Noah.Zweiacker@ceff.ch",2732,"Reconvilier","118",1);

INSERT INTO Personne(id, Nom, Email, username, is_active, is_superuser, is_staff)
VALUES
(119, "Admin", "", "administrator", 1, 1, 1);

DELETE FROM MembreCP WHERE id > 0;
DELETE FROM CyberParlement WHERE id > 0;
ALTER TABLE CyberParlement AUTO_INCREMENT = 1;
INSERT INTO CyberParlement(id,Nom,CPParent,Description,Visibilite,Statutensemble,slug) VALUES
(1,'CPJB', null, 'Cyberparlement du Jura bernois', 'PU','DR','cpjb'),
(2,'Tramelan',1, 'Village de Tramelan', 'PU','DR','tramelan'),
(3,'Tavannes', 1, 'Village de Tavannes', 'PU','DR','tavannes'),
(4,'Saint-Imier',1, 'Village de Saint-Imier', 'PU','DR','saint-imier'),
(5,'ES',2, null, 'PU','DR','es'),
(6,'EP',2, null, 'PU','DR','ep'),
(7,'ES',3, null, 'PU','DR','es-1'),
(8,'EP',3, null, 'PU','DR','ep-1'),
(9,'ES',4, null, 'PU','DR','es-2'),
(10,'EP',4, null, 'PU','DR','ep-2');

DELETE FROM MembreCP WHERE id > 0;
ALTER TABLE MembreCP AUTO_INCREMENT=1;
INSERT INTO MembreCP(idPersonne,idCyberParlement,RoleCP)
VALUES
(1,5,"CC"),
(2,6,"CC"),
(3,7,"CC"),
(4,8,"CC"),
(5,9,"CC"),
(6,10,"CC"),
(8,6,"ME"),
(9,7,"ME"),
(10,8,"ME"),
(11,9,"ME"),
(12,10,"ME"),
(13,5,"ME"),
(14,6,"ME"),
(15,7,"ME"),
(16,8,"ME"),
(17,9,"ME"),
(18,10,"ME"),
(19,5,"ME"),
(20,6,"ME"),
(21,7,"ME"),
(22,8,"ME"),
(23,9,"ME"),
(24,10,"ME"),
(25,5,"ME"),
(26,6,"ME"),
(27,7,"ME"),
(28,8,"ME"),
(29,9,"ME"),
(30,10,"ME"),
(31,5,"ME"),
(32,6,"ME"),
(33,7,"ME"),
(34,8,"ME"),
(35,9,"ME"),
(36,10,"ME"),
(37,5,"ME"),
(38,6,"ME"),
(39,1,"CC"),
(40,8,"ME"),
(41,9,"ME"),
(42,10,"ME"),
(43,5,"ME"),
(44,6,"ME"),
(45,7,"ME"),
(46,8,"ME"),
(47,9,"ME"),
(48,10,"ME"),
(49,5,"ME"),
(50,6,"ME"),
(51,7,"ME"),
(52,8,"ME"),
(53,9,"ME"),
(54,10,"ME"),
(55,5,"ME"),
(56,6,"ME"),
(57,7,"ME"),
(58,8,"ME"),
(59,9,"ME"),
(60,10,"ME"),
(61,5,"ME"),
(62,6,"ME"),
(63,7,"ME"),
(64,8,"ME"),
(65,9,"ME"),
(66,10,"ME"),
(67,5,"ME"),
(68,6,"ME"),
(69,7,"ME"),
(70,8,"ME"),
(71,9,"ME"),
(72,10,"ME"),
(73,5,"ME"),
(74,6,"ME"),
(75,7,"ME"),
(76,8,"ME"),
(77,9,"ME"),
(78,10,"ME"),
(79,5,"ME"),
(80,6,"ME"),
(81,7,"ME"),
(82,8,"ME"),
(83,9,"ME"),
(84,10,"ME"),
(85,5,"ME"),
(86,6,"ME"),
(87,7,"ME"),
(88,8,"ME"),
(89,9,"ME"),
(90,10,"ME"),
(91,5,"ME"),
(92,6,"ME"),
(93,7,"ME"),
(94,8,"ME"),
(95,9,"ME"),
(96,10,"ME"),
(97,5,"ME"),
(98,6,"ME"),
(99,7,"ME"),
(100,8,"ME"),
(101,9,"ME"),
(102,10,"ME"),
(103,5,"ME"),
(104,6,"ME"),
(105,7,"ME"),
(106,8,"ME"),
(107,9,"ME"),
(108,10,"ME"),
(109,5,"ME"),
(110,6,"ME"),
(111,7,"ME"),
(112,8,"ME"),
(113,9,"ME"),
(114,10,"ME"),
(115,5,"ME"),
(116,6,"ME"),
(117,7,"ME"),
(118,8,"ME"),
(102,4,"CC"),
(16,3,"CC");

DELETE FROM Initiative WHERE id > 0;
ALTER TABLE Initiative AUTO_INCREMENT=1;
INSERT INTO Initiative(id, Nom, Description,idCP,idInitiateur,Statut,mode_validation) VALUES
(1,"Fusion EP / ES","Voulez-vous fusionner l'école secondaire avec l'école primaire ?", 5,1,"AVAL","SMS"),
(2,"Plus de crème dans les mille-feuilles", "Évident n'est-ce pas",10,6,"VAL","email");

DELETE FROM ChoixInitiative WHERE id > 0;
ALTER TABLE ChoixInitiative AUTO_INCREMENT=1;
INSERT INTO ChoixInitiative(id, Choix, Ordre) VALUES
(1,"Oui mais c'est l'école secondaire qui dirige",1),
(1,"Oui mais c'est l'école primaire qui dirige",2),
(1,"Non, jamais",3),
(2,"Pas plus, sinon c'est écoeurant",1),
(2," Bien sûr pour le même prix",2),
(2,"Je n'aime pas les mille-feuilles",3);

DELETE FROM VoteInitiative WHERE id > 0;
ALTER TABLE VoteInitiative AUTO_INCREMENT=1;
INSERT INTO VoteInitiative(idPersonne,idChoixInitiative,idInitiative) VALUES
(103,1,1),(109,1,1),(115,2,1);

SET FOREIGN_KEY_CHECKS = 1;