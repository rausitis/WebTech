--Database Movie Lib

-- UserInfo Table

CREATE TABLE UserInfo (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,  -- Assuming password is stored as a hashed string
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    age VARCHAR(10),
    gender VARCHAR(50),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    createdBy VARCHAR(255),
    modifiedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modifiedBy VARCHAR(255),
    matureContent BOOLEAN,
    authRoles VARCHAR(50) CHECK (authRoles IN ('USER', 'ADMIN'))
);

-- Populate UserInfo with users (regular and admin)
INSERT INTO UserInfo (username, password, firstname, lastname, age, gender, createdBy, matureContent, authRoles)
VALUES 
('paxinte', 'hashed_password1', 'Paul', 'Axinte', '24', 'Male', 'admin', FALSE, 'USER'),
('efickova', 'hashed_password2', 'Eugenia', 'Fickova', '22', 'Female', 'admin', TRUE, 'ADMIN'),
('apinto', 'hashed_password3', 'Alexandre', 'Pinto', '29', 'Male', 'admin', FALSE, 'USER'),
('rmiglava', 'hashed_password4', 'Ruta', 'Miglava', '23', 'Female', 'admin', FALSE, 'USER'),
('sgraczykowski', 'hashed_password5', 'Stanislaw', 'Graczykowski', '21', 'Male', 'admin', TRUE, 'USER');


-- Roles Table
CREATE TABLE Roles (
    id SERIAL PRIMARY KEY,
    role VARCHAR(50) CHECK (role IN ('USER', 'ADMIN')),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    createdBy VARCHAR(255),
    modifiedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modifiedBy VARCHAR(255)
);

-- Populate Roles with data
INSERT INTO Roles (role, createdBy)
VALUES 
('USER', 'admin'),
('ADMIN', 'admin');


-- AuthToken Table
CREATE TABLE AuthToken (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    token VARCHAR(255) UNIQUE NOT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    createdBy VARCHAR(255),
    modifiedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modifiedBy VARCHAR(255)
);

-- Populate AuthToken with tokens
INSERT INTO AuthToken (username, token, createdBy)
VALUES 
('paxinte', 'token_paxinte', 'admin'),
('efickova', 'token_efickova', 'admin'),
('apinto', 'token_apinto', 'admin'),
('rmiglava', 'token_rmiglava', 'admin'),
('sgraczykowski', 'token_sgraczykowski', 'admin');


-- Content Table
CREATE TABLE Content (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    matureContent BOOLEAN,
    type VARCHAR(50) CHECK (type IN ('MOVIE', 'SERIES')),
    cast_members TEXT[] NOT NULL, -- PostgreSQL array to store multiple actors
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    createdBy VARCHAR(255),
    modifiedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modifiedBy VARCHAR(255)
);

