import customtkinter as ctk
import os
import sqlite3
from PIL import Image


class App(ctk.CTk):
    def __init__(app):
        super().__init__()

        app.title("image_example.py")
        app.geometry("700x450")

        # set grid layout 1x2
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        app.blue_cross = ctk.CTkImage(Image.open(os.path.join(image_path, "Blue_cross.svg.png")), size=(26, 26))
        app.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        app.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        app.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        app.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        app.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        app.navigation_frame = ctk.CTkFrame(app, corner_radius=0)
        app.navigation_frame.grid(row=0, column=0, sticky="nsew")
        app.navigation_frame.grid_rowconfigure(6, weight=1)

        app.navigation_frame_label = ctk.CTkLabel(app.navigation_frame, text="  Image Example", image=app.blue_cross,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        app.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        app.patient_button = ctk.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Patient Search",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=app.home_image, anchor="w", command=app.patient_button_event)
        app.patient_button.grid(row=1, column=0, sticky="ew")

        app.add_patient_button = ctk.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add New Patient",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.chat_image, anchor="w", command=app.add_patient_button_event)
        app.add_patient_button.grid(row=2, column=0, sticky="ew")

        app.appointments_button = ctk.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Appointments",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.chat_image, anchor="w", command=app.appointments_button_event)
        app.appointments_button.grid(row=3, column=0, sticky="ew")

        app.rooms_button = ctk.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Rooms",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.chat_image, anchor="w", command=app.rooms_button_event)
        app.rooms_button.grid(row=4, column=0, sticky="ew")

        app.doc_nurse_button = ctk.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Doctor/Nurse Managment",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.chat_image, anchor="w", command=app.doc_nurse_button_event)
        app.doc_nurse_button.grid(row=5, column=0, sticky="ew")

        app.appearance_mode_menu = ctk.CTkOptionMenu(app.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=app.change_appearance_mode_event)
        app.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        app.home_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")
        app.home_frame.grid_columnconfigure(0, weight=1)

        app.home_frame_large_image_label = ctk.CTkLabel(app.home_frame, text="", image=app.large_test_image)
        app.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        app.home_frame_button_1 = ctk.CTkButton(app.home_frame, text="", image=app.image_icon_image)
        app.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        app.home_frame_button_2 = ctk.CTkButton(app.home_frame, text="CTkButton", image=app.image_icon_image, compound="right")
        app.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        

        # create add patient frame
        app.add_patient_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")

        app.entry_first_name = ctk.CTkEntry(app.add_patient_frame, placeholder_text="First Name")
        app.entry_first_name.grid(row=1, column=0, padx=20, pady=10)

        app.entry_last_name = ctk.CTkEntry(app.add_patient_frame, placeholder_text="Last Name")
        app.entry_last_name.grid(row=2, column=0, padx=20, pady=10)

        app.entry_dob = ctk.CTkEntry(app.add_patient_frame, placeholder_text="Date of Birth (YYYY-MM-DD)")
        app.entry_dob.grid(row=3, column=0, padx=20, pady=10)

        app.entry_address = ctk.CTkEntry(app.add_patient_frame, placeholder_text="Address")
        app.entry_address.grid(row=4, column=0, padx=20, pady=10)

        app.entry_allergies = ctk.CTkEntry(app.add_patient_frame, placeholder_text="Allergies")
        app.entry_allergies.grid(row=5, column=0, padx=20, pady=10)

        app.entry_blood_type = ctk.CTkEntry(app.add_patient_frame, placeholder_text="Blood Type")
        app.entry_blood_type.grid(row=6, column=0, padx=20, pady=10)

        app.submit = ctk.CTkEntry(app.add_patient_frame, placeholder_text="Blood Type")
        app.entry_blood_type.grid(row=6, column=0, padx=20, pady=10)

        app.submit_button = ctk.CTkButton(app, text="Submit", command=save_patient_data)
        app.submit_button.grid(row=7, column=0, padx=20, pady=10)

        def save_patient_data():
            # Fetch data from entry fields
            patient_data = (
                app.entry_first_name.get(),
                app.entry_last_name.get(),
                app.entry_dob.get(),
                app.entry_address.get(),
                app.entry_allergies.get(),
                app.entry_blood_type.get()
            )

            # Database operation
            try:
                # Connect to the SQLite database
                conn = sqlite3.connect('data.sqlite')  # Replace 'data.sqlite' with your actual database file
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


        
        # create appointment frame
        app.appointment_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")

        # create rooms frame
        app.room_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")

        #create doc and nurse frame
        app.doc_nurse_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")
        

        # select default frame
        app.select_frame_by_name("Patient_Home")

    def select_frame_by_name(app, name):
        # set button color for selected button
        app.patient_button.configure(fg_color=("gray75", "gray25") if name == "Patient_Home" else "transparent")
        app.add_patient_button.configure(fg_color=("gray75", "gray25") if name == "Add_Patient" else "transparent")
        app.appointments_button.configure(fg_color=("gray75", "gray25") if name == "Appointments" else "transparent")
        app.rooms_button.configure(fg_color=("gray75", "gray25") if name == "Rooms" else "transparent")
        app.doc_nurse_button.configure(fg_color=("gray75", "gray25") if name == "Doctor_Nurse" else "transparent")

        # show selected frame
        if name == "Patient_Home":
            app.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.home_frame.grid_forget()
        if name == "Add_Patient":
            app.add_patient_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.add_patient_frame.grid_forget()
        if name == "Appointments":
            app.appointment_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.appointment_frame.grid_forget()
        if name == "Rooms":
            app.room_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.room_frame.grid_forget()
        if name == "Doctor_Nurse":
            app.doc_nurse_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.doc_nurse_frame.grid_forget()

    def patient_button_event(app):
        app.select_frame_by_name("Patient_Home")

    def add_patient_button_event(app):
        app.select_frame_by_name("Add_Patient")

    def appointments_button_event(app):
        app.select_frame_by_name("Appointments")

    def rooms_button_event(app):
        app.select_frame_by_name("Rooms")

    def doc_nurse_button_event(app):
        app.select_frame_by_name("Doctor and Nurse")


    def change_appearance_mode_event(app, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

