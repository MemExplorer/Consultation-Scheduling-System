import customtkinter
import models.resources as res

class teacher_app(customtkinter.CTk):
    
    def __init__(self, user_data: list):
        super().__init__()

        self.user_data = user_data

        self.title(f"Welcome, {self.user_data[3]}.")
        self.geometry(f"{res.constants.WIN_WIDTH}x{res.constants.WIN_HEIGHT}")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        """ File directory pathing for images
        Need image fixing, should use svg icons for icons due to resolution stretching when scaling. No error found.
        """

        #images are fetched from resources
        self.logo_image = customtkinter.CTkImage(res.fetch_image(res.images.customtkinter_logo_single), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(res.fetch_image(res.images.poster), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(res.fetch_image(res.images.image_icon_light), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=res.fetch_image(res.images.home_dark),
                                                 dark_image=res.fetch_image(res.images.home_light), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=res.fetch_image(res.images.chat_dark),
                                                 dark_image=res.fetch_image(res.images.chat_light), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=res.fetch_image(res.images.add_user_dark),
                                                     dark_image=res.fetch_image(res.images.add_user_light), size=(20, 20))

        """ End of resource pathing """
    
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Image Example", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # label 
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        #Create 2nd frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid(row=0, column=0, sticky="nsew")

        # add a label to the second frame
        self.second_frame_label = customtkinter.CTkLabel(self.second_frame, text="This is the second frame",
                                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        self.second_frame_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        # add a button to the second frame
        self.second_frame_button = customtkinter.CTkButton(self.second_frame, text="Click me", command=self.second_frame_button_click, width=200)
        self.second_frame_button.grid(row=1, column=0, padx=30, pady=(15, 15))
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def second_frame_button_click(self):
        print("Second frame button clicked")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)



# This is used to initialize the student application window in the login method -> ValidateUser
def _dangerouslyInit(user_data: list) -> None:
    app = teacher_app(user_data=user_data)
    app.mainloop()


if __name__ == "__main__":
    pass