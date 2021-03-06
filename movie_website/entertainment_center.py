# coding=UTF-8
import media
import fresh_tomatoes

# Entering the data of the movies in instancies of the class Movie.
shawshank = media.Movie("The Shawshank redemption", "Sueños de fuga", 
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", 
	"https://www.youtube.com/watch?v=NmzuHjWmXOc", 
	"A banker gets in jail by allegedly killing his wife and her lover; not accustomed to this life in prison he receives a bad treatment, but never loses hope",
	"1994","Frank Darabont","Tim Robbins","Morgan Freeman","5")
dark_knight = media.Movie("Dark Knight","Batman: El caballero de la noche",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY",
	"In a city with rampant corruption and under the criminals reign, Batman finds some allies to give the fight.",
	"2008","Christopher Nolan","Christian Bale","Heath Ledger","5")
batman_begins = media.Movie("Batman Begins","Batman inicia",
	"https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
	"https://www.youtube.com/watch?v=neY2xVmOfUM","An orphan boy looks for ways to fight injustice and to sublimate his rage with the world, and eventually becomes a masked protector of his city.",
	"2005","Christopher Nolan","Christian Bale","Michael Cain","4")
dark_knight_rises = media.Movie("Dark Knight rises","El caballero de la noche renace",
	"https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY",
	"The biggest city in the world is about to be finally destroyed by the league of shadows, and Batman is taken to the limit to save the city he loves.",
	"2012","Christopher Nolan","Christian Bale","Anne Hathaway","4")
million_dollar = media.Movie("Million dollar baby","Million dollar baby",
	"https://upload.wikimedia.org/wikipedia/en/d/d3/Million_Dollar_Baby_poster.jpg",
	"https://www.youtube.com/watch?v=5_RsHRmIRBY",
	"A girl with talent finds the job that could get her out of poverty, but things will not be easy for her.",
	"2004","Clint Eastwood","Hillary Swank","Clint Eastwood","4,5")
gran_torino = media.Movie("Gran torino","Gran torino",
	"https://upload.wikimedia.org/wikipedia/en/c/c6/Gran_Torino_poster.jpg",
	"https://www.youtube.com/watch?v=3WkGaPMInMc",
	"An old man seems to be an outrageous white supremacist, but in the deep he is just a guy without love.",
	"2008","Clint Eastwood","Clint Eastwood","Christopher Carley","4,5")
judge = media.Movie("The judge","El juez",
	"https://upload.wikimedia.org/wikipedia/en/6/61/The_Judge_2014_film_poster.jpg",
	"https://www.youtube.com/watch?v=ZBvK6ni97W8",
	"The relationship between one lawyer and his father is not easy when both are full of pride, but familiar love is above everything.",
	"2014","David Dobkin","Robert Downey Jr","Robert Duvall","5")
matrix = media.Movie("Matrix","La matriz",
	"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
	"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
	"A tasteless fictional film with nothing to offer to the viewer.",
	"1999","Andy Wachowski","Keanu Reeves","Laurence Fishburn","1")
titanic = media.Movie("Titanic","Titanic",
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
	"https://www.youtube.com/watch?v=ZfNEC36jZFY",
	"Full of commonplaces and cliches, made for massive selling, with lots of special effects, but with a significal lack of content.",
	"1997","James Cameron","Leonardo Di Caprio","Kate Winslet","2")
hobbit = media.Movie("The Hobbit: An Unexpected Journey","El hobbit",
	"https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
	"https://www.youtube.com/watch?v=5xpcwquIpRQ",
	"A hobbit with a normal life suddenly gets involved in a big adventure and has to prove his value to his partners.",
	"2012","Peter Jackson","Ian McKellen","Martin Freeman","4")
whiplash = media.Movie("Whiplash","Whiplash, Música y Obsesión",
	"https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
	"https://www.youtube.com/watch?v=7d_jQycdQGo",
	"A disciplined aspiring drum player wants to play with the most respected jazz director, but will learn that aweful people is aweful",
	"2014","Damien Chazelle","Milles Teller","J.K. Simmons","4,8")
