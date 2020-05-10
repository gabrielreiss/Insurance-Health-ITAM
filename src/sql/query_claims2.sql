SELECT 
        count(*) as quantidade,
        avg( `Number of claims` ) as claims,
        CAST (count(*) AS FLOAT) / 
        CAST ( (select count(*) from Diseases_per_person) AS FLOAT) AS prob

FROM Diseases_per_person
GROUP BY `Number of claims`;