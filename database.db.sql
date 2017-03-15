sqlite> .fullschema
CREATE TABLE Companies (
    ID INT PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Owners TEXT,
    Revenue INT,
    total_board INT,
    percent_women INT
 );

CREATE TABLE People (
    First_Name TEXT,
    Last_Name TEXT,
    isCEO TEXT,
    Gender TEXT, 
);

INSERT INTO Companies(Name, Owners, Revenue, total_board, percent_women)    
VALUES(Walmart, Rob Walton, 378800000000, 12, 25);

