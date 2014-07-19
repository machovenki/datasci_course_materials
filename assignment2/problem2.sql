// Big words sql statement

select count(1) from
(
select docid, sum(count) as t_ct from frequency group by docid having t_ct > 300
);

// Two words SQL statement

select
    count(t.docid)
from
    frequency t
    , frequency w
where
    t.term = 'transactions'
    and
    w.term = 'world'
    and 
    t.docid = w.docid;
