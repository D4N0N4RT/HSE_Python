-- Create the client_info table
CREATE TABLE client_info (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    registration_address VARCHAR(255) NOT NULL,
    last_known_location VARCHAR(255) NOT NULL
);

-- Insert sample data into the client_info table
INSERT INTO client_info (user_id, name, registration_address, last_known_location) VALUES
(1, 'John Doe', 'New York', 'Los Angeles'),
(2, 'Jane Smith', 'Chicago', 'San Francisco'),
(3, 'Michael Johnson', 'Houston', 'Austin'),
(4, 'Emily Davis', 'Miami', 'Orlando'),
(5, 'Chris Brown', 'Boston', 'New York'),
(6, 'Anna White', 'Seattle', 'Portland'),
(7, 'David Miller', 'San Diego', 'Las Vegas'),
(8, 'Laura Wilson', 'Philadelphia', 'Washington DC'),
(9, 'Kevin Lee', 'Denver', 'Chicago'),
(10, 'Sophia Martinez', 'Phoenix', 'San Jose');