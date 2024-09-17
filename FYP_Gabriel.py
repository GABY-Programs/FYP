import tkinter as Tk
import keyboard
import pyperclip
import pyautogui
import datetime
import time
import psutil
import platform
import os
import pygame
from plyer import notification
import concurrent.futures
import sqlite3
from tkinter import messagebox #messagebox for quiz.
import subprocess
import shutil


def preload_db():
    subprocess.run(["python", "Quiz_db.py",],check=True) #Executes the Quiz_db.py file which creates the db with the quiz contents.


#Popups for each function.
def notif_keylog():
    notification.notify(
        title='⌨️Key Logger Function⌨️(30s)',
        message='Logging started👩🏽‍💻\n'
                'Start typing!!!😀',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_malware():
    notification.notify(
        title='🛑🛑Malware🛑🛑',
        message='Tip: Open task manager to end anti-emulation technique',
        app_icon='Virus.ico',
        timeout=3,
    )


def notif_clipboard():
    notification.notify(
        title='📋Clipboard Logging function📋(15s)',
        message='Start copying content!!! 😀',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_screencapture():
    notification.notify(
        title='🖥️Screen capture Function(20s)🖥️',
        message='1 screenshot every second for 5 seconds',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_func_end():
    notification.notify(
        title='🥳Function Ended!!!🥳',
        message='Thank you for running this function',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_sys_info():
    notification.notify(
        title='💻System Specs Logged💻',
        message='Your system info has been logged',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_app_run():
    notification.notify(
        title='💻Active Apps Logged💻',
        message='Your apps have been logged',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_delete():
    notification.notify(
        title='📃All files created were deleted📃',
        message='Bloat text files deleted🥳',
        app_icon='icon.ico',
        timeout=3,
    )


def notif_2_func_end():
    notification.notify(
        title='🥳Malware shut down🥳',
        message='Task Manager is on, turning off function',
        app_icon='icon.ico',
        timeout=3,
    )


#Creation of readme file. Also pops up the text file that got created.
def read_me():
    file_content = """How to use the functions/buttons:

1. keystroke logging: This function will run for 30 seconds(can exit if 'esc' is pressed)
   and will log all of your key strokes. After pressing the Keystroke Logging button,
   open chrome and start typing as if you were unaware of the keylogger. After the function
   ends, you are able to see sensitive information that a threat actor would have sent to 
   a remote C&C server for analysis. This is one way threat actors can steal emails, 
   passwords, etc.

2. Screen capture: This function will run for 30 seconds and will take a screenshot every
   5 seconds. After pressing the Screen Capture button, start opening files or applications 
   on your computer. After the function ends, you are able to see the screen shots with
   possible sensitive information that a threat actor could use maliciously. These would
   also be send to a C&C server for threat actors to use.

3. Clipboard Logging: This function will run for 30 seconds and will log all of your
   clipboard history. After pressing the Clipboard start copying information such as
   emails, passwords, crypto keys, etc to your clipboard. After the function is ended,
   you can see your clipboard history in a txt file which puts it in perspective how
   easy a threat actor could steal sensitive information.

4. Keystroke logging and Screen Capture: This function will run for 30 seconds. It is a
   combination of 2 functions that would run simultaneously in the real world. Explanations
   are above in area 1 and 2.

5. Stealth mode AKA anti-emulation: This feature is present in nearly all key loggers and
   even in some types of malware. The feature sleeps the malware as soon as the user opens
   a surveillance application suck as process hacker or task manager. When running the
   function, you will be prompted with notifications emulating malware being "active",
   the way you get rid of this is by opening task manager and this sleeps the function.

6. System Specs Logging: This function will log your computer specs information such as
   your cpu, gpu, memory, etc. This feature is used in malware because it allows the
   threat actors to know how much power your computer has and if it is worth it to
   implement a crypto miner on the machine. You are able to view the system specs in the
   txt file that gets created.

7. Logging Running Application: This feature logs all of the running applications on your
   machine and logs them into a txt file. This is used to see all active applications and
   what type of apps the user likes to use. The applications can be viewed in the txt file.

8. Delete Folder and Files: This button deletes all of the files that were created by the
   application and the folder itself. This is to make sure that your machine does not get
   bloated with too many files that you do not need after running the demonstration tool.

9. Open File Location: This button opens the location where all of the screenshots and
   txt files are held. This is to make it easier for you to find the outputs of each
   function.

10. Quiz: The quiz button opens a quiz page and displays the 12 MCQ style questions
    where you have to answer then all and submit the answers. After pressing the quiz
    button, full screen the application(there is a scroll wheel at the bottom) and then
    do the mcq. After completing the mcq, you can press return(also make the windows 
    smaller) and you will be sent back to the main menu.

11. Exit: The Exit button closes the application fully."""

    with open("images_and_files/readme.txt", 'w') as file:
        file.write(file_content)

    try:
        import subprocess
        subprocess.Popen(['notepad.exe', "images_and_files/readme.txt"])
    except Exception as e:
        print(f"Error: {e}")



def log_apps():#Log apps that are running
    new_processes = set() #new set to keep track of all processes
    with open("images_and_files/Logged_Apps.txt", 'w') as log_file:#Create Logged_Apps.txt. Will write to the file(overwrite all old data)
        notif_app_run() #Notif
        for proc in psutil.process_iter(['pid', 'name']):#psutil(python library fore retrieving process info). Retrieves PID + name
            process_name = proc.info['name'].lower()#Makes all process names, lowercase for easier reading for users
            if (not process_name.startswith('svchost')#Ignores all processes with the following starts as they are basic windows apps.
                and not process_name.startswith('system')#If they dont contain the following, they pass the if statement
                and not process_name.startswith('csrss')
                and not process_name.startswith('wininit')
                and not process_name.startswith('winlogon')
                and process_name not in new_processes):#if the process is in new_processes, it continues to next line
                log_file.write(f"{proc.info['pid']}: {process_name}\n")#Logged apps to Logged_apps file in PID: NAME format
                new_processes.add(process_name)#Adds process to net_processes to avoid duplication of logs

#Combined functions for the combined button in GUI, requested by mary davin.
def keystroke_logging_Combined():#Every time a key is pressed, the function log_keys_combined is called and hooks keyboard
    keyboard.hook(log_keys_combined)
    start_time = time.time()

    #When esc button is pressed or the set time passes, the function stops, same as when ctrl+c is pressed. Also keyboard unhooks
    try:
        while True:
            if keyboard.is_pressed("esc"):
                keyboard.unhook(log_keys_combined)
                print("Exiting function")
                break
            if time.time() - start_time >= 15:
                keyboard.unhook(log_keys_combined)
                print("Exiting function")
                break
            time.sleep(1)

    except KeyboardInterrupt:
        pass


def log_keys_combined(event):
    try:
        excluded_keys = ["tab", "caps lock", "shift", "right shift", "backspace", "esc"]
        if keyboard.is_pressed(event.name):#Checks for key presses, not key releases(had issue with this).
            with open("images_and_files/CombinedKeystrokes.txt", "a") as log_file:
                if event.name == "space":#If a space is pressed, it will append a new line in the text file.
                    log_file.write("\n")
                elif event.name.isprintable() and event.name not in excluded_keys:#if a key is pressed it will print except if it's in excluded_keys
                    log_file.write(event.name)
    #Error handling
    except Exception as e:
        print(f"Error: {e}")


def Screen_Capture_Combined(num_screenshots=15, save_path='images_and_files'):#One screenshot every second for the amount of screenshots set currently
    current_directory = os.path.dirname(os.path.realpath(__file__))
    save_directory = os.path.join(current_directory, save_path)
    for i in range(num_screenshots):#when it reaches num_screenshots, it will stop taking screenshots
        try:
            screenshot = pyautogui.screenshot()#creates a screenshot
            timestamp = datetime.datetime.now().strftime("%Y %m %d  %H %M %S")#Save date and time of each screenshot
            screenshot_name = f"{save_path} {timestamp} {i + 1}.png"#Names each screenshot with the '(save_path)screenshot (timestamp)year month day hour minute second' example 'screenshot 2024 02 20  16 10 30 0.png'
            screenshot_path = os.path.join(save_directory, screenshot_name)
            screenshot.save(screenshot_path)#Screenshot gets saved with above name
            print(f"Screenshot saved successfully: {screenshot_name}")#for confirmation, Maybe delete later. Then sleep for 1 second and redo function
            time.sleep(1)
        #Error handling
        except Exception as e:
            print(f"Error: Screenshot {i + 1}: {e}")
            return


#notif for combined function.
def notif_start_combined():
    notification.notify(
        title='⌨️Key Logger Function⌨️(15s)',
        message='Logging and Screen Capture started👩🏽‍💻\n'
                'Start typing!!!😀',
        app_icon='icon.ico',
        timeout=3,
    )

def notif_end_combined():
    notification.notify(
        title='Function Ended',
        message='Thank you for running this function\n'
                'Bye Bye!!!😀',
        app_icon='icon.ico',
        timeout=3,
    )

def combined():
    with concurrent.futures.ThreadPoolExecutor() as executor:#Setting up a ThreadPoolExecutor to run 2 functions at once.
        notif_start_combined()
        features = [executor.submit(keystroke_logging_Combined), executor.submit(Screen_Capture_Combined)]#Runs both functions, names features
        concurrent.futures.wait(features)
        notif_end_combined()#After all features are complete, Notif runs.


#Not combined version of functions. To run individually
def keystroke_logging():#Every time a key is pressed, the function log_keys is called
    keyboard.hook(log_keys)
    start_time = time.time()
    notif_keylog()
    #When esc button is pressed or the set time passes, the function stops, same as when ctrl+c is pressed
    try:
        while True:
            if keyboard.is_pressed("esc"):
                print("Exiting function")
                notif_func_end()
                keyboard.unhook(log_keys)
                break

            if time.time() - start_time >= 30:
                print("Exiting function")
                notif_func_end()
                keyboard.unhook(log_keys)
                break

            time.sleep(1)

    except KeyboardInterrupt:
        pass


def log_keys(event):
    try:
        excluded_keys = ["tab", "caps lock", "shift", "ctrl", "right shift", "backspace", "esc", "enter"]

        if keyboard.is_pressed(event.name):#Checks for key presses, not key releases.
            with open("images_and_files/Keystrokes.txt", "a") as log_file:
                if event.name == "space":#If a space is pressed, it will append a new line in the text file.
                    log_file.write("\n")
                elif event.name.isprintable() and event.name not in excluded_keys:#if a key is pressed it will print except if it is in excluded_keys
                    log_file.write(event.name)
    #Error handling
    except Exception as e:
        print(f"Error: {e}")


def Screen_Capture(num_screenshots=4, save_path='images_and_files'):#One screenshot every second for however many num_screenshots is set
    notif_screencapture()
    current_directory = os.path.dirname(os.path.realpath(__file__))
    save_directory = os.path.join(current_directory, save_path)
    for i in range(num_screenshots):#when it reaches num_screenshots amount, it will stop taking screenshots
        try:
            screenshot = pyautogui.screenshot()#creates a screenshot
            timestamp = datetime.datetime.now().strftime("%Y %m %d  %H %M %S")#Save date and time of each screenshot
            screenshot_name = f"{save_path} {timestamp} {i + 1}.png"#Names each screenshot with the '(save_path)screenshot (timestamp)year month day hour minute second' example 'screenshot 2024 02 20  16 10 30 0.png'
            screenshot_path = os.path.join(save_directory, screenshot_name)
            screenshot.save(screenshot_path)#Screenshot gets saved with above name
            print(f"Screenshot saved successfully: {screenshot_name}")#for confirmation, Maybe delete later. Then sleep for 1 second and redo function
            time.sleep(5)
        #Error handling
        except Exception as e:
            print(f"Error: Screenshot {i + 1}: {e}")
            return
    notif_func_end()


def Clipboard_Monitoring(duration=15):#Runs function for set time in seconds
    notif_clipboard()
    start_time = time.time()#initializing the start time of the function

    def Save_Clipboard(clipboard_content, prev_content):#Nested a function within Clipboard_Monitoring()
        try:
            with open('images_and_files/clipboard_contents.txt', 'a') as file:
                timestamp = datetime.datetime.now().strftime("%Y/%m/%d  %H:%M:%S")
                if clipboard_content != prev_content:#If current clipboard item is not the same as previous clipboard content, go to next line
                    file.write(f"{timestamp}: {clipboard_content}\n\n")#After opening a text file called clipboard_contents.txt, it appends content that is being copied to the txt file. an example is "2024/02/28 17:37:43: Copied content"

                    print(f"Clipboard content saved at {timestamp}")#for confirmation, Maybe delete later.
        #Error handling
        except Exception as e:
            print(f"Error: {e}")

    prev_clipboard_content = pyperclip.paste()#current clipboard content gets initialized as previous clipboard content for later use

    while time.time() - start_time < duration:#Loop continues while duration(15) is higher than start time
        clipboard_content = pyperclip.paste()#Recieves last clipboard item
        if clipboard_content != prev_clipboard_content:#If the current content is not the same as the previous content, continue to next line
            Save_Clipboard(clipboard_content, prev_clipboard_content)#save current clipboard content on top of previous clipboard content
        prev_clipboard_content = clipboard_content#current content becomes previous content, and loop continues after 1 seconds
        time.sleep(1)

    notif_func_end()


def AntiEmulation_Techniques():
    while True:
        for process in psutil.process_iter(['name']):#Only process names are checked
            if 'Taskmgr' in process.info['name']:#If process name 'Taskmgr' is found, process prints out line below and breaks
                notif_2_func_end()
                break
        else:
            time.sleep(4)#If 'Taskmgr' is not found, it will sleep for 1 second then continue and redo the check
            notif_malware()
            continue
        break


def System_Specification_Logging():
    try:
        notif_sys_info()
        #formatting an output to be saved into a file. Sys_info will show OS,Processor type, system architecture type and system memory
        sys_info = f"System Specs:\n\n\
            OS: {platform.system()} {platform.version()}\n\
            Processor: {platform.processor()}\n\
            System Architecture: {platform.architecture()}\n\
            Computer Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
        file_path = 'images_and_files/system_specification.txt'#file name will be system_specification.txt
        with open(file_path, "a") as file:
            file.write(sys_info)#Writes sys_info to the txt file


        print(f"\nSystem Specs were saved to system_specification.txt\n")#for confirmation, Maybe delete later.
    #Error handling
    except Exception as e:
        print(f"Error: {e}")


def delete_files():#Deletes directory for users to not have bloat on their computer.
    notif_delete()
    folder_name = 'images_and_files'
    if os.path.exists(folder_name):
        try:
            shutil.rmtree(folder_name)
            print("deleted")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("not exist")


def quit_command():#Quit Gui/program function
    exit()


def play_start_sound():#Sound that is run when GUI is started
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
    sound = pygame.mixer.Sound('Open_Sound.mp3')#source of sound: https://www.youtube.com/watch?v=I_UR40xOzfY
    sound.play()

def create_folder():#Created folder for all functions
    folder_name =  'images_and_files'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("done")
    else:
        print("already exists")


def open_folder():#Open directory images_and_files when function executed
    folder_name = 'images_and_files'
    if os.path.exists(folder_name):
        os.system('explorer "' + folder_name + '"')
    else:
        print("folder not there")

#TKinter GUI
class gui(Tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.Tk.__init__(self, *args, **kwargs)

        container = Tk.Frame(self)#Creating container configuration
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}#Initializing frame for the GUI

        for page_classes in (MainPage, QuizPage):
            frame = page_classes(container, self)
            self.frames[page_classes] = frame
            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(MainPage)#Show mainpage frame

    def show_frame(self, cont):#If on MainPage, Show buttons for the MainPage Frame, If not on MainPage, forget the button in the frame.
        frame = self.frames[cont]
        frame.tkraise()

        if cont == MainPage:
            self.frames[MainPage].show_buttons()
        else:
            self.frames[MainPage].hide_buttons()


class page(Tk.Frame):#initializing the frame/creating a foundation for creating pages in Tkinter. When creating a page, this will be called because it makes creation easier, showing page and allowing for page changing.
    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        self.controller = controller

    def page_shown(self):
        pass

    def change_page(self, page_classes):
        self.controller.show_frame(page_classes)


class MainPage(page):#Creating the main page. Creating the canvas, creating rectangle and adding text.
    def __init__(self, parent, controller):
        page.__init__(self, parent, controller)

        canvas = Tk.Canvas(
            self,
            bg="#FFFFFF",
            height=500,
            width=700.0,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            100.0,
            fill="#B02626",
            outline=""
        )

        canvas.create_text(
            21.0,
            38.0,
            anchor="nw",
            text="CyberAware Explorer",
            fill="#FFFFFF",
            font=("Inter SemiBold", 20 * -1)
        )
#Creating all of the buttons for the main page which also have a function each+picture.
        button_image_keystroke = Tk.PhotoImage(file="button_keystroke.png")
        self.button_keystroke_image = button_image_keystroke
        self.button_keystroke = Tk.Button(
            command=keystroke_logging,
            image=button_image_keystroke,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )

        button_image_screen = Tk.PhotoImage(file="button_screen.png")
        self.button_screen_image = button_image_screen
        self.button_screen = Tk.Button(
            command=Screen_Capture,
            image=button_image_screen,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )

        button_image_clipboard = Tk.PhotoImage(file="button_clipboard.png")
        self.button_clipboard_image = button_image_clipboard
        self.button_clipboard = Tk.Button(
            image=button_image_clipboard,
            borderwidth=0,
            highlightthickness=0,
            command=Clipboard_Monitoring,
            relief="flat"
        )

        button_image_quiz = Tk.PhotoImage(file="button_quiz.png")
        self.button_quiz_image = button_image_quiz
        self.button_quiz = Tk.Button(
            image=button_image_quiz,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(QuizPage),
            relief="flat"
        )

        button_image_stealth = Tk.PhotoImage(file="button_stealth.png")
        self.button_stealth_image = button_image_stealth
        self.button_stealth = Tk.Button(
            image=button_image_stealth,
            borderwidth=0,
            highlightthickness=0,
            command=AntiEmulation_Techniques,
            relief="flat"
        )

        button_image_specs = Tk.PhotoImage(file="button_specs.png")
        self.button_specs_image = button_image_specs
        self.button_specs = Tk.Button(
            image=button_image_specs,
            borderwidth=0,
            highlightthickness=0,
            command=System_Specification_Logging,
            relief="flat"
        )

        button_image_delete = Tk.PhotoImage(file="button_delete.png")
        self.button_delete_image = button_image_delete
        self.button_delete = Tk.Button(
            image=button_image_delete,
            borderwidth=0,
            highlightthickness=0,
            command=delete_files,
            relief="flat"
        )

        button_image_exit = Tk.PhotoImage(file="button_exit.png")
        self.button_exit_image = button_image_exit
        self.button_exit = Tk.Button(
            image=button_image_exit,
            borderwidth=0,
            highlightthickness=0,
            command=quit_command,
            relief="flat"
        )

        button_image_combined = Tk.PhotoImage(file="button_combined.png")
        self.button_combined_image = button_image_combined
        self.button_combined = Tk.Button(
            image=button_image_combined,
            borderwidth=0,
            highlightthickness=0,
            command=combined,
            relief="flat"
        )

        button_image_location = Tk.PhotoImage(file="button_location.png")
        self.button_location_image = button_image_location
        self.button_location = Tk.Button(
            image=button_image_location,
            borderwidth=0,
            highlightthickness=0,
            command=open_folder,
            relief="flat"
        )

        button_image_instructions = Tk.PhotoImage(file="button_instructions.png")
        self.button_instructions_image = button_image_instructions
        self.button_instructions = Tk.Button(
            image=button_image_instructions,
            borderwidth=0,
            highlightthickness=0,
            command=read_me,
            relief="flat"
        )

        button_image_log_apps = Tk.PhotoImage(file="button_log_apps.png")
        self.button_log_apps_image = button_image_log_apps
        self.button_log_apps = Tk.Button(
            image=button_image_log_apps,
            borderwidth=0,
            highlightthickness=0,
            command=log_apps,
            relief="flat"
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_buttons(self):#Button location + size on main page
        self.button_keystroke.place(x=172.0, y=176.0, width=155, height=45)
        self.button_screen.place(x=172.0, y=240.0, width=155, height=45)
        self.button_clipboard.place(x=172.0, y=303.0, width=155, height=45)
        self.button_quiz.place(x=375.0, y=367.0, width=155, height=45)
        self.button_stealth.place(x=375.0, y=176.0, width=155, height=45)
        self.button_specs.place(x=375.0, y=240.0, width=155, height=45)
        self.button_delete.place(x=375.0, y=303.0, width=155, height=45)
        self.button_exit.place(x=375.0, y=430.0, width=155, height=45)
        self.button_combined.place(x=172.0, y=367.0, width=155, height=45)
        self.button_location.place(x=172.0, y=430.0, width=155, height=45)
        self.button_instructions.place(x=172.0, y=112.0, width=155, height=45)
        self.button_log_apps.place(x=375.0, y=112.0, width=155, height=45)


    def hide_buttons(self):#Function for forgetting all buttons
        self.button_keystroke.place_forget()
        self.button_screen.place_forget()
        self.button_clipboard.place_forget()
        self.button_quiz.place_forget()
        self.button_stealth.place_forget()
        self.button_specs.place_forget()
        self.button_delete.place_forget()
        self.button_exit.place_forget()
        self.button_combined.place_forget()
        self.button_location.place_forget()
        self.button_instructions.place_forget()
        self.button_log_apps.place_forget()


class QuizPage(page):#quiz page
    def evaluate_answers(self):#Answer result messagebox, calculating user quiz result and printing it
        self.correct_answers_count = sum(1 for (user_answer, correct_answer) in self.user_answers.values() if user_answer.get() == correct_answer)
        messagebox.showinfo("Results", f"You got {self.correct_answers_count} out of {len(self.user_answers)} correct!")


    def __init__(self, parent, controller):#Creating Quiz page, canvas, buttons, scrollbar(horizontal because vertical did not work(reason is unknown :( (I tried to fix a long time) ))
        page.__init__(self, parent, controller)

        self.controller = controller
        self.user_answers = {}
        self.correct_answers_count = 0

        # Main canvas setup
        self.main_canvas = Tk.Canvas(self, bg="#FFFFFF", height=500, width=700.0, bd=0, highlightthickness=0, relief="ridge", xscrollcommand=lambda *args: self.xview(*args))
        self.main_canvas.pack(side="top", fill="both", expand=True)

        # Horizontal scrollbar setup
        self.scrollbar = Tk.Scrollbar(self, orient="horizontal", command=self.main_canvas.xview, bg="red")
        self.scrollbar.pack(side="bottom", fill="x")
        self.main_canvas.configure(xscrollcommand=self.scrollbar.set)

        # Frame to hold the content inside the main canvas
        self.quiz_frame = Tk.Frame(self.main_canvas, bg="#FFFFFF")
        self.canvas_window = self.main_canvas.create_window((0, 0), window=self.quiz_frame, anchor="nw")

        self.quiz_frame.bind("<Configure>", self.on_frame_configure)

        # Header rectangle and text
        self.header_canvas = Tk.Canvas(self.quiz_frame, bg="#FFFFFF", height=100, width=20, highlightthickness=0, relief='flat')
        self.header_canvas.grid(row=0, column=0, columnspan=4, sticky="ew")
        self.header_canvas.create_text(74, 50, text="Quiz", fill="#B02626", font=("Inter SemiBold", 20 * -1))

        #3 buttons created, quit, return, submit
        self.button_return = Tk.PhotoImage(file="button_return.png")
        return_back = Tk.Button(
            self.header_canvas,
            image=self.button_return,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(MainPage),
            relief="flat"
        )
        return_back.place(x=100, y=5, width=62, height=27)

        self.quit = Tk.PhotoImage(file="button_quit.png")
        quit_button = Tk.Button(
            self.header_canvas,
            image=self.quit,
            borderwidth=0,
            highlightthickness=0,
            command=quit_command,
            relief="flat"
        )
        quit_button.place(x=198.0, y=5.0, width=62, height=27)

        self.submit = Tk.PhotoImage(file="button_submit.png")
        submit_button = Tk.Button(
            self.header_canvas,
            image=self.submit,
            borderwidth=0,
            highlightthickness=0,
            command=self.evaluate_answers,
            relief="flat"
        )
        submit_button.place(x=540.0, y=5.0, width=62, height=27)

        self.load_questions()
    def on_frame_configure(self, event=None):
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

    def xview(self, *args):
        self.main_canvas.xview(*args)

    def load_questions(self):#connect to quizdb and load questions from the database
        with sqlite3.connect('gabriel.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM quiz')
            questions = c.fetchall()

        self.answer_vars = {}#DB questions and answers are in a MCQ format. I added 12 questions in the quiz db.
        for index, (q_id, question, a1, a2, a3, a4, correct) in enumerate(questions, start=1):
            column_index = (index - 1) % 3
            if index in [1, 2, 3]:
                row_index = ((index - 1) // 3) * 5
            else:
                row_index = 3 * 5 + ((index - 4) // 3) * 6

            self.answer_vars[q_id] = Tk.StringVar(value="0")

            # Create a frame for the question label to act as a border
            question_frame = Tk.Frame(self.quiz_frame, bd=1, relief='solid', bg='black')
            question_frame.grid(row=row_index, column=column_index * 2, sticky="w", padx=35, pady=2)


            question_label = Tk.Label(question_frame, text=f"{index}. {question}", justify="left", bg="#FF9393")
            question_label.pack(padx=1, pady=1)  #Quiz question padding

            #Creating a spacer for questions(Making format look nicer)
            if index not in [1, 2, 3]:
                spacer_label = Tk.Label(self.quiz_frame, text="", justify="left", bg="#FFFFFF")
                spacer_label.grid(row=row_index + 1, column=column_index * 2, sticky="w", padx=35, pady=2)
                answer_start_row = row_index + 2
            else:
                answer_start_row = row_index + 1

            #Quiz answers have a radio style button.
            for i, option in enumerate([a1, a2, a3, a4], start=1):
                rb = Tk.Radiobutton(self.quiz_frame, text=option, variable=self.answer_vars[q_id], value=option,
                                    bg="#FFFFFF")
                rb.grid(row=answer_start_row + i - 1, column=column_index * 2, sticky="w", padx=50)

            self.user_answers[q_id] = (self.answer_vars[q_id], correct)

if __name__ == '__main__':
    create_folder()
    preload_db()
    window = gui()
    window.geometry("700x500")
    window.title("Keylogger FYP Software")
    play_start_sound()
    window.iconbitmap('icon.ico')
    window.mainloop()