-- Populate Content 
INSERT INTO Content (title, description, matureContent, type, cast_members, createdBy)
VALUES 
('Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.', TRUE, 'MOVIE', ARRAY['Leonardo DiCaprio', 'Joseph Gordon-Levitt'], 'admin'),
('Stranger Things', 'When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.', FALSE, 'SERIES', ARRAY['Millie Bobby Brown', 'David Harbour'], 'admin'),
('The Matrix', 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.', TRUE, 'MOVIE', ARRAY['Keanu Reeves', 'Laurence Fishburne'], 'admin'),
('The Witcher', 'The Witcher follows the story of Geralt of Rivia, a solitary monster hunter, who struggles to find his place in a world where people often prove more wicked than monsters and beasts. But when destiny hurtles him toward a powerful sorceress, and a young princess with a special gift, the three must learn to navigate independently the increasingly volatile Continent.', TRUE, 'SERIES', ARRAY['Henry Cavill', 'Anya Chalotra'], 'admin'),
('Breaking Bad', 'Breaking Bad follows Walter White, a struggling, frustrated high school chemistry teacher who becomes a crimelord in the local methamphetamine drug trade, driven to provide for his family financially after being diagnosed with inoperable lung cancer.', TRUE, 'SERIES', ARRAY['Bryan Cranston', 'Aaron Paul'], 'admin'),
('Game of Thrones', 'Nine noble families wage war against each other in order to gain control over the mythical land of Westeros.', TRUE, 'SERIES', ARRAY['Emilia Clarke', 'Kit Harington', 'Peter Dinklage', 'Lena Headey', 'Nikolaj Coster-Waldau', 'Sophie Turner', 'Maisie Williams', 'Iain Glen', 'Conleth Hill', 'Gwendoline Christie'], 'admin'),
('The Avengers', 'Earth''s mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.', TRUE, 'MOVIE', ARRAY['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Tom Hiddleston', 'Samuel L. Jackson', 'Cobie Smulders', 'Clark Gregg'], 'admin'),
('Friends', 'Follows the personal and professional lives of six twenty to thirty-something-year-old friends living in Manhattan.', FALSE, 'SERIES', ARRAY['Jennifer Aniston', 'Courteney Cox', 'Lisa Kudrow', 'Matt LeBlanc', 'Matthew Perry', 'David Schwimmer', 'James Michael Tyler', 'Maggie Wheeler', 'Elliott Gould', 'Christina Pickles'], 'admin'),
('The Dark Knight', 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.', TRUE, 'MOVIE', ARRAY['Christian Bale', 'Heath Ledger', 'Aaron Eckhart', 'Michael Caine', 'Maggie Gyllenhaal', 'Gary Oldman', 'Morgan Freeman', 'Eric Roberts', 'Cillian Murphy', 'Chin Han'], 'admin'),
('The Mandalorian', 'The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.', FALSE, 'SERIES', ARRAY['Pedro Pascal', 'Carl Weathers', 'Gina Carano', 'Giancarlo Esposito', 'Werner Herzog', 'Nick Nolte', 'Taika Waititi', 'Emily Swallow', 'Omid Abtahi', 'Amy Sedaris'], 'admin'),
('Titanic', 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.', TRUE, 'MOVIE', ARRAY['Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane', 'Kathy Bates', 'Frances Fisher', 'Danny Nucci', 'Jonathan Hyde', 'Bernard Hill', 'David Warner', 'Bill Paxton'], 'admin'),
('Sherlock', 'A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.', FALSE, 'SERIES', ARRAY['Benedict Cumberbatch', 'Martin Freeman', 'Una Stubbs', 'Rupert Graves', 'Louise Brealey', 'Andrew Scott', 'Mark Gatiss', 'Amanda Abbington', 'Vinette Robinson', 'Jonathan Aris'], 'admin'),
('Avatar', 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', TRUE, 'MOVIE', ARRAY['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver', 'Stephen Lang', 'Giovanni Ribisi', 'Michelle Rodriguez', 'Laz Alonso', 'CCH Pounder', 'Wes Studi', 'Joel David Moore'], 'admin'),
('Breaking Bad', 'A high school chemistry teacher turned methamphetamine manufacturing kingpin partners with a former student in a dangerous drug trade.', TRUE, 'SERIES', ARRAY['Bryan Cranston', 'Aaron Paul', 'Anna Gunn', 'Dean Norris', 'Betsy Brandt', 'RJ Mitte', 'Bob Odenkirk', 'Jonathan Banks', 'Giancarlo Esposito', 'Jesse Plemons'], 'admin'),
('Pulp Fiction', 'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.', TRUE, 'MOVIE', ARRAY['John Travolta', 'Uma Thurman', 'Samuel L. Jackson', 'Bruce Willis', 'Ving Rhames', 'Harvey Keitel', 'Tim Roth', 'Amanda Plummer', 'Eric Stoltz', 'Rosanna Arquette'], 'admin'),
('Stranger Things', 'When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.', FALSE, 'SERIES', ARRAY['Millie Bobby Brown', 'David Harbour', 'Winona Ryder', 'Finn Wolfhard', 'Gaten Matarazzo', 'Caleb McLaughlin', 'Natalia Dyer', 'Charlie Heaton', 'Cara Buono', 'Noah Schnapp'], 'admin'),
('Harry Potter and the Sorcerer''s Stone', 'An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.', TRUE, 'MOVIE', ARRAY['Daniel Radcliffe', 'Emma Watson', 'Rupert Grint', 'Richard Harris', 'Maggie Smith', 'Robbie Coltrane', 'Alan Rickman', 'Tom Felton', 'John Hurt', 'Ian Hart'], 'admin'),
('The Crown', 'Follows the political rivalries and romance of Queen Elizabeth II''s reign and the events that shaped the second half of the twentieth century.', FALSE, 'SERIES', ARRAY['Claire Foy', 'Matt Smith', 'Olivia Colman', 'Helena Bonham Carter', 'Tobias Menzies', 'Josh O''Connor', 'Emma Corrin', 'Vanessa Kirby', 'John Lithgow', 'Charles Dance'], 'admin'),
('Interstellar', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity''s survival.', TRUE, 'MOVIE', ARRAY['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain', 'Michael Caine', 'Casey Affleck', 'Timothée Chalamet', 'Bill Irwin', 'Mackenzie Foy', 'Topher Grace', 'David Gyasi'], 'admin'),
('The Office', 'A mockumentary on a group of typical office workers, where the workday consists of ego clashes, inappropriate behavior, and tedium.', FALSE, 'SERIES', ARRAY['Steve Carell', 'Rainn Wilson', 'John Krasinski', 'Jenna Fischer', 'Mindy Kaling', 'B.J. Novak', 'Ed Helms', 'Angela Kinsey', 'Brian Baumgartner', 'Oscar Nunez'], 'admin'),
('The Godfather', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', TRUE, 'MOVIE', ARRAY['Marlon Brando', 'Al Pacino', 'James Caan', 'Robert Duvall', 'Diane Keaton', 'Talia Shire', 'Sterling Hayden', 'Richard S. Castellano', 'John Marley', 'Richard Conte'], 'admin'),
('Black Mirror', 'An anthology series exploring a twisted, high-tech multiverse where humanity''s greatest innovations and darkest instincts collide.', TRUE, 'SERIES', ARRAY['Bryce Dallas Howard', 'Daniel Kaluuya', 'Mackenzie Davis', 'Jon Hamm', 'Cristin Milioti', 'Jesse Plemons', 'Rosemarie DeWitt', 'Alex Lawther', 'Andrew Scott', 'Fionn Whitehead'], 'admin'),
('The Lord of the Rings: The Fellowship of the Ring', 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.', TRUE, 'MOVIE', ARRAY['Elijah Wood', 'Ian McKellen', 'Viggo Mortensen', 'Orlando Bloom', 'Sean Astin', 'John Rhys-Davies', 'Billy Boyd', 'Dominic Monaghan', 'Liv Tyler', 'Cate Blanchett'], 'admin'),
('House of Cards', 'A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.', TRUE, 'SERIES', ARRAY['Kevin Spacey', 'Robin Wright', 'Michael Kelly', 'Kate Mara', 'Corey Stoll', 'Sakina Jaffrey', 'Molly Parker', 'Mahershala Ali', 'Elizabeth Marvel', 'Gerald McRaney'], 'admin'),
('Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', TRUE, 'MOVIE', ARRAY['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page', 'Tom Hardy', 'Ken Watanabe', 'Cillian Murphy', 'Marion Cotillard', 'Michael Caine', 'Tom Berenger', 'Lukas Haas'], 'admin');

-- Admin Table
CREATE TABLE Admin (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password TEXT NOT NULL,  -- Assuming password is stored as a hashed string
    role VARCHAR(50) CHECK (role = 'ADMIN')
);

-- Populate Admin with 1 admin user
INSERT INTO Admin (username, password, role)
VALUES 
('efickova', 'hashed_password2', 'ADMIN');
