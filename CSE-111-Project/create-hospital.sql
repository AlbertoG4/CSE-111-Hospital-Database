-- SQLite

DROP TABLE DOCTOR;
DROP TABLE PATIENT;
DROP TABLE MEDICATION;
DROP TABLE APPOINTMENT;
DROP TABLE PATIENT_ROOM;
DROP TABLE ROOM;
DROP TABLE NURSE;
DROP TABLE PATIENT_MEDICATION;

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
    AppointmentTime TIMESTAMP NOT NULL,
    Purpose VARCHAR(255),
    Notes VARCHAR(255),
    FOREIGN KEY (PatientID) REFERENCES patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES doctor(DoctorID)
);

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