birdman = media.Movie("Birdman or (The Unexpected Virtue of Ignorance)","Birdman",
	"https://upload.wikimedia.org/wikipedia/en/a/a3/Birdman_poster.jpg",
	"https://www.youtube.com/watch?v=uJfLoE6hanc",
	"An actor has his life marked by a film he once protagonized, and will live in a very gray world until his mind gets released.",
	"2014","Alejandro Gonzàlez IÐarritu","Michael Keaton","Edward Norton","4,7")
boyhood = media.Movie("Boyhood", "Momentos de una vida",
	"https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
	"https://www.youtube.com/watch?v=Y0oX0xiwOv8",
	"An inspiring vision of the growth of a normal boy in a normal family with the usual issues.",
	"2014","Richard Linkater","Patricia Arquette","Ellar Coltrane","4,6")
grand_hotel = media.Movie("The Grand Budapest Hotel","El Gran Hotel Budapest",
	"https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
	"https://www.youtube.com/watch?v=mXRztrOK47I",
	"An amazingly fictional story, based on the writings of Stefan Zweig. Tells the story of a supposed crime commited by the staff of a picturesque hotel.",
	"2014","Wes Anderson","Ralph Fiennes","F. Murray Abraham","5")
enigma = media.Movie("The imitation game","Código enigma",
	"https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
	"https://www.youtube.com/watch?v=nuPZUUED5uk",
	"One of the greatest computer scientists in history helps allies to win the war and changes the world forever, but his great achievements are denied because of his homosexuality.",
	"2014","Morten Tyldum","Benedict Cumberbatch","Keira Knightley","4,5")
theory_everything = media.Movie("A theory of everything","La teoría del todo",
	"https://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg",
	"https://www.youtube.com/watch?v=Salz7uGp72c",
	"The story of Stephen Hawking, from the conception of his biggest ideas to the difficult life he kept while his disease progressed.",
	"2014","James Marsh","Eddie Redmayne","Felicity Jones","4")
interstellar = media.Movie("Interstellar","Interestelar",
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=zSWdZVtXT7E",
	"A fictional film of how could humankind save itself in a postapocalliptic world.",
	"2014","Christopher Nolan","Matthew McConaughey","Anne Hathaway","4")
midnight_paris = media.Movie("Midnight in Paris","Medianoche en París",
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=FAfR8omt-CY",
	"A americanwriter struggles to get his opera prima done, while finds a chance to live a fictional romance in the Paris of other time.",
	"2011","Woody Allen","Kathy Bates","Owen Wilson","4,5")
blue_jasmin = media.Movie("Blue Jasmine","Blue Jasmine",
	"https://upload.wikimedia.org/wikipedia/en/3/3f/Blue_Jasmine_poster.jpg",
	"https://www.youtube.com/watch?v=FER3C394aI8",
	"Jasmine lives in a surreal world, escaping to the huge problemas she has in her life.",
	"2013","Woody Allen","Cate Blanchett","Alec Baldwin","4")
match_point = media.Movie("Match Point","Match Point",
	"https://upload.wikimedia.org/wikipedia/en/0/0a/MatchPointPoster.jpg",
	"https://www.youtube.com/watch?v=wISRAOb6xm0",
	"A former tennis instructor finds love and a path to have a better life, but then risks everything because of an affair with an untalented actress.",
	"2005","Woody Allen","Scarlett Johanson","Brian Cox","5")
alice = media.Movie("Still Alice","Siempre Alice",
	"https://upload.wikimedia.org/wikipedia/en/d/d2/Still_Alice_-_Movie_Poster.jpg",
	"https://www.youtube.com/watch?v=ZrXrZ5iiR0o",
	"A brilliant psychology teacher struggles to find herself despite an early onset Alzheimer's disease, that changes everything in her life.",
	"2015","Richard Glatzer","Julianne Moore","Alec Baldwin","4,9")
