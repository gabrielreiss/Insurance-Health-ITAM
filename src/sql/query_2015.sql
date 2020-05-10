SELECT 
        Año,
        Grupo,
        Tipo,
        sum( pago )
FROM Payments_2015
group by Grupo, Tipo
