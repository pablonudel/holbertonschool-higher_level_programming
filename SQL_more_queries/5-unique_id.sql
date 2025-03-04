-- creates the table unique_id
CREATE TABLE if NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);