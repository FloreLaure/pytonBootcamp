## 1
SELECT first_name as Firstname, last_name as Lastname FROM employees;

## 2
SELECT DISTINCT(department_id) FROM employees;

## 3
SELECT * FROM employees ORDER BY first_name DESC;

## 4
SELECT first_name as PRENOM, last_name as NOM, salary as SALAIRE, (salary*0.15) as PF FROM employees;

## 5
SELECT employee_id, first_name as PRENOM, last_name as NOM, salary as SALAIRE FROM employees ORDER BY salary ASC;

## 6
SELECT SUM(salary) as SALIRE_TOTAL FROM employees;

## 7
SELECT MAX(salary) AS SALAIRE_MAXIMAL, MIN(salary) as SALAIRE_MINIMAL FROM employees;

## 8
SELECT AVG(salary) as SALAIRE_MOYEN FROM employees;

## 9
SELECT COUNT(employee_id) AS NOMBRE_TRAVAILLEUR FROM employees;

## 10
SELECT UPPER(first_name) FROM employees;

## 11
SELECT SUBSTRING(first_name for 3) FROM employees;

## 12
SELECT CONCAT(first_name, ' ', last_name) as IDENTITE FROM employees;

## 13
SELECT first_name, last_name, CHAR_LENGTH(first_name)+CHAR_LENGTH(last_name) as LONGUEUR_NOM_COMPLET FROM employees;

## 14
SELECT first_name FROM employees WHERE first_name ~ '^[0-9]$';

## 15
SELECT * FROM employees LIMIT 10;



## parti 2


## 1
SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 and 15000;

## 2
SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN '1987-01-01' and '1987-12-31';

## 3
SELECT * FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';

## 4
 SELECT employees.last_name, jobs.job_title, employees.salary 
 FROM employees JOIN jobs ON jobs.job_id = employees.job_id 
 WHERE jobs.job_id NOT IN (SELECT DISTINCT jobs.job_id
      FROM jobs
      WHERE jobs.job_title = 'Programmer'
    ) AND employees.salary NOT IN (4500, 10000, 15000);

## 5
SELECT last_name FROM employees WHERE CHAR_LENGTH(last_name) = 6;

## 6
SELECT last_name FROM employees WHERE SUBSTRING(last_name FROM 3 for 1) LIKE '%e%';

## 7
SELECT DISTINCT(jobs.job_title) FROM jobs JOIN employees ON jobs.job_id = employees.job_id;

## 8
SELECT * FROM employees WHERE last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')



