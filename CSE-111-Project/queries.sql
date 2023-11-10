/*1)List first and last names of all doctors*/
SELECT FirstName, LastName 
FROM doctor;

/*2)List all the patients first and last names with their blood types.*/
SELECT FirstName, LastName, BloodType 
FROM patient;

/*3)List of Patients with Their Appointments and Assigned Doctors

This query retrieves patient details along with their appointment times and the corresponding doctors.*/
SELECT
    p.FirstName AS PatientFirstName,
    p.LastName AS PatientLastName,
    a.AppointmentTime,
    d.FirstName AS DoctorFirstName,
    d.LastName AS DoctorLastName
FROM
    patient p
JOIN
    appointment a ON p.PatientID = a.PatientID
JOIN
    doctor d ON a.DoctorID = d.DoctorID;

/* Patients, Their Room Assignments, and Check-in Dates

This query shows which patients are assigned to which rooms, along with their check-in dates. */

SELECT
    p.FirstName AS PatientFirstName,
    p.LastName AS PatientLastName,
    pr.RoomNumber,
    pr.CheckInDate
FROM
    patient p
JOIN
    patient_room pr ON p.PatientID = pr.PatientID
JOIN
    room r ON pr.RoomNumber = r.RoomNumber;

/* Patients with Their Prescribed Medications and Prescribing Details

This query lists patients, the medications prescribed to them, and details about the prescriptions. */

SELECT
    p.FirstName AS PatientFirstName,
    p.LastName AS PatientLastName,
    m.Name AS MedicationName,
    pm.Dosage,
    pm.Frequency,
    pm.PrescribedDate
FROM
    patient p
JOIN
    patient_medication pm ON p.PatientID = pm.PatientID
JOIN
    medication m ON pm.MedicationID = m.MedicationID;


/*4)Count the number of appointments for each doctor*/
SELECT DoctorID, COUNT(*) AS AppointmentCount 
FROM appointment 
GROUP BY DoctorID;

/*5)List the medications prescribed, along with the patient's first name
fix this query*/
SELECT p.FirstName, m.Name
FROM patient p
JOIN patient_medication pm ON p.PatientID = pm.PatientID
JOIN medication m ON pm.MedicationID = m.MedicationID;


/*6)list the doctors whos specialty is Cardiology*/
SELECT FirstName, LastName 
FROM doctor
WHERE Specialization = 'Cardiology';

/*7)Find the patients who were born in 1990 or earlier*/
SELECT FirstName, LastName
FROM patient
WHERE DateOfBirth <= '1990-01-01';

/*8)List the rooms where patients are currently checked in
fixed this one as well*/
SELECT RoomNumber, PatientID, CheckInDate
FROM patient_room 
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

/*11)Count the number of patients in each room
updated*/
SELECT RoomNumber, COUNT(*) AS PatientCount
FROM patient_room
GROUP BY RoomNumber;


/*12)List the nurses working the night shift*/
SELECT FirstName, LastName
FROM nurse 
WHERE Shift = 'night';

/*13)Count the number of patients*/
SELECT COUNT(*) AS PatientCount 
FROM patient;

/*14)Count the number of nurses*/
SELECT COUNT(*) AS NurseCount
FROM nurse;

/*15)List the patients who have a room assigned*/
SELECT FirstName, LastName
FROM patient
LEFT JOIN room ON patient.PatientID = room.PatientID
WHERE room.PatientID IS NOT NULL;

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

/*20)Count the total number of patients seeing a Pediatric Doctor
cahgned alias since it was the wrong type of doctor*/
SELECT COUNT(*) AS PediatricPatientCount
FROM appointment a
JOIN doctor d ON a.DoctorID = d.DoctorID
WHERE d.Specialization = 'Pediatric';


/*Modification Statements*/

INSERT INTO patient (PatientID, FirstName, LastName, DateOfBirth, Address, MedicationID, Allergies, BloodType)
VALUES ('12346', 'Alice', 'Johnson', '1985-03-15', '123 Elm St', '25469', 'Peanuts', 'AB+');

INSERT INTO doctor (DoctorID, FirstName, LastName, Specialization)
VALUES ('1006', 'Emily', 'Brown', 'Gynecology');

INSERT INTO medication (MedicationID, Name, Pharma_Company, Purpose, SideEffects, DosageForm)
VALUES ('95217', 'Aspirin', 'Bayer', 'Pain relief', 'Stomach upset', 'Tablet');


UPDATE patient
SET Address = '456 Oak St'
WHERE PatientID = 12341;

UPDATE doctor
SET Specialization = 'Neurology'
WHERE DoctorID = 1002;

UPDATE medication
SET DosageForm = 'Capsule'
WHERE MedicationID = 45621;


DELETE FROM patient
WHERE PatientID = 12346;

DELETE FROM doctor
WHERE DoctorID = 1006;

DELETE FROM medication
WHERE MedicationID = 95217;
