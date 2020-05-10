SELECT 
    t1.Grupo,
    t1.Tipo,
    soma_2015,
    soma_2016,
    soma_2017,
    soma_2018

FROM ( 
    SELECT 
        Año,
        Grupo,
        Tipo,
        sum( pago ) as soma_2018
    FROM Payments_2018
    group by Grupo, Tipo
) AS t1

LEFT OUTER JOIN(
    SELECT 
            Año,
            Grupo,
            Tipo,
            sum( pago ) as soma_2017
    FROM Payments_2017
    group by Grupo, Tipo
) AS t2
ON t1.Grupo = t2.Grupo
AND t1.Tipo = t2.Tipo

LEFT OUTER JOIN(
        SELECT 
            Año,
            Grupo,
            Tipo,
            sum( pago ) as soma_2016
    FROM Payments_2016
    group by Grupo, Tipo
) AS t3
ON t1.Grupo = t3.Grupo
AND t1.Tipo = t3.Tipo

LEFT OUTER JOIN(
        SELECT 
            Año,
            Grupo,
            Tipo,
            sum( pago ) as soma_2015
    FROM Payments_2015
    group by Grupo, Tipo
) AS t4
ON t1.Grupo = t4.Grupo
AND t1.Tipo = t4.Tipo