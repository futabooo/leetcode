--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below

DELETE e1 FROM Person e1, Person e2 
WHERE e1.Email = e2.Email AND e1.Id > e2.Id;

-- @lc code=end

