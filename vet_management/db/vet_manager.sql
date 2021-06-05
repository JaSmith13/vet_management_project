DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    qualifications VARCHAR(255),
    contact_number VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    breed VARCHAR(255),
    owner_contact_number VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id)
);

INSERT INTO vets (first_name, last_name, qualifications, contact_number)
VALUES ('Aileen', 'Matthews', 'MRCVS', '07865 123456');

INSERT INTO vets (first_name, last_name, qualifications, contact_number)
VALUES ('Roland', 'Walters', 'FRCVS', '01234 987654');

INSERT INTO vets (first_name, last_name, qualifications, contact_number)
VALUES ('Rachel', 'Mcfarlane', 'MRCVS', '07531 246810');

INSERT INTO pets (name, date_of_birth, breed, owner_contact_number, treatment_notes, vet_id)
VALUES ('Stanley', '01/07/2018', 'cocker spaniel', '07891 654321', 'allergic to meat', 1);

