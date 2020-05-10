SELECT DISTINCT t1.Grupo, 
                t1.Tipo,
                case when soma_2015 is NULL then 0 else soma_2015 end as soma_2015,
                case when soma_2016 is NULL then 0 else soma_2016 end as soma_2016,
                case when soma_2017 is NULL then 0 else soma_2017 end as soma_2017,
                case when soma_2018 is NULL then 0 else soma_2018 end as soma_2018
FROM (
    SELECT  *

    FROM ( 
        SELECT Tipo, Grupo
        FROM Payments_2018
        group by Grupo, Tipo
    )

    UNION ALL
        SELECT Tipo, Grupo
        FROM Payments_2017
        group by Grupo, Tipo

    UNION ALL
            SELECT Tipo, Grupo
        FROM Payments_2016
        group by Grupo, Tipo

    UNION ALL
            SELECT Tipo, Grupo
        FROM Payments_2015
        group by Grupo, Tipo

    ) AS t1

LEFT JOIN (
    SELECT 
        Grupo,
        Tipo,
        sum( pago ) as soma_2018
    FROM Payments_2018
    group by Grupo, Tipo
) AS t2018
ON t1.Grupo = t2018.Grupo
AND t1.Tipo = t2018.Tipo

LEFT JOIN (
    SELECT 
        Grupo,
        Tipo,
        sum( pago ) as soma_2017
    FROM Payments_2017
    group by Grupo, Tipo
) AS t2017
ON t1.Grupo = t2017.Grupo
AND t1.Tipo = t2017.Tipo

LEFT JOIN (
    SELECT 
        Grupo,
        Tipo,
        sum( pago ) as soma_2016
    FROM Payments_2016
    group by Grupo, Tipo
) AS t2016
ON t1.Grupo = t2016.Grupo
AND t1.Tipo = t2016.Tipo

LEFT JOIN (
    SELECT 
        Grupo,
        Tipo,
        sum( pago ) as soma_2015
    FROM Payments_2015
    group by Grupo, Tipo
) AS t2015
ON t1.Grupo = t2015.Grupo
AND t1.Tipo = t2015.Tipo

order by t1.Grupo, t1.Tipo
;