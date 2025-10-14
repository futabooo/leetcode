--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below

WITH temp_with_prev AS (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
)
SELECT id
FROM temp_with_prev
WHERE temperature > prev_temperature
  AND DATEDIFF(recordDate, prev_date) = 1;
-- @lc code=end

