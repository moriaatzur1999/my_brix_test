
CREATE TABLE "products" (catID integer  , Name varchar(20) PRIMARY KEY, price integer, FOREIGN KEY(catID) REFERENCES cat(ID));
CREATE TABLE "cat" (ID integer PRIMARY KEY, Name varchar(20));