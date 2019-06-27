# Name-Database-Generator
Through a python script, a database will be created and uploaded with random fake identifications, generated automatically

--------------------
Auto-generate a (FAKE POPULATION) DB of :
- names (Family & First)
- Social Security Number (French) > Unique 
- Female/Male
- Date of Birth (Full dd/mm/yyyy)
- Area/City of Birth (minima in France, and/or if possible whole world)
- email
- Postal Address in France (Random) - If possible to generate
- Phone Number (Cellphone/Landline)
- Car Registration Number (French)
- Car description
- Password Management with Hash

---------------------
Tools :
- Python 3.7 (Or Upper) - MVC Structure approach
- MySQL
- SQLAlchemy
- Pandas
- Flask ? - *For Reading and interface with the database after creating it.*
- Django ? - *For Reading and interface with the database after creating it.*
- Hash python module ? bcrypt? SHA256? | Using a Salt and pepper to the Hash? >> **pip install bcrypt** | [bcrypt 3.1.7](https://pypi.org/project/bcrypt/)
- Crypto python module for cryptographic related random generation ?

-----------------------
Constructions Steps:
- [ ] Ask input at beginning, How many people shall we generate, to populate our FICTIONAL database.
- [ ] Generate a RANDOMISED French Social Security Number.
- [ ] From Social Security Number, determine if Male/Female.
- [ ] From M/F SecSoc > Pick Random First Name (Corresponding M/F).
- [ ] From SecSoc, Extract Birth Date : Year & Month ; Randomly pick a Day in the month >> Store it as Datetime.date Object.
- [ ] From Sec Soc, Extract Region of Birth (Department number).
- [ ] From Soc Sec, Extract and compare: City of birth registration etc (up to remainder of last 3 totally random numbers.
- [ ] From SocSec,  compute the security/validation Key > Extra 2 digits.
- [ ] With a REGEX, generate a random-ish email: FirstName[.-_""+]FamNamae@[gmail, yahoo, bogus].[com, org, fr, co.uk, de, net, tv, etc].
- [ ] With few rules (a regex?) generate a random-ish Phone number (Cellphone Only? Or Fixe and/or cellphone? If Fixe Landline, what about Area code?).
- [ ] Export all data into a MySQL DB (Multiple crossreferenced tables possible).
- [ ] Small interface, to read and parse data from MySQL database. Read and Update data.

---------------------------
Questions:
- [ ] **ATTENTION:** For Social Sec Number, Telephone, & Car Reg Num >>> *If already exist = No Repeating data == Need to be Unique*.
- [ ] Can we generate a random-ish postal address (dependent from fix phone number area code) ? how to make it Work? Open source map? GPS coordinates?
- [ ] Does this script generate France metropolitan Social Security Numbers ONLY? What About *Corsica* **2A** & **2B**? What About *Overseas Departments* (**97** and **98**)? What About *Foreigners* (**99**, and their corresponding country of birth, in next digits)?
- [ ] What Display for Reading data? > HTML, CSS, JS ??? W/ Django OR Flask?
- [ ] Through a Login for this interface (Username & Password management) administrating *different* ***user rights*** *management*: Data Admin = Read & Update & Create New, Simple User = Read Only.
- [ ] Can I create a random Car registration number and car database? > Randomly create a **Car Registration Number**, *Randomly assign it to a Car type*, and then Randomly assign it to a Fact-person in Database. (Multiple cross ref data tables).
- [ ] Can we create a **Random Password Generator** > to store as *SHA/HASH* in a DB Table for each populated DB fake-person ?
- [ ] All extra *small* script, HOW? WHEN? Do they update the database? ALL in 1? Or 1 after the Other, Parsing the DB and updating afterward?
- [ ] For **Testing purposed**, Export a csv file with a Unique Identifier (e.g. SocSecNum), the Plain Text Password, and The Hash fingerprint. **Obviously in a real-world dev/production such export wouldn't exist**.
- [ ] How to Store the Hash & Salt in the MySQL Database? Should they be Join into a single String, OR stored separately in 2 different Tables?