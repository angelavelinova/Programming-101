SELECT avg(speed)
FROM pc

SELECT maker, avg(screen) 
FROM laptop 
left join product on laptop.model = product.model 
GROUP BY maker 

SELECT avg(speed)
FROM laptop
WHERE price > 1000

SELECT hd, avg(price)
FROM PC
GROUP BY hd

SELECT speed, avg(price)
FROM pc
WHERE speed > 500
GROUP BY speed

SELECT avg(price) 
FROM pc 
left join product on pc.model = product.model 
WHERE maker = 'A'

SELECT avg(laptop.price)
FROM product
JOIN laptop ON laptop.model = product.model
WHERE product.maker = 'B'
UNION
SELECT avg(pc.price)
FROM product
join pc on pc.model = product.model
WHERE product.maker = 'B'


SELECT maker
FROM product
WHERE type = 'PC'
GROUP BY maker
HAVING count(type) >= 3;

SELECT maker, price 
FROM product 
join pc on product.model = pc.model 
WHERE pc.price = (SELECT max(price)
									FROM pc)

SELECT avg(ram)
FROM pc
WHERE model in (SELECT  model
								FROM product
								WHERE maker in (SELECT maker 
																FROM product
																WHERE model in (SELECT model
																								FROM printer)))

