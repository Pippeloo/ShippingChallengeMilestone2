-- Create a table
CREATE TABLE data (
  id SERIAL PRIMARY KEY,
  name varchar NOT NULL
);

-- Insert some data
INSERT INTO data (name) VALUES
('Jules Torfs');