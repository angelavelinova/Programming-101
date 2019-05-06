SELECT name, country, numguns, launched 
from ships
join classes on classes.class = ships.class

SELECT name, classes.class, country, numguns, launched 
FROM classes
left join ships on classes.class = ships.class
where classes.class in (select name from ships)

SELECT ships.name
FROM ships
join outcomes on outcomes.ship = ships.name
join battles on battles.name = outcomes.battle
WHERE date like '%1942%'

SELECT country, count(*)
FROM classes
left join ships on classes.class = ships.class
left join outcomes on outcomes.ship = ships.name
WHERE battle is null
GROUP BY country
