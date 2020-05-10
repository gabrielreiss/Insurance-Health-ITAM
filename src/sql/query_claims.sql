SELECT 
        count(*) as quantidade,
        avg( `Number of claims` ) as claims

FROM Diseases_per_person
GROUP BY `Number of claims`;