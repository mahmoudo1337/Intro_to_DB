CREATE DATABASE IF NOT EXISTS alx_book_store

CREATE TABLE Books (
    book_id PRIMARY KEY,
    title VARCHAR(30),
    FOREIGN KEY (author_id) REFERENCES (Authors),
    price DOUBLE,
    publication_date DATE
)

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
)

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215)
    email VARCHAR(215)
    address TEXT
)

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    Foreign Key (customer_id) REFERENCES Customers(customer_id),
    order_date DATE
)

CREATE TABLE Order_Details(
    orderdetail_id INT PRIMARY KEY,
    Foreign Key (order_id) REFERENCES (Orders),
    Foreign Key (book_id) REFERENCES (Books),
    quantity DOUBLE
)