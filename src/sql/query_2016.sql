SELECT 
        Año,
        Grupo,
        Tipo,
        sum( pago )
FROM Payments_2016
group by Grupo, Tipo