vie_en_rose = media.Movie("La vie en rose","La vida en rosa",
	"https://upload.wikimedia.org/wikipedia/en/c/cb/La_Vie_en_Rose_poster.jpg",
	"https://www.youtube.com/watch?v=xujvIs0DhJU",
	"Based in the life of Edith Piaf, shows the struggle of a very poor girl, that even when finally got succesful, was never very fortunate.",
	"2007","Olivier Dahan","Marion Cotillard","G_rard Depardieu","4,5")
casablanca = media.Movie("Casablanca","Casablanca",
	"https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
	"https://www.youtube.com/watch?v=BkL9l7qovsE",
	"With the second world war over their heads, a couple struggles to survive in foreign lands. ",
	"1942","Michael Curtiz","Humphrey Bogart","Ingrid Bergman","4,5")
general = media.Movie("The general","El maquinista de la General",
	"https://upload.wikimedia.org/wikipedia/en/5/59/The_General_poster.jpg",
	"https://www.youtube.com/watch?v=68lvPMCPWog",
	"A silent drama of a train engineer that looses his love during the US Civil War.",
	"1926","Buster Keaton","Buster Keaton","Marion Mack","4,5")
metropolis = media.Movie("Metropolis","Metrópolis",
	"https://upload.wikimedia.org/wikipedia/en/0/06/Metropolisposter.jpg",
	"https://www.youtube.com/watch?v=ObM0drwTshA",
	"A black and white film that alerts of what could happen in a society where technology is everything and humanity gets lost.",
	"1927","Fritz Lang","Alfred Abel","Brigitte Helm","4")
the_kid = media.Movie("The kid","El chico",
	"https://upload.wikimedia.org/wikipedia/commons/5/59/CC_The_Kid_1921.jpg",
	"https://www.youtube.com/watch?v=UBX2Yy2dqg4",
	"A silent comedy of Chaplin, in which a girl abandons his son in despair, and the kid is raised by a poor man, eventually helping him to commit some minor crimes.",
	"1921","Charlie Chaplin","Charlie Chaplin","Jackie Coogan","4")
wolf_wall_street = media.Movie("The wolf of Wall Street","El lobo de Wall Street",
	"https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
	"https://www.youtube.com/watch?v=idAVRvQeYAE",
	"Unethical Wall Street corridors fill their pockets with money, but eventually wont escape from reality.",
	"2013","Martin Scorsese","Leonardo Di Caprio","Matthew McConaughey","4,2")
_12_years_slave = media.Movie("12 years a slave","12 años de esclavitud",
	"https://upload.wikimedia.org/wikipedia/en/5/5c/12_Years_a_Slave_film_poster.jpg",
	"https://www.youtube.com/watch?v=KrDg_6rxCzs",
	"A free living african american musician, is hijacked from the North, and taken to live to the South as an slave.",
	"2013","Steve McQueen","Chiwetel Ejiofor","Michael Fassbender","4,5")
slumdog_millionaire = media.Movie("Slumdog millionaire","Quién quiere ser millonario",
	"https://upload.wikimedia.org/wikipedia/en/f/fe/Slumdog_millionaire_ver2.jpg",
	"https://www.youtube.com/watch?v=AIzbwV7on6Q",
	"A couple of brothers struggle to live a poor life in a though gettho in Mumbai.",
	"2008","Danny Boyle","Dev Patel","Freida Pinto","4")
social_network = media.Movie("The social network","La red social",
	"https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
	"https://www.youtube.com/watch?v=2RB3edZyeYw","The story behind facebook.",
	"2010","David Fincher","Jesse Eisenberg","ustin Timberlake","3,8")


movies = [shawshank, dark_knight, batman_begins, dark_knight_rises, million_dollar, gran_torino, judge, matrix, titanic, hobbit, whiplash, birdman, boyhood, grand_hotel, enigma, theory_everything, interstellar, midnight_paris, blue_jasmin, match_point, alice, vie_en_rose, casablanca, general, metropolis, the_kid, wolf_wall_street, _12_years_slave, slumdog_millionaire, social_network]

# Call of fresh tomatoes, to generate the web page, with the list movies as parameter.
fresh_tomatoes.open_movies_page(movies)
