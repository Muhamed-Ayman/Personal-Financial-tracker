import email
import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk, Image
import sqlite3
from tkinter import ttk, messagebox
import smtplib # smtplib for sending messages via Email
import random  # random is used to generate random OTP Codes to send to the user
from email.message import EmailMessage # For the structure of the message sent to the user
import os # To create an environment to secure the gmail app password
import sys



conn = sqlite3.connect("the_base.db")
c = conn.cursor()

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ------------------- OTP INPUT CLASS -------------------


# ------------------- LOGIN PAGE -------------------

class forget_Page:

      
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Monetra')
        self.window.configure(bg="#ffffff")
      
        self.icon = PhotoImage(file=resource_path("images\\app_logo.png"))  # PNG icon
        self.window.iconphoto(True, self.icon) 
        
        
        img = Image.open(resource_path("images\\raj.png"))
        img = img.resize((426, 40), Image.Resampling.LANCZOS)
        self.entry_bg = ImageTk.PhotoImage(img)
        img2 = Image.open(resource_path("images\\box.png"))
        img2 = img2.resize((426, 47), Image.Resampling.LANCZOS)
        self.box_btn = ImageTk.PhotoImage(img2)
        self.the_line = ImageTk.PhotoImage(Image.open(resource_path("images\\gf.png")))
        self.subbg = ImageTk.PhotoImage(Image.open(resource_path("images\\sar.png")))
        self.code_bg = ImageTk.PhotoImage(Image.open(resource_path("images\\gof.png")))
        self.mail = ImageTk.PhotoImage(Image.open(resource_path("images\\mail.png")))
        self.label_font = ('poppins', 18, "normal")
        password_instructions = [
            "•Use at least 8 characters",
            "•Use one uppercase letter",
            "•Use one number",
            "•Use one special character (e.g. !@#$%)"
        ]
        self.inst_font = ('poppins', 10, "normal")
        self.sublabel_font = ('poppins', 14, "normal")
        
        # ----------------- Background -----------------
        self.bg_frame = Image.open(resource_path("images\\l7.png"))
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()-20

        # FIXED: Replace ANTIALIAS with Resampling.LANCZOS
        self.bg_frame = self.bg_frame.resize(
            (screen_width, screen_height),
            Image.Resampling.LANCZOS
        )

        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(x=-2,y=0)

        self.lgn_frame = Frame(self.window, bg='#312c3c', width=610, height=580)
        self.lgn_frame.place(x=883, y=252)
        


        # ----------------- quote -----------------
        self.quote_label = Label(self.window, text=" Your Lifetime Financial Partner", bg="#312c3c", fg="#6D54B5")
        self.quote_label.config(font=("Stencil", 25, "bold"))
        self.quote_label.place(x=875, y=207)
        
        # ----------------- email -----------------
        self.email_label = Label(self.lgn_frame, text="Email", bg="#312c3c", fg="#666666",
                                    font=('poppins', 25, "bold"))
        self.email_label.place(x=230, y=75)
        self.email_wrong_label= Label(self.lgn_frame, text="Invlid Email address",font=('OCR A Extended',13,'bold'), bg="#312c3c", fg="red",width=0,height=0)
        self.email_wrong_label.place(x=185, y=170)
        self.email_wrong_label.place_forget()  
        self.email_wrong_label2= Label(self.lgn_frame, text="Email is not found",font=('OCR A Extended',13,'bold'), bg="#312c3c", fg="red",width=0,height=0)
        self.email_wrong_label2.place(x=185, y=170)
        self.email_wrong_label2.place_forget()  
        self.email_bg = Label(self.lgn_frame, bg="#312c3c", image=self.entry_bg)
        self.email_bg.image = self.entry_bg
        self.email_bg.place(x=70, y=128)
        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#3C3A4B", fg="#1c1b19",
                                    font=("yu gothic ui ", 15, "bold"), insertbackground='#6b6a69')

        self.email_entry.place(x=75, y=132, width=410, height=33)



        # ----------------- continue button-----------------
        self.continue_bg = Label(self.lgn_frame, bg="#312c3c", fg="white",image=self.box_btn)
        self.continue_bg.image = self.box_btn
        self.continue_bg.place(x=70, y=314)
        self.continue_btn = Button(self.lgn_frame, text="Continue", bg="#6D54B5",activebackground='#6D54B5',activeforeground="#0C0D0D", fg="white", font=("Segoe UI", 16, "bold"),bd=0,command=self.email_checker)
        self.continue_btn.place(x=235,y=322,width=100,height=30)

  





        #------------------ note -----------------
        self.note_label = Label(self.lgn_frame,  text="📝", font=("Segoe UI", 25),bg="#312c3c",fg="#F6069A")
        self.note_label.place(x=70, y=245)
        self.note_text = Label(self.lgn_frame, text="We’ll send your credentials to your email.", font=("Snap ITC", 12, "normal"), bg="#312c3c", fg="#FFFFFF",width=0,height=0)
        self.note_text.place(x=113, y=250)
        self.note_text2 = Label(self.lgn_frame, text=" Please keep it safe.", font=("Snap ITC", 12, "bold"), bg="#312c3c", fg="#D3FC08",width=0,height=0)
        self.note_text2.place(x=113, y=270)
        # self.note_text.place(x=100, y=250)
    def is_valid_email(self):
            Email = self.email_entry.get()

            if not Email:
                    return False

            # no spaces
            if " " in Email:
                    return False

            # must contain exactly one @
            if Email.count("@") != 1:
                    return False

          

            # domain parts not empty

              

            return True
    def found_email(self):
      Email = self.email_entry.get()
      c.execute("SELECT * FROM users WHERE email =?",(Email, ))
      exists = c.fetchone()
      if exists:
        return True
      else:
        return False
    def email_checker(self):
      self.email_wrong_label.place_forget()
      self.email_wrong_label2.place_forget()
      if  self.is_valid_email()==True:
        if self.found_email()==False:
          self.email_wrong_label2.place(x=185, y=170) 
        else:
          from Emails_to_users import send_forgotten_password_to_user as send_info
          the_email=self.email_entry.get()
          the_username=c.execute("SELECT username FROM users WHERE email =?",(the_email, )).fetchone()[0]
          the_password=c.execute("SELECT password FROM users WHERE email =?",(the_email, )).fetchone()[0]
          send_info(the_email, the_username, the_password)
          messagebox.showinfo("Monetra","The credntials send succefully")
          self.continue_btn.config(state='DISABLED')

          
          
          
          
      else:
        self.email_wrong_label.place(x=185, y=170)
        

        # ----------------- login Button -----------------






            
        
      






# ------------------- RUN APP -------------------
def page(parent):
    
    window = Toplevel(parent)
    forget_Page(window)
    


if __name__ == '__main__':
    page()
