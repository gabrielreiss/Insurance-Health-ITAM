SELECT Año, Tipo, Grupo, Pago
FROM (
    select *
    from Payments_2015

    UNION ALL

    select *
    from Payments_2016

    UNION ALL

    select *
    from Payments_2017

    UNION ALL

    select *
    from Payments_2018
);