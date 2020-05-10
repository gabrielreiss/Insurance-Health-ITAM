SELECT 
        Año,
        Grupo,
        Tipo,
        sum( pago )
FROM Payments_2017
group by Grupo, Tipo
