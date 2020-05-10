SELECT DISTINCT t1.Grupo, 
                case when soma_2015 is NULL then 0 else soma_2015 end as soma_2015,
                case when soma_2016 is NULL then 0 else soma_2016 end as soma_2016,
                case when soma_2017 is NULL then 0 else soma_2017 end as soma_2017,
                case when soma_2018 is NULL then 0 else soma_2018 end as soma_2018
FROM (
    SELECT  *

    FROM ( 
        SELECT Grupo
        FROM Payments_2018
        group by Grupo
    )

    UNION ALL
        SELECT Grupo
        FROM Payments_2017
        group by Grupo

    UNION ALL
            SELECT  Grupo
        FROM Payments_2016
        group by Grupo

    UNION ALL
            SELECT  Grupo
        FROM Payments_2015
        group by Grupo

    ) AS t1

LEFT JOIN (
    SELECT 
        Grupo,
        
        sum( pago ) as soma_2018
    FROM Payments_2018
    group by Grupo
) AS t2018
ON t1.Grupo = t2018.Grupo

LEFT JOIN (
    SELECT 
        Grupo,
        
        sum( pago ) as soma_2017
    FROM Payments_2017
    group by Grupo
) AS t2017
ON t1.Grupo = t2017.Grupo

LEFT JOIN (
    SELECT 
        Grupo,
        
        sum( pago ) as soma_2016
    FROM Payments_2016
    group by Grupo
) AS t2016
ON t1.Grupo = t2016.Grupo

LEFT JOIN (
    SELECT 
        Grupo,
        
        sum( pago ) as soma_2015
    FROM Payments_2015
    group by Grupo
) AS t2015
ON t1.Grupo = t2015.Grupo

order by t1.Grupo
;