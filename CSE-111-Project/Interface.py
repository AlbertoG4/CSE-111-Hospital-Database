import customtkinter as ctk
import os
import sqlite3
from PIL import Image
from datetime import datetime


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hospital Database")
        self.geometry("1050x650")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.blue_cross = ctk.CTkImage(Image.open(os.path.join(image_path, "Blue_cross.svg.png")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "background.jpg")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text=" UCM HOSPITAL", image=self.blue_cross,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.patient_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Patient Search",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.patient_button_event)
        self.patient_button.grid(row=1, column=0, sticky="ew")

        self.add_patient_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add New Patient",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.add_patient_button_event)
        self.add_patient_button.grid(row=2, column=0, sticky="ew")

        self.appointment_search_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Appointment Search",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.appointment_search_button_event)
        self.appointment_search_button.grid(row=3, column=0, sticky="ew")

        self.add_appointment_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add Appointment",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.add_appointments_button_event)
        self.add_appointment_button.grid(row=4, column=0, sticky="ew")

        self.rooms_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Rooms",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.rooms_button_event)
        self.rooms_button.grid(row=5, column=0, sticky="ew")

        self.doc_nurse_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Doctor/Nurse Information",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.doc_nurse_button_event)
        self.doc_nurse_button.grid(row=6, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")
        
        # create home_patient_search frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure((1, 2) , weight=0)

        self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.search_first_name = ctk.CTkEntry(self.home_frame, placeholder_text="First Name")
        self.search_first_name.grid(row=1, column=0, padx=20, pady=10)

        self.search_last_name = ctk.CTkEntry(self.home_frame, placeholder_text="Last Name")
        self.search_last_name.grid(row=2, column=0, padx=20, pady=10)

        self.search_dob = ctk.CTkEntry(self.home_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        self.search_dob.grid(row=3, column=0, padx=20, pady=10)

        self.submit_search_button = ctk.CTkButton(self.home_frame, text="Search", command=self.search_patient_data)
        self.submit_search_button.grid(row=4, column=0, padx=20, pady=10)

        self.display_button = ctk.CTkButton(self.home_frame, text="Display all patients", command=self.display_patients)
        self.display_button.grid(row=5, column=0, padx=20, pady=10)
        
        #    # Assuming add_patient_frame is already defined in your class
        # self.tabview = ctk.CTkTabview(self.home_frame, width=250)
        # self.tabview.add("Results")
        # self.tabview.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

        # create add patient frame
        self.add_patient_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.add_patient_frame.grid_columnconfigure(0, weight=1)
        self.add_patient_frame.grid_columnconfigure((1, 2) , weight=0)

        self.add_patient__image_label = ctk.CTkLabel(self.add_patient_frame, text="", image=self.large_test_image)
        self.add_patient__image_label.grid(row=0, column=0, padx=20, pady=10)

        self.entry_first = ctk.CTkEntry(self.add_patient_frame, placeholder_text="First Name")
        self.entry_first.grid(row=1, column=0, padx=20, pady=10)

        self.entry_last = ctk.CTkEntry(self.add_patient_frame, placeholder_text="Last Name")
        self.entry_last.grid(row=2, column=0, padx=20, pady=10)

        self.entry_bday = ctk.CTkEntry(self.add_patient_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        self.entry_bday.grid(row=3, column=0, padx=20, pady=10)

        self.entry_address = ctk.CTkEntry(self.add_patient_frame, placeholder_text="Address")
        self.entry_address.grid(row=4, column=0, padx=20, pady=10)

        self.entry_allergies = ctk.CTkEntry(self.add_patient_frame, placeholder_text="Allergies")
        self.entry_allergies.grid(row=5, column=0, padx=20, pady=10)

        self.entry_blood_type = ctk.CTkEntry(self.add_patient_frame, placeholder_text="Blood Type")
        self.entry_blood_type.grid(row=6, column=0, padx=20, pady=10)

        self.submit_button = ctk.CTkButton(self.add_patient_frame, text="Submit", command=self.save_patient_data)
        self.submit_button.grid(row=7, column=0, padx=20, pady=10)

        #     # create tabview
        # self.tabview = ctk.CTkTabview(self.add_patient_frame, width=250)
        # self.tabview.add("Results")
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")


        # Display rooms frame
        self.room_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.room_frame.grid_columnconfigure(0, weight=1)
        self.room_frame.grid_columnconfigure((1, 2) , weight=0)

        self.room_frame__image_label = ctk.CTkLabel(self.room_frame, text="", image=self.large_test_image)
        self.room_frame__image_label.grid(row=0, column=0, padx=20, pady=10)

            #Display all rooms button
        self.submit_button_all = ctk.CTkButton(self.room_frame, text="Display all Rooms", command=self.display_rooms_all)
        self.submit_button_all.grid(row=1, column=0, padx=20, pady=10)

            #Display available rooms
        self.submit_button_empty = ctk.CTkButton(self.room_frame, text="Display available rooms", command=self.display_rooms_empty)
        self.submit_button_empty.grid(row=2, column=0, padx=20, pady=10)

            #Display Non-available rooms
        self.submit_button_non_empty = ctk.CTkButton(self.room_frame, text="Display Non-available rooms", command=self.display_rooms_occupied)
        self.submit_button_non_empty.grid(row=3, column=0, padx=20, pady=10)

            #Display patient rooms
        self.display_patient_rooms = ctk.CTkButton(self.room_frame, text="Display Patient rooms", command=self.patient_rooms)
        self.display_patient_rooms.grid(row=4, column=0, padx=20, pady=10)

        #     # create tabview
        # self.tabview = ctk.CTkTabview(self.room_frame, width=250)
        # self.tabview.add("Results")
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #search appointment frame
        self.search_appointment_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.search_appointment_frame.grid(row=1, column=0, padx=20, pady=10)
        self.search_appointment_frame.grid_columnconfigure(0, weight=1)
        self.search_appointment_frame.grid_columnconfigure((1, 2) , weight=0)

        self.search_appointment_frame_label = ctk.CTkLabel(self.search_appointment_frame, text="", image=self.large_test_image)
        self.search_appointment_frame_label.grid(row=0, column=0, padx=20, pady=10)

        self.a_first = ctk.CTkEntry(self.search_appointment_frame, placeholder_text="First_Name")
        self.a_first.grid(row=1, column=0, padx=20, pady=10)

        self.a_last = ctk.CTkEntry(self.search_appointment_frame, placeholder_text="Last_Name")
        self.a_last.grid(row=2, column=0, padx=20, pady=10)

        self.entry_patient_dob = ctk.CTkEntry(self.search_appointment_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        self.entry_patient_dob.grid(row=3, column=0, padx=20, pady=10)

        self.submit_button = ctk.CTkButton(self.search_appointment_frame, text="Submit", command=self.search_appointment)
        self.submit_button.grid(row=4, column=0, padx=20, pady=10)

        self.submit_button = ctk.CTkButton(self.search_appointment_frame, text="Display all apointments", command=self.display_appointments)
        self.submit_button.grid(row=5, column=0, padx=20, pady=10)           

        #     # create tabview
        # self.tabview = ctk.CTkTabview(self.search_appointment_frame, width=250)
        # self.tabview.add("Results")
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #create/add/delete/update appointment frame
        self.add_appointment_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.add_appointment_frame.grid_columnconfigure(0, weight=1)
        self.add_appointment_frame.grid_columnconfigure(1 , weight=0)

        self.add_appointment_frame_label = ctk.CTkLabel(self.add_appointment_frame, text="", image=self.large_test_image)
        self.add_appointment_frame_label.grid(row=0, column=0, padx=20, pady=10)

        self.entry_patient_first_name = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="First_Name")
        self.entry_patient_first_name.grid(row=1, column=0, padx=20, pady=10)

        self.entry_patient_last_name = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Last_Name")
        self.entry_patient_last_name.grid(row=2, column=0, padx=20, pady=10)

        self.entry_patient_dob = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        self.entry_patient_dob.grid(row=3, column=0, padx=20, pady=10)

        self.doctor_first_last = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Attending Doctor")
        self.doctor_first_last.grid(row=4, column=0, padx=20, pady=10)

        self.entry_appointment_date = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Appointment Date (YYYY-MM-DD)")
        self.entry_appointment_date.grid(row=5, column=0, padx=20, pady=10)

        self.entry_appointment_time = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Appointment Time (HH:MM AM/PM)")
        self.entry_appointment_time.grid(row=6, column=0, padx=20, pady=10)

        self.notes = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Appointment notes")
        self.notes.grid(row=7, column=0, padx=20, pady=10)

        self.submit_button = ctk.CTkButton(self.add_appointment_frame, text="Submit", command=self.add_appointment)
        self.submit_button.grid(row=8, column=0, padx=20, pady=10)

        self.delete_patient_first_name = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="First_Name")
        self.delete_patient_first_name.grid(row=1, column=1, padx=20, pady=10)

        self.delete_patient_last_name = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Last_Name")
        self.delete_patient_last_name.grid(row=2, column=1, padx=20, pady=10)

        self.entry_appointment_date = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Appointment Date (YYYY-MM-DD)")
        self.entry_appointment_date.grid(row=3, column=1, padx=20, pady=10)

        self.delete_button = ctk.CTkButton(self.add_appointment_frame, text="Delete appointment", command=self.delete_appointment)
        self.delete_button.grid(row=4, column=1, padx=20, pady=10)
        
        #create doc and nurse frame
        self.doc_nurse_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.doc_nurse_frame.grid_columnconfigure(0, weight=1)
        self.doc_nurse_frame.grid_columnconfigure(1 , weight=0)

        self.doc_nurse_frame_label = ctk.CTkLabel(self.doc_nurse_frame, text="", image=self.large_test_image)
        self.doc_nurse_frame_label.grid(row=0, column=0, padx=20, pady=10)

        self.add_doc_first_name = ctk.CTkEntry(self.doc_nurse_frame, placeholder_text="First_Name")
        self.add_doc_first_name.grid(row=1, column=0, padx=20, pady=10)

        self.add_doc_last_name = ctk.CTkEntry(self.doc_nurse_frame, placeholder_text="Last_Name")
        self.add_doc_last_name.grid(row=2, column=0, padx=20, pady=10)

        self.add_specialty = ctk.CTkEntry(self.doc_nurse_frame, placeholder_text="Specialty")

        self.add_doc_info = ctk.CTkButton(self.doc_nurse_frame, text= "Add a Doctor", command=self.add_doctor)
        self.add_doc_info.grid(row=3, column=0, padx=20, pady=10)

        self.add_nurse_first_name = ctk.CTkEntry(self.doc_nurse_frame, placeholder_text="First_Name")
        self.add_nurse_first_name.grid(row=4, column=0, padx=20, pady=10)

        self.add_nurse_last_name = ctk.CTkEntry(self.doc_nurse_frame, placeholder_text="Last_Name")
        self.add_nurse_last_name.grid(row=5, column=0, padx=20, pady=10)

        self.add_shift = ctk.CTkEntry(self.doc_nurse_frame, placeholder_text="Shift preference")

        self.add_nurse_info = ctk.CTkButton(self.doc_nurse_frame, text= "Add a Nurse", command=self.add_nurse)
        self.add_nurse_info.grid(row=6, column=0, padx=20, pady=10)

        self.doc_info = ctk.CTkButton(self.doc_nurse_frame, text= "Display Doctors", command=self.display_doctors)
        self.doc_info.grid(row=7, column=0, padx=20, pady=10)

        self.nurse_info = ctk.CTkButton(self.doc_nurse_frame, text= "Display Nurses", command=self.display_nurses)
        self.nurse_info.grid(row=8, column=0, padx=20, pady=10)


        # select default frame
        self.select_frame_by_name("Patient_Home")

    def search_patient_data(self):
        # Fetch data from entry fields
        first_name = self.search_first_name.get().strip()
        last_name = self.search_last_name.get().strip()
        dob = self.search_dob.get().strip()

        # Building the query dynamically based on input
        query_parts = []
        params = []
        if first_name:
            query_parts.append("FirstName LIKE ?")
            params.append(first_name + '%')
        if last_name:
            query_parts.append("LastName LIKE ?")
            params.append(last_name + '%')
        if dob:
            query_parts.append("DateOfBirth = ?")
            params.append(dob)

        # If no fields are filled, return to avoid querying all records
        if not query_parts:
            print("No search criteria provided.")
            return

        query = "SELECT * FROM patient WHERE " + " OR ".join(query_parts)

        # Database operation
        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()
            cursor.execute(query, params)
            search_results = cursor.fetchall()
            for row in search_results:
                print(row)  # Print the result or handle it as needed
        except sqlite3.Error as error:
            print("Failed to search data in sqlite table", error)
        finally:
            if conn:
                conn.close()

    # display the whole patient table
    def display_patients(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to select all patients
            query = "SELECT * FROM patient"
            cursor.execute(query)

            # Fetch all patient data
            patients = cursor.fetchall()

            # Check if any patient data was found
            if patients:
                print("All Patients:")
                for patient in patients:
                    # Each patient is a tuple of data
                    print(patient)
            else:
                print("No patients found.")

        except sqlite3.Error as error:
            print("Failed to retrieve patients", error)
        finally:
            # Ensure the database connection is closed
            if conn:
                conn.close()

    # for adding patient information to sqlite, this is taking directly from add_patient frame
    def save_patient_data(self):
    # Fetch data from entry fields
        patient_data = (
            self.entry_first.get(),
            self.entry_last.get(),
            self.entry_bday.get(),
            self.entry_address.get(),
            self.entry_allergies.get(),
            self.entry_blood_type.get()
            )

        # Database operation
        try:
            # Connect to the SQLite database
            with sqlite3.connect('data.sqlite') as conn:
                cursor = conn.cursor()

            # SQL query to insert a new patient
            query = ''' INSERT INTO patient (FirstName, LastName, DateOfBirth, Address, Allergies, BloodType)
                        VALUES (?, ?, ?, ?, ?, ?) '''

            # Execute the query and commit the changes
            cursor.execute(query, patient_data)
            conn.commit()
            print("Patient added successfully")

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        
        finally:
            # Close the database connection
            if conn:
                conn.close()

    def display_rooms_all(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            query = "SELECT * FROM room"
            cursor.execute(query)
            rooms = cursor.fetchall()

            for room in rooms:
                print(room)  # Replace this with your method of displaying the data

        except sqlite3.Error as error:
            print("Failed to display all rooms", error)
        finally:
            if conn:
                conn.close()

    def display_rooms_empty(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # Assuming 'CheckOutDate IS NULL' signifies a room is currently occupied
            query = '''SELECT * FROM room 
                    WHERE RoomNumber NOT IN 
                    (SELECT RoomNumber FROM patient_room WHERE CheckOutDate IS NULL)'''
            cursor.execute(query)
            empty_rooms = cursor.fetchall()

            for room in empty_rooms:
                print(room)

        except sqlite3.Error as error:
            print("Failed to display available rooms", error)
        finally:
            if conn:
                conn.close()

    def display_rooms_occupied(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            query = '''SELECT * FROM room 
                    WHERE RoomNumber IN 
                    (SELECT RoomNumber FROM patient_room WHERE CheckOutDate IS NULL)'''
            cursor.execute(query)
            occupied_rooms = cursor.fetchall()

            for room in occupied_rooms:
                print(room)

        except sqlite3.Error as error:
            print("Failed to display non-available rooms", error)
        finally:
            if conn:
                conn.close()

    def patient_rooms(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to select patient room data and join with the patient and nurse tables
            query = '''
                SELECT pr.RoomNumber, pr.CheckInDate, pr.CheckOutDate, 
                    p.FirstName || ' ' || p.LastName AS PatientName, 
                    n.FirstName || ' ' || n.LastName AS NurseName
                FROM patient_room pr
                JOIN patient p ON pr.PatientID = p.PatientID
                LEFT JOIN nurse n ON pr.NurseID = n.NurseID
            '''
            cursor.execute(query)

            # Fetch all patient room data
            patient_rooms = cursor.fetchall()

            # Check if any patient room data was found
            if patient_rooms:
                print("All Patient Rooms:")
                for room in patient_rooms:
                    print(f"Room Number: {room[0]}, Check-In Date: {room[1]}, Check-Out Date: {room[2]}, Patient: {room[3]}, Nurse: {room[4]}")
            else:
                print("No patient rooms found.")

        except sqlite3.Error as error:
            print("Failed to retrieve patient rooms", error)
        finally:
            if conn:
                conn.close()




    def display_appointments(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to select all appointments and join with the patient and doctor tables
            query = '''
                SELECT a.AppointmentID, p.FirstName, p.LastName, d.FirstName, d.LastName, a.AppointmentDate, a.AppointmentTime, a.Purpose, a.Notes
                FROM appointment a
                JOIN patient p ON a.PatientID = p.PatientID
                JOIN doctor d ON a.DoctorID = d.DoctorID
            '''
            cursor.execute(query)

            # Fetch all appointments
            appointments = cursor.fetchall()

            # Check if any appointments were found
            if appointments:
                print("All Appointments:")
                for appointment in appointments:
                    # Each appointment is a tuple of data
                    print(f"Appointment ID: {appointment[0]} | Patient Name: {appointment[1]} {appointment[2]} | "
                        f"Doctor Name: {appointment[3]} {appointment[4]} | "
                        f"Date: {appointment[5]} | Time: {appointment[6]} | Purpose: {appointment[7]} | Notes: {appointment[8]}")
            else:
                print("No appointments found.")

        except sqlite3.Error as error:
            print("Failed to retrieve appointments", error)
        finally:
            if conn:
                conn.close()




    def search_appointment(self):
        # Fetch data from entry fields
        patient_first_name = self.a_first.get()
        patient_last_name = self.a_last.get()
        patient_dob = self.entry_patient_dob.get()

        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to find appointments for a patient with a matching name and date of birth.
            query = ''' SELECT a.AppointmentID, a.AppointmentDate, a.AppointmentTime, a.Purpose, a.Notes
                        FROM appointment a
                        JOIN patient p ON a.PatientID = p.PatientID
                        WHERE p.FirstName = ? AND p.LastName = ? OR p.DateOfBirth = ? '''

            cursor.execute(query, (patient_first_name, patient_last_name, patient_dob))
            appointments = cursor.fetchall()

            if appointments:
                print("Appointments found:")
                for appointment in appointments:
                    print(appointment)  # Displaying the data in the terminal
            else:
                print("No appointments found for the specified patient.")

        except sqlite3.Error as error:
            print("Failed to search appointments", error)
        finally:
            if conn:
                conn.close()


    def add_appointment(self):
        # Fetch data from entry fields
        patient_first_name = self.entry_patient_first_name.get()
        patient_last_name = self.entry_patient_last_name.get()
        patient_dob = self.entry_patient_dob.get()
        doctor_name = self.doctor_first_last.get()
        appointment_date = self.entry_appointment_date.get()
        appointment_time = self.entry_appointment_time.get()
        appointment_notes = self.notes.get()

        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # Find the PatientID and DoctorID based on the names
            cursor.execute("SELECT PatientID FROM patient WHERE FirstName = ? AND LastName = ? AND DateOfBirth = ?", 
                        (patient_first_name, patient_last_name, patient_dob))
            patient_id_result = cursor.fetchone()

            cursor.execute("SELECT DoctorID FROM doctor WHERE FirstName || ' ' || LastName = ?", 
                        (doctor_name,))
            doctor_id_result = cursor.fetchone()

            if patient_id_result and doctor_id_result:
                patient_id = patient_id_result[0]
                doctor_id = doctor_id_result[0]

                # SQL query to insert a new appointment
                query = ''' INSERT INTO appointment (PatientID, DoctorID, AppointmentDate, AppointmentTime, Notes)
                            VALUES (?, ?, ?, ?, ?) '''
                cursor.execute(query, (patient_id, doctor_id, appointment_date, appointment_time, appointment_notes))

                conn.commit()
                print("Appointment added successfully")

            else:
                print("Patient or Doctor not found")

        except sqlite3.Error as error:
            print("Failed to add appointment", error)
        finally:
            if conn:
                conn.close()


    def delete_appointment(self):
        # Fetch data from entry fields
        patient_first_name = self.delete_patient_first_name.get()
        patient_last_name = self.delete_patient_last_name.get()
        appointment_date = self.entry_appointment_date.get()

        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # First, find the patient ID based on the first and last name
            cursor.execute("SELECT PatientID FROM patient WHERE FirstName = ? AND LastName = ?", 
                        (patient_first_name, patient_last_name))
            patient_id_result = cursor.fetchone()

            if patient_id_result:
                patient_id = patient_id_result[0]

                # Then, delete the appointment for that patient ID and the specified date
                delete_query = ''' DELETE FROM appointment 
                                WHERE PatientID = ? AND AppointmentDate = ? '''
                cursor.execute(delete_query, (patient_id, appointment_date))
                conn.commit()

                if cursor.rowcount > 0:
                    print("Appointment deleted successfully")
                else:
                    print("No appointment found for the given details")

            else:
                print("Patient not found")

        except sqlite3.Error as error:
            print("Failed to delete appointment", error)
        finally:
            if conn:
                conn.close()

    def display_doctors(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to select all doctors
            query = "SELECT * FROM doctor"
            cursor.execute(query)

            # Fetch all doctor data
            doctors = cursor.fetchall()

            # Check if any doctor data was found
            if doctors:
                print("All Doctors:")
                for doctor in doctors:
                    # Each doctor is a tuple of data
                    print(f"Doctor ID: {doctor[0]}, Name: {doctor[1]} {doctor[2]}, Specialization: {doctor[3]}")
            else:
                print("No doctors found.")

        except sqlite3.Error as error:
            print("Failed to retrieve doctors", error)
        finally:
            # Ensure the database connection is closed
            if conn:
                conn.close()

    def display_nurses(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to select all nurses
            query = "SELECT * FROM nurse"
            cursor.execute(query)

            # Fetch all nurse data
            nurses = cursor.fetchall()

            # Check if any nurse data was found
            if nurses:
                print("All Nurses:")
                for nurse in nurses:
                    # Each nurse is a tuple of data
                    print(f"Nurse ID: {nurse[0]}, Name: {nurse[1]} {nurse[2]}, Shift: {nurse[3]}")
            else:
                print("No nurses found.")

        except sqlite3.Error as error:
            print("Failed to retrieve nurses", error)
        finally:
            # Ensure the database connection is closed
            if conn:
                conn.close()

    def add_doctor(self):
        # Fetch data from entry fields
        first_name = self.add_doc_first_name.get()
        last_name = self.add_doc_last_name.get()
        specialty = self.add_specialty.get()

        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to insert a new doctor
            query = "INSERT INTO doctor (FirstName, LastName, Specialization) VALUES (?, ?, ?)"
            cursor.execute(query, (first_name, last_name, specialty))

            # Commit the changes to the database
            conn.commit()
            print("New doctor added successfully")

        except sqlite3.Error as error:
            print("Failed to add new doctor", error)
        finally:
            # Ensure the database connection is closed
            if conn:
                conn.close()


    def add_nurse(self):
        # Fetch data from entry fields
        first_name = self.add_nurse_first_name.get()
        last_name = self.add_nurse_last_name.get()
        shift_preference = self.add_shift.get()

        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # SQL query to insert a new nurse
            query = "INSERT INTO nurse (FirstName, LastName, Shift) VALUES (?, ?, ?)"
            cursor.execute(query, (first_name, last_name, shift_preference))

            # Commit the changes to the database
            conn.commit()
            print("New nurse added successfully")

        except sqlite3.Error as error:
            print("Failed to add new nurse", error)
        finally:
            # Ensure the database connection is closed
            if conn:
                conn.close()

    
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.patient_button.configure(fg_color=("gray75", "gray25") if name == "Patient_Home" else "transparent")
        self.add_patient_button.configure(fg_color=("gray75", "gray25") if name == "Add_Patient" else "transparent")
        self.appointment_search_button.configure(fg_color=("gray75", "gray25") if name == "Appointment_Search" else "transparent")
        self.add_appointment_button.configure(fg_color=("gray75", "gray25") if name == "Add_Appointment" else "transparent")
        self.rooms_button.configure(fg_color=("gray75", "gray25") if name == "Rooms" else "transparent")
        self.doc_nurse_button.configure(fg_color=("gray75", "gray25") if name == "Doctor_Nurse" else "transparent")

        # show selected frame
        if name == "Patient_Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Add_Patient":
            self.add_patient_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.add_patient_frame.grid_forget()
        if name == "Appointment_Search":
            self.search_appointment_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.search_appointment_frame.grid_forget()
        if name == "Add_Appointment":
            self.add_appointment_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.add_appointment_frame.grid_forget()
        if name == "Rooms":
            self.room_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.room_frame.grid_forget()
        if name == "Doctor_Nurse":
            self.doc_nurse_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.doc_nurse_frame.grid_forget()

    def patient_button_event(self):
        self.select_frame_by_name("Patient_Home")

    def appointment_search_button_event(self):
        self.select_frame_by_name("Appointment_Search")

    def add_patient_button_event(self):
        self.select_frame_by_name("Add_Patient")

    def add_appointments_button_event(self):
        self.select_frame_by_name("Add_Appointment")

    def rooms_button_event(self):
        self.select_frame_by_name("Rooms")

    def doc_nurse_button_event(self):
        self.select_frame_by_name("Doctor_Nurse")


    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()

