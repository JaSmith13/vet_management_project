DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    qualifications VARCHAR(255),
    contact_number VARCHAR(255),
    is_active BOOLEAN
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact_number VARCHAR(255),
    address TEXT, 
    email VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE,
    breed VARCHAR(255),
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id)
);

INSERT INTO vets (first_name, last_name, qualifications, contact_number, is_active)
VALUES ('Aileen', 'Matthews', 'MRCVS', '07865 123456', TRUE);

INSERT INTO vets (first_name, last_name, qualifications, contact_number, is_active)
VALUES ('Roland', 'Walters', 'FRCVS', '01234 987654', FALSE);

INSERT INTO vets (first_name, last_name, qualifications, contact_number, is_active)
VALUES ('Rachel', 'Mcfarlane', 'MRCVS', '07531 246810', TRUE);

INSERT INTO owners (first_name, last_name, contact_number, address, email)
VALUES ('Daniel', 'Johnson', '07891 654321', 'deviltown', 'djohnson@gmail.com');

INSERT INTO pets (name, date_of_birth, breed, owner_id, treatment_notes, vet_id)
VALUES ('Stanley', '01/07/2018', 'cocker spaniel', 1, 'allergic to meat', 1);

INSERT INTO pets (name, date_of_birth, breed, owner_id, treatment_notes, vet_id)
VALUES ('Sadie', '10/6/2020', 'scottie cross', 1, 'N/A', 3);


