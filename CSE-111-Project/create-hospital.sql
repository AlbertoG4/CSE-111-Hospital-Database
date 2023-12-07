-- SQLite

DROP TABLE IF EXISTS DOCTOR;
DROP TABLE IF EXISTS PATIENT;
DROP TABLE IF EXISTS MEDICATION;
DROP TABLE IF EXISTS APPOINTMENT;
DROP TABLE IF EXISTS PATIENT_ROOM;
DROP TABLE IF EXISTS ROOM;
DROP TABLE IF EXISTS NURSE;
DROP TABLE IF EXISTS PATIENT_MEDICATION;

CREATE TABLE doctor (
    DoctorID INTEGER PRIMARY KEY,
    FirstName CHAR(32) NOT NULL,
    LastName CHAR(32) NOT NULL,
    Specialization CHAR(50) NOT NULL
);

CREATE TABLE patient (
    PatientID INTEGER PRIMARY KEY,
    FirstName CHAR(32) NOT NULL,
    LastName CHAR(32) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address CHAR(100) NOT NULL,
    Allergies VARCHAR(255),
    BloodType CHAR(3)

);

CREATE TABLE medication (
    MedicationID INTEGER PRIMARY KEY,
    Name CHAR(50) NOT NULL,
    Pharma_Company CHAR(50),
    Purpose VARCHAR(255),
    SideEffects VARCHAR(255),
    DosageForm CHAR(20) NOT NULL
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

-- had to create room because the PatientRoom junction table can 
-- record each instance of a patient being assigned to a room, while the Room table maintains the static details about each room.
CREATE TABLE room (
    RoomNumber CHAR(10) PRIMARY KEY,
    RoomType CHAR(20),
    Capacity INTEGER
);

CREATE TABLE patient_room (
    PatientID INTEGER NOT NULL,
    RoomNumber CHAR(10) NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE,
    PRIMARY KEY (PatientID, RoomNumber, CheckInDate),
    FOREIGN KEY (PatientID) REFERENCES patient(PatientID),
    FOREIGN KEY (RoomNumber) REFERENCES room(RoomNumber)
);


CREATE TABLE nurse (
    NurseID INTEGER PRIMARY KEY,
    FirstName CHAR(32) NOT NULL,
    LastName CHAR(32) NOT NULL,
    Shift CHAR(20) NOT NULL
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
