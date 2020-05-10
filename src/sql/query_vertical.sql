SELECT *

FROM ( 
    SELECT 
        Año,
        Grupo,
        Tipo,
        sum( pago ) as soma
    FROM Payments_2018
    group by Grupo, Tipo
) AS t1

UNION ALL
    SELECT 
            Año,
            Grupo,
            Tipo,
            sum( pago ) as soma
    FROM Payments_2017
    group by Grupo, Tipo

UNION ALL
        SELECT 
            Año,
            Grupo,
            Tipo,
            sum( pago ) as soma
    FROM Payments_2016
    group by Grupo, Tipo

UNION ALL
        SELECT 
            Año,
            Grupo,
            Tipo,
            sum( pago ) as soma
    FROM Payments_2015
    group by Grupo, Tipo
;