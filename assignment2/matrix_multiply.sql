// Simple matrix multiplication

select val from
(
select a.row_num r, b.col_num c, sum(a.value * b.value) as val from a, b where a.col_num = b.row_num group by r,c having r=2 and c=3
);

