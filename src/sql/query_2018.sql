SELECT 
        Año,
        Grupo,
        Tipo,
        sum( pago )
FROM Payments_2018
group by Grupo, Tipo
