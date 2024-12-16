from tkinter import *
from tkinter import messagebox
from datetime import datetime



###########
### GUI ###
###########



# # BASIC PROGRAM WINDOW #

# # Instantiating the app:
# app = Tk()

# # Setting title:
# app.title("University of Chester")

# # Window sizing and positioning:
# app.geometry("470x115+55+200")      # width x height + position horizontal + positon vertical

# # Creating labels:
# l1 = Label(text="Hello")
# l1.grid(row=0, column=0, ipadx=5)

# l2 = Label(text="These columns are not the same width")
# l2.grid(row=0, column=1, ipadx=5, columnspan=2)

# l3 = Label(text="World")
# l3.grid(row=0, column=3)

# l4 = Label(text="Col0")
# l4.grid(row=1, column=0)

# l5 = Label(text="Col1")
# l5.grid(row=1, column=1)

# l6 = Label(text="Col2")
# l6.grid(row=1, column=2)

# l7 = Label(text="Col3")
# l7.grid(row=1, column=3)

# l8 = Label(text="Col1")
# l8.grid(row=2, column=1, sticky=E)      # Moves the text N S E or W within the cell.

# l9 = Label(text="Col2")
# l9.grid(row=2, column=2, sticky=W)

# # Infinite loop for running main window:
# app.mainloop()



# LOGIN GUI #

# Create MainFrame class:
class MainFrame(Frame):     # Frame is a class in Tkinter that is used to create a container or sub-window within an applicaton.

    # Initialise the frame:
    def __init__(self, master):
        super().__init__(master)
        self.grid()     # Applies grid layout to MainFrame.
        self.create_widgets()
    
    # Create the widgets within the frame:
    def create_widgets(self):
         
         # Row 0:
         self.l1 = Label(self, text="Please enter your name and passcode:")
         self.l1.grid(row=0, column=0, ipadx=5, columnspan=2)   # ipadx = internal padding, x axis.

         # Row 1
         self.l1 = Label(self, text="Name:")
         self.l1.grid(row=1, column=0, ipadx=10, sticky=E)
         
         self.e1 = Entry(self)
         self.e1.grid(row=1, column=1, columnspan=2)

         self.my_check = BooleanVar()
         self.c1 = Checkbutton(self, text="New Visitor?", variable=self.my_check, onvalue=True, offvalue=False)
         self.c1.grid(row=1, column=3)

         # Row 2
         self.l2 = Label(self, text="Passcode:")
         self.l2.grid(row=2, column=0, ipadx=10, sticky=E)

         self.e2 = Entry(self)
         self.e2.grid(row=2, column=1, columnspan=2)

         # Row 3
         self.b1 = Button(self, text='  Submit  ', command=self.submit_name, bg="#7ABF8D")
         self.b1.grid(row=3, column=3, columnspan=2)

         self.l3 = Label(self, text="Date (DD/MM/YYYY)")
         self.l3.grid(row=3, column=0, ipadx=10, sticky=E)

         self.d1 = Entry(self)
         self.d1.grid(row=3, column=1)

    # Function for submitting
    def submit_name(self):
        form_status = self.form_check()

        if form_status == "":
            my_name = self.e1.get()
            my_passcode = self.e2.get()
            my_new_visitor = self.my_check.get()
            my_date = self.d1.get()
            print(f"{my_name} has entered the passcode {my_passcode} with new visitor flag: {my_new_visitor}. Date: {my_date}")
            self.reset()
        else:
            message_text = f"Errors on form:\n\n{form_status}"
            print(message_text)
            messagebox.showerror("Error", message_text)

    # Function for resetting
    def reset(self):
        self.e1.delete(0, "end")
        self.e2.delete(0, "end")
        self.e1.focus()
        self.my_check.set(False)

    #
    def form_check(self):
        form_status = ""

        # Check that entry box is not blank
        if self.e1.get() == "":
            print("Error: You must enter a name.")
            form_status = "- Missing name \n"

        if self.e2.get() == "":
            print("Error: You must enter a passcode.")
            form_status += "- Missing passcode \n"

        if self.d1.get() == "":
            print("Error: You must enter a date.")
            form_status += "- Missing date \n"

        # Check for integer
        try:
            int_passcode = int(self.e2.get())
        except ValueError:
            print("Error: Passcode is not a number.")
            form_status += "- Passcode is not a number \n"

        # Check for valid date
        format = "%d/%m/%Y"
        try:
            result = bool(datetime.strptime(self.d1.get(), format))    # strptime = "string parse time".
        except ValueError:
            print("Error: Date is not valid.")
            form_status += "- Date is not valid \n"

        form_status = form_status[:-2]

        return form_status




# Starting the TKinter event loop:
if __name__ == "__main__":
    root = Tk()
    root.title("Login GUI")
    root.geometry("400x125")
    app = MainFrame(root)
    app.mainloop()
