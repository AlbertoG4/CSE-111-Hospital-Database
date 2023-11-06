/*1)List first and last names of all doctors*/
SELECT FirstName, LastName 
FROM doctor;

/*2)List all the patients first and last names with their blood types.*/
SELECT FirstName, LastName, BloodType 
FROM patient;

/*3)Find the names of all patients who have allergies*/
SELECT FirstName, LastName 
FROM patient 
WHERE Allergies IS NOT NULL;

/*4)Count the number of appointments for each doctor*/
SELECT DoctorID, COUNT(*) AS AppointmentCount 
FROM appointment 
GROUP BY DoctorID;

/*5)List the medications prescribed by doctors, along with the patient's first name*/
SELECT p.FirstName, m.Name
FROM patient p
JOIN medication m ON p.MedicationID = m.MedicationID;

/*6)list the doctors whos specialty is Cardiology*/
SELECT * 
FROM doctor
WHERE Specialization = 'Cardiology';

/*7)Find the patients who were born in 2000 or later*/
SELECT FirstName, LastName 
FROM patient 
WHERE DateOfBirth >= '2000/01/01';

/*8)List the rooms where patients are currently checked in*/
SELECT RoomNumber, PatientID, CheckInDate
FROM room 
WHERE CheckOutDate IS NULL;

/*9)List the medications with side effects*/
SELECT Name, SideEffects 
FROM medication
WHERE SideEffects IS NOT NULL;

/*10)Find the doctors who have not appointments*/
SELECT d.FirstName, d.LastName
FROM doctor d
LEFT JOIN appointment a ON d.DoctorID = a.DoctorID
WHERE a.DoctorID IS NULL;

/*11)Count the number of patients in each room*/
SELECT RoomNumber, COUNT(*) AS PatientCount
FROM room
GROUP BY RoomNumber;

/*12)List the nurses working the night shift*/
SELECT FirstName, LastName
FROM nurse 
WHERE Shift = 'Night';

/*13)Count the number of patients*/
SELECT COUNT(*) AS PatientCount 
FROM patient;

/*14)Count the number of nurses*/
SELECT COUNT(*) AS NurseCount
FROM nurse;

/*15)List the patients who have no assigned room*/
SELECT FirstName, LastName
FROM patient
LEFT JOIN room ON patient.PatientID = room.PatientID
WHERE room.PatientID IS NULL;

/*16)Find the patients who have been checked out from their room*/
SELECT FirstName, LastName
FROM patient
JOIN room ON patient.PatientID = room.PatientID
WHERE room.CheckOutDate IS NOT NULL;

/*17)Count the doctors*/
SELECT COUNT(*) AS DoctorCount
FROM doctor;

/*18)List the medications and their purposes.*/
SELECT Name, Purpose 
FROM medication;

/*19)List patients older than 60*/
SELECT FirstName, LastName, DateOfBirth
FROM patient
WHERE DateOfBirth < DATE('now', '-60 years');

/*20)Count the total number of patients in the database*/
SELECT COUNT(*) AS TotalPatients 
FROM patient;


