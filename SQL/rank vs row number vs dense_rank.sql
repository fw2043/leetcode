
---RANK vs DENSE_RANK vs ROW_NUMBER functions
--If there is a tie between two scores, you can use rank or dense_rank(If there is a tie between two scores, both should have the same ranking.,
	--After a tie, the next ranking number should be the next consecutive integer value)
-- If you want ranks with gaps, you can use rank()
----row_number will not give you a tie, just add row number for them