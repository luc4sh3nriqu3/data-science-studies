SELECT seller_id,
        sum(t1.price) as totalRevenue,
        count(distinct t1.order_id) as qtSalles

FROM tb_order_items as t1

GROUP BY seller_id;