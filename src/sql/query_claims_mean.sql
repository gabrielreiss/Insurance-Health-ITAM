SELECT 
        count(*) as quantidade,
        avg( `Number of claims` ) as prop

FROM Diseases_per_person;