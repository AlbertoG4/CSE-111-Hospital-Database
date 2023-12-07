-- SQLite

DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS nurse;
DROP TABLE IF EXISTS nurse_patient_assignment;
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

CREATE TABLE nurse_patient_assignment (
    NurseID INTEGER NOT NULL,
    PatientID INTEGER NOT NULL,
    AssignmentDate DATE NOT NULL,
    PRIMARY KEY (NurseID, PatientID, AssignmentDate),
    FOREIGN KEY (NurseID) REFERENCES nurse(NurseID),
    FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
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

