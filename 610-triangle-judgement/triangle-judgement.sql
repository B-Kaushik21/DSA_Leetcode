SELECT x,y,z,   
    CASE
        WHEN x<0 AND y<0 AND z<0 THEN 'No'
        WHEN x=y AND y=z THEN 'Yes'
        WHEN (x+y)>z AND (x+z)>y AND (z+y)>x THEN 'Yes'
        ELSE 'No' 
    END AS 'triangle'
FROM Triangle