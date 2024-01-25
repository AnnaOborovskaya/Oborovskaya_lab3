Для создания таблиц в postgre:

CREATE TABLE users(
	id_user SERIAL PRIMARY KEY,
	Name TEXT NOT NULL,
	district text[]
 );

CREATE TABLE orders(
	id_order SERIAL PRIMARY KEY,
	Name TEXT NOT NULL,
	district text,
	status INTEGER, 
	id_user INTEGER,
	FOREIGN KEY (id_user) REFERENCES users (id_user)
);
