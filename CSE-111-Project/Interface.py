import customtkinter as ctk
import os
import sqlite3
from PIL import Image
from datetime import datetime


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hospital Database")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.blue_cross = ctk.CTkImage(Image.open(os.path.join(image_path, "Blue_cross.svg.png")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
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

        self.doc_nurse_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Doctor/Nurse Managment",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.doc_nurse_button_event)
        self.doc_nurse_button.grid(row=6, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")
        
        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

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

        # create add patient frame
        self.add_patient_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.add_patient_frame.grid_columnconfigure(0, weight=1)

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


        # Display rooms frame
        self.room_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.room_frame.grid_columnconfigure(0, weight=1)

            #Display all rooms button
        self.submit_button_all = ctk.CTkButton(self.room_frame, text="Display all Rooms", command=self.display_rooms_all)
        self.submit_button_all.grid(row=0, column=0, padx=20, pady=10)

            #Display available rooms
        self.submit_button_empty = ctk.CTkButton(self.room_frame, text="Display available rooms", command=self.display_rooms_empty)
        self.submit_button_empty.grid(row=1, column=0, padx=20, pady=10)

            #Display Non-available rooms
        self.submit_button_non_empty = ctk.CTkButton(self.room_frame, text="Display Non-available rooms", command=self.display_rooms_occupied)
        self.submit_button_non_empty.grid(row=2, column=0, padx=20, pady=10)

        #search appointment frame
        self.search_appointment_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.search_appointment_frame.grid(row=1, column=0, padx=20, pady=10)

        self.entry_patient_name = ctk.CTkEntry(self.search_appointment_frame, placeholder_text="Patient Name")
        self.entry_patient_name.grid(row=1, column=0, padx=20, pady=10)

        self.entry_patient_dob = ctk.CTkEntry(self.search_appointment_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        self.entry_patient_dob.grid(row=2, column=0, padx=20, pady=10)

        self.submit_button = ctk.CTkButton(self.search_appointment_frame, text="Submit", command=self.search_appointment)
        self.submit_button.grid(row=3, column=0, padx=20, pady=10)       
        #create/add appointment frame
        self.add_appointment_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.entry_patient_name = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Patient Name")
        self.entry_patient_name.grid(row=1, column=0, padx=20, pady=10)

        self.entry_patient_dob = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        self.entry_patient_dob.grid(row=2, column=0, padx=20, pady=10)

        self.entry_appointment_date = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Appointment Date (YYYY-MM-DD)")
        self.entry_appointment_date.grid(row=3, column=0, padx=20, pady=10)

        self.entry_appointment_time = ctk.CTkEntry(self.add_appointment_frame, placeholder_text="Appointment Time (HH:MM AM/PM)")
        self.entry_appointment_time.grid(row=4, column=0, padx=20, pady=10)

        self.submit_button = ctk.CTkButton(self.add_appointment_frame, text="Submit", command=self.add_appointment)
        self.submit_button.grid(row=5, column=0, padx=20, pady=10)
        
        #create doc and nurse frame
        self.doc_nurse_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        

        # select default frame
        self.select_frame_by_name("Patient_Home")
        

    def search_patient_data(self):
        # Fetch data from entry fields
        first_name = self.search_first_name.get()
        last_name = self.search_last_name.get()
        dob = self.search_dob.get()

        # Database operation
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('data.sqlite')  # Replace 'data.sqlite' with your actual database file
            cursor = conn.cursor()

            # SQL query to search for a patient
            # This query will search for records that match all provided fields
            query = ''' SELECT * FROM patient 
                        WHERE FirstName LIKE ? AND LastName LIKE ? AND DateOfBirth = ? '''
            cursor.execute(query, (first_name + '%', last_name + '%', dob))

            # Fetching the results
            search_results = cursor.fetchall()
            for row in search_results:
                print(row)  # Print the result or handle it as needed

        except sqlite3.Error as error:
            print("Failed to search data in sqlite table", error)
        
        finally:
            # Close the database connection
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

    def search_appointment(self):
        # Fetch data from entry fields
        patient_name = self.entry_patient_name.get()
        patient_dob = self.entry_patient_dob.get()

        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # Assuming you have a 'patient' and an 'appointment' table and they are related by 'PatientID'.
            # This query joins the 'patient' and 'appointment' tables to find appointments
            # for a patient with a matching name and date of birth.
            query = ''' SELECT a.AppointmentID, a.AppointmentTime, a.Notes
                        FROM appointment a
                        JOIN patient p ON a.PatientID = p.PatientID
                        WHERE p.FirstName || ' ' || p.LastName LIKE ? AND p.DateOfBirth = ? '''

            # Format patient name for partial matching and execute query
            cursor.execute(query, ('%' + patient_name + '%', patient_dob))
            appointments = cursor.fetchall()

            for appointment in appointments:
                print(appointment)  # Replace with your method of displaying the data

        except sqlite3.Error as error:
            print("Failed to search appointments", error)
        finally:
            if conn:
                conn.close()

    def add_appointment(self):
        # Fetch data from entry fields
        patient_name = self.entry_patient_name.get()
        patient_dob = self.entry_patient_dob.get()
        appointment_date = self.entry_appointment_date.get()
        appointment_time = self.entry_appointment_time.get()

        # Combine date and time into a single datetime object (if necessary)
        appointment_datetime = datetime.strptime(appointment_date + ' ' + appointment_time, '%Y-%m-%d %I:%M %p')

        try:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()

            # Assuming you have a 'patient' table and you need to find the PatientID based on name and DOB
            cursor.execute("SELECT PatientID FROM patient WHERE FirstName || ' ' || LastName = ? AND DateOfBirth = ?", (patient_name, patient_dob))
            patient_id_result = cursor.fetchone()

            if patient_id_result:
                patient_id = patient_id_result[0]
                
                # SQL query to insert a new appointment
                query = ''' INSERT INTO appointment (PatientID, AppointmentTime)
                            VALUES (?, ?) '''
                cursor.execute(query, (patient_id, appointment_datetime))
                conn.commit()
                print("Appointment added successfully")
            else:
                print("Patient not found")

        except sqlite3.Error as error:
            print("Failed to add appointment", error)
        finally:
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
        self.select_frame_by_name("Doctor and Nurse")


    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()

