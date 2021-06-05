DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    breed VARCHAR(255),
    owner_contact_number VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id)
);

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    qualifications VARCHAR(255),
    contact_number VARCHAR(255)
);

INSERT INTO vets (first_name, last_name, qualifications, contact_number)
VALUES ('Aileen', 'Matthews', 'MRCVS', '07865 123456');

INSERT INTO vets (first_name, last_name, qualifications, contact_number)
VALUES ('Roland', 'Walters', 'FRCVS', '01234 987654');

INSERT INTO vets (first_name, last_name, qualifications, contact_number)
VALUES ('Rachel', 'Mcfarlane', 'MRCVS', '07531 246810');