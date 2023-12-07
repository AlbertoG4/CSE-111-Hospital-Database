-- SQLite

DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS nurse;
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS patient_room;
DROP TABLE IF EXISTS appointment;
DROP TABLE IF EXISTS medication;
DROP TABLE IF EXISTS patient_medication;


CREATE TABLE doctor (
    DoctorID INTEGER PRIMARY KEY,
    FirstName VARCHAR(32) NOT NULL,
    LastName VARCHAR(32) NOT NULL,
    Specialization CHAR(50) NOT NULL
);

CREATE TABLE nurse (
    NurseID INTEGER PRIMARY KEY,
    FirstName VARCHAR(32) NOT NULL,
    LastName VARCHAR(32) NOT NULL,
    Shift CHAR(20) NOT NULL
);

CREATE TABLE patient (
    PatientID INTEGER PRIMARY KEY,
    FirstName VARCHAR(32) NOT NULL,
    LastName VARCHAR(32) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address CHAR(100) NOT NULL,
    Allergies VARCHAR(255),
    BloodType CHAR(3)
);

-- had to create room because the PatientRoom junction table can 
-- record each instance of a patient being assigned to a room, while the Room table maintains the static details about each room.
CREATE TABLE room (
    RoomNumber CHAR(10) PRIMARY KEY,
    RoomType CHAR(20),
    Capacity INTEGER
);

CREATE TABLE patient_room (
    PatientID INTEGER NOT NULL,
    NurseID INTEGER,
    RoomNumber CHAR(10) NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE,
    PRIMARY KEY (PatientID, RoomNumber, CheckInDate),
    FOREIGN KEY (PatientID) REFERENCES patient(PatientID),
    FOREIGN KEY (NurseID) REFERENCES nurse(NurseID),
    FOREIGN KEY (RoomNumber) REFERENCES room(RoomNumber)
);

CREATE TABLE appointment (
    AppointmentID INTEGER PRIMARY KEY,
    PatientID INTEGER NOT NULL,
    DoctorID INTEGER NOT NULL,
    AppointmentDate DATE NOT NULL, 
    AppointmentTime TIMESTAMP NOT NULL,
    Purpose VARCHAR(255),
    Notes VARCHAR(255),
    FOREIGN KEY (PatientID) REFERENCES patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES doctor(DoctorID)
);

CREATE TABLE medication (
    MedicationID INTEGER PRIMARY KEY,
    Name CHAR(50) NOT NULL,
    Pharma_Company CHAR(50),
    Purpose VARCHAR(255),
    SideEffects VARCHAR(255),
    DosageForm CHAR(20) NOT NULL
);

CREATE TABLE patient_medication (
    PatientID INTEGER NOT NULL,
    MedicationID INTEGER NOT NULL,
    PrescribedDate DATE NOT NULL,
    Dosage CHAR(50),
    Frequency CHAR(50),
    PRIMARY KEY (PatientID, MedicationID, PrescribedDate),
    FOREIGN KEY (PatientID) REFERENCES patient(PatientID),
    FOREIGN KEY (MedicationID) REFERENCES medication(MedicationID)
);

INSERT INTO doctor (FirstName, LastName, Specialization) VALUES 
('Emily', 'Johnson', 'Cardiology'),
('Michael', 'Smith', 'Neurology'),
('Rachel', 'Lee', 'Pediatrics'),
('James', 'Brown', 'Oncology'),
('Laura', 'Garcia', 'Dermatology');

INSERT INTO nurse (FirstName, LastName, Shift) VALUES 
('Sarah', 'Miller', 'Day'),
('Carlos', 'Rodriguez', 'Night'),
('Anna', 'Martinez', 'Evening'),
('David', 'Hernandez', 'Day'),
('Jessica', 'Wilson', 'Night');


INSERT INTO medication (Name, Pharma_Company, Purpose, SideEffects, DosageForm) VALUES 
('Lisinopril', 'Merck', 'Lower blood pressure', 'Dizziness, headaches', 'Tablet'),
('Ciprofloxacin', 'Bayer', 'Antibiotic', 'Nausea, diarrhea', 'Tablet'),
('Metformin', 'GlaxoSmithKline', 'Diabetes treatment', 'Nausea, vomiting', 'Extended-release tablet'),
('Simvastatin', 'Pfizer', 'Lower cholesterol', 'Muscle pain, headaches', 'Tablet'),
('Omeprazole', 'AstraZeneca', 'Reduce stomach acid', 'Headache, stomach pain', 'Capsule');

INSERT INTO patient (FirstName, LastName, DateOfBirth, Address, Allergies, BloodType) VALUES 
('Mia', 'Williams', '1991-05-21', '234 Elm St, Springfield', 'None', 'A+'),
('Ethan', 'Brown', '1988-12-10', '567 Oak Ave, Greenville', 'Penicillin', 'B-'),
('Abigail', 'Davis', '1976-03-15', '890 Maple Rd, Oldtown', 'Latex', 'O+'),
('Alexander', 'Wilson', '1982-07-22', '123 Pine St, Newtown', 'None', 'AB-'),
('Sophia', 'Martinez', '1990-09-30', '456 Birch Ln, Hillville', 'Nuts', 'A-');

INSERT INTO room (RoomNumber, RoomType, Capacity) VALUES 
('101A', 'ICU', 1),
('101B', 'ICU', 1),
('102', 'General', 2),
('103', 'General', 2),
('201', 'Maternity', 3);

INSERT INTO patient_room (PatientID, NurseID, RoomNumber, CheckInDate, CheckOutDate) VALUES
(1, 1, '101A', '2023-04-01', NULL),
(2, 2, '102', '2023-04-02', NULL),
(3, 3, '103', '2023-04-03', '2023-04-10'),
(4, 4, '101B', '2023-04-04', NULL),
(5, 5, '201', '2023-04-05', NULL);

INSERT INTO appointment (PatientID, DoctorID, AppointmentDate, AppointmentTime, Purpose, Notes) VALUES
(1, 1, '2023-04-15', '2023-04-15 09:00:00', 'Routine Checkup', 'Annual physical'),
(2, 2, '2023-04-16', '2023-04-16 10:00:00', 'Follow-up', 'Review test results'),
(3, 3, '2023-04-17', '2023-04-17 11:00:00', 'Consultation', 'Discuss treatment options'),
(4, 4, '2023-04-18', '2023-04-18 14:00:00', 'Emergency', 'Urgent consultation'),
(5, 5, '2023-04-19', '2023-04-19 15:00:00', 'Routine Checkup', 'Pregnancy follow-up');

INSERT INTO patient_medication (PatientID, MedicationID, PrescribedDate, Dosage, Frequency) VALUES
(1, 1, '2023-04-01', '10mg', 'Once a day'),
(2, 2, '2023-04-02', '250mg', 'Twice a day'),
(3, 3, '2023-04-03', '500mg', 'Once a day'),
(4, 4, '2023-04-04', '20mg', 'Once a day'),
(5, 5, '2023-04-05', '40mg', 'Once a day');

