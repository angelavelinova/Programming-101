CREATE TABLE Languages( 
			user_id INTEGER PRIMARY KEY, 
			language TEXT, 
			answer TEXT, 
			answered BOOLEAN,                                                       
			guide TEXT)  
     
insert into Languages values (1, 'Python', 'google',0,'A folder named 
		  Python was created. Go there and fight with program.py!')
insert into Languages values (2, 'Go', '200 OK',0,'A folder named Go w
		  as created. Go there and try to make Google Go run.')
insert into Languages values (3, 'Java', 'object oriented programming'
		  ,0,'A folder named Java was created. Can you handle the class?')
insert into Languages values (4, 'Haskell', 'Lambda',0,'Something pure
		   has landed. Go to Haskell folder and see it!')
insert into Languages values (5, 'C#', 'NDI=',0,'Do you see sharp? Go 
		  to the C# folder and check out.')
insert into Languages values (6, 'Ruby', 'https://www.ruby-lang.org/bg
		  /',0,'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!')
insert into Languages values (7, 'C++', 'header files',0,'Here be dragons! It is C++ time. Go to the C++ folder.')
	
ALTER TABLE `Languages` 
ADD COLUMN rating int; 
      
UPDATE languages 
SET answered = 1 
WHERE language = "Python" or language = "Go";

SELECT language 
FROM `Languages` 
WHERE answer = "200 OK" or answer = "Lambda";
