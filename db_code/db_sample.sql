
SELECT d.name
FROM Department d
JOIN Employee e ON d.id = e.department_id
JOIN Salary_Payments sp ON e.id = sp.employee_id
WHERE sp.date >= NOW() - INTERVAL '3 months'
GROUP BY d.id, d.name
HAVING COUNT(DISTINCT e.id) > 10;