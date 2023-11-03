-- SQLite
DROP TABLE Doctor;
DROP TABLE Patient;
DROP TABLE Nurse;
DROP TABLE Medication;
DROP TABLE PatientRoom;
DROP TABLE Appointment;

CREATE TABLE Doctor (
    DoctorID INTEGER PRIMARY KEY,
    FirstName CHAR(32) NOT NULL,
    LastName CHAR(32) NOT NULL,
    Specialization CHAR(50) NOT NULL
);

CREATE TABLE Patient (
    PatientID INTEGER PRIMARY KEY,
    FirstName CHAR(32) NOT NULL,
    LastName CHAR(32) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address CHAR(100) NOT NULL,
    MedicationID INTEGER NOT NULL,
    Allergies VARCHAR(255),
    BloodType CHAR(3),
    FOREIGN KEY (MedicationID) REFERENCES Medication(MedicationID)
);

CREATE TABLE Medication (
    MedicationID INTEGER PRIMARY KEY,
    Name CHAR(50) NOT NULL,
    Pharma_Company CHAR(50),
    Purpose VARCHAR(255),
    SideEffects VARCHAR(255),
    DosageForm CHAR(20) NOT NULL
);

CREATE TABLE Appointment (
    AppointmentID INTEGER PRIMARY KEY,
    PatientID INTEGER NOT NULL,
    DoctorID INTEGER NOT NULL,
    AppointmentTime TIMESTAMP NOT NULL,
    Purpose VARCHAR(255),
    Notes VARCHAR(255),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
);

CREATE TABLE PatientRoom (
    PatientID INTEGER NOT NULL,
    RoomNumber CHAR(10) NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE,
    PRIMARY KEY (PatientID, RoomNumber, CheckInDate),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

CREATE TABLE Nurse (
    NurseID INTEGER PRIMARY KEY,
    FirstName CHAR(32) NOT NULL,
    LastName CHAR(32) NOT NULL,
    Shift CHAR(20) NOT NULL
);