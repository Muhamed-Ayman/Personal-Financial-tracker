import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import  messagebox
from PIL import Image, ImageTk

import sys
import os

# Database setup
conn = sqlite3.connect("the_base.db")
c = conn.cursor()
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)






# ------------------- LOGIN PAGE -------------------
class LoginPage:

      
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Monetra')
        self.window.configure(bg="#ffffff")
      
        self.icon = PhotoImage(file=resource_path('images\\app_logo.png'))  # PNG icon
        self.window.iconphoto(True, self.icon) 
        
        
        img = Image.open(resource_path('images\\entry_bg.png'))
        img = img.resize((426, 40), Image.Resampling.LANCZOS)
        self.entry_bg = ImageTk.PhotoImage(img)
        img2 = Image.open(resource_path('images\\box.png'))
        img2 = img2.resize((426, 47), Image.Resampling.LANCZOS)
        self.box_btn = ImageTk.PhotoImage(img2)
        
        

        self.label_font = ('poppins', 18, "normal")

        
        
        # ----------------- Background -----------------
        self.bg_frame = Image.open(resource_path("images\\background.png"))
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
        
        # ----------------- Username -----------------
        self.username_label = Label(self.lgn_frame, text="Username", bg="#312c3c", fg="#666666",
                                    font=self.label_font)
        self.username_label.place(x=65, y=90)
        self.username_wrong_label= Label(self.lgn_frame, text="Username is not found",font=('OCR A Extended',12), bg="#312c3c", fg="red",width=0,height=0)
        self.username_wrong_label.place(x=78, y=170)
        self.username_wrong_label.place_forget()  
        self.username_bg = Label(self.lgn_frame, bg="#312c3c", image=self.entry_bg)
        self.username_bg.image = self.entry_bg
        self.username_bg.place(x=70, y=128)
        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#3C3A4B", fg="#1c1b19",
                                    font=("yu gothic ui ", 15, "bold"), insertbackground='#6b6a69')

        self.username_entry.place(x=75, y=132, width=410, height=33)

        
        # ----------------- Password -----------------
        self.password_label = Label(self.lgn_frame, text="Password", bg="#312c3c", fg="#666666",
                                    font=self.label_font)
        self.password_label.place(x=65, y=200)
        self.password_wrong_label= Label(self.lgn_frame, text="Incorrect Password",font=("OCR A Extended",12), bg="#312c3c", fg="red",width=0,height=0)
        self.password_wrong_label.place(x=78, y=280)
        self.password_wrong_label.place_forget()
        self.password_bg = Label(self.lgn_frame, bg="#312c3c", image=self.entry_bg)
        self.password_bg.image = self.entry_bg
        self.password_bg.place(x=70, y=238)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#3C3A4B", fg="#1c1b19",
                                    font=("yu gothic ui ", 15, "bold"), insertbackground='#6b6a69',show='•')

        self.password_entry.place(x=75, y=242, width=410, height=33)
        normal_font = font.Font(family="Segoe UI", size=12, weight="bold", underline=0)
        hover_font  = font.Font(family="Segoe UI", size=12, weight="bold", underline=1)
        normal_font2 = font.Font(family="Bahnschrift SemiLight",size=14,weight="bold", underline=0)
        hover_font2  = font.Font(family="Bahnschrift SemiLight",size=14,weight="bold", underline=1)

        img5 = Image.open(resource_path('images\\hide.png'))
        img5 = img5.resize((21, 21), Image.Resampling.LANCZOS)
        self.show_image = ImageTk.PhotoImage(img5)
        img6 = Image.open(resource_path('images\\show.png'))
        img6 = img6.resize((21, 21), Image.Resampling.LANCZOS)
        self.hide_image = ImageTk.PhotoImage(img6)

        
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#3c3a4b", borderwidth=0, background="#3c3a4b", cursor="hand2")
        self.show_button.place(x=460, y=250)
        
        # ----------------- login Button -----------------
        self.log_in_bg = Label(self.lgn_frame, bg="#312c3c", fg="white",image=self.box_btn)
        self.log_in_bg.image = self.box_btn
        self.log_in_bg.place(x=70, y=320)
        self.log_in_btn = Button(self.lgn_frame, text="Log In", bg="#6D54B5",activebackground='#6D54B5',activeforeground="#0C0D0D", fg="white", font=("Segoe UI", 16, "bold"),bd=0,command=self.all_check)
        self.log_in_btn.place(x=240,y=328,width=100,height=30)
        #------------------sub sublogin labels-----------------
        self.forget_pass= Button(self.lgn_frame, text="Forgotten password?", bg="#312c3c", fg="#BAB9B9",bd=0
                                , activebackground="#312c3c", activeforeground="#BAB9B9", cursor="hand2",font=("Bahnschrift SemiLight",14,"bold"),command=self.go_forget_pass_page)
        self.forget_pass.place(x=180, y=374)
        self.username_line = Canvas(self.lgn_frame, width=525, height=2.0, bg="#980398", highlightthickness=0)
        self.username_line.place(x=20, y=425)
        self.username_line = Canvas(self.lgn_frame, width=525, height=2.0, bg="#980398", highlightthickness=0)
        self.username_line.place(x=20, y=432)
        self.signup_label = Label(self.lgn_frame, text="Don't have an account?", bg="#312c3c", fg="#ffffff",font=("Bahnschrift SemiLight",15,"bold"))
        self.signup_label.place(x=131, y=440)
        self.signup_btn = Button(self.lgn_frame, text="Sign up",bd=0, bg="#312c3c",activebackground="#312c3c",activeforeground="#00B3FF", fg="#00B3FF",font=("Bahnschrift SemiLight",15,"bold"), cursor="hand2",command=self.open_signup_page) 
        self.signup_btn.place(x=361, y=436)
        # hover handlers
        def on_enter(e):
            if(e.widget==self.forget_pass):
                e.widget.config(font=hover_font2)
            else:
              e.widget.config(font=hover_font)

        def on_leave(e):
            if(e.widget==self.forget_pass):
                e.widget.config(font=normal_font2)
            else:
              e.widget.config(font=normal_font)
        self.forget_pass.bind("<Enter>", on_enter)
        self.forget_pass.bind("<Leave>", on_leave)






        
        
        

        




    # Password show/hide methods
    


    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="#3c3a4b", borderwidth=0, background="#3c3a4b", cursor="hand2")
        self.hide_button.place(x=460, y=250)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#3c3a4b", borderwidth=0, background="#3c3a4b", cursor="hand2")
        self.show_button.place(x=460, y=250)
        self.password_entry.config(show='•')

    def go_forget_pass_page(self):
        from forget_password_page import page
        page(self.window)


    def all_check(self):
      
      self.username_wrong_label.place_forget()
      self.password_wrong_label.place_forget()

      step2=None
      username=self.username_entry.get()
      password=self.password_entry.get()
      if username=="" or password=="":
        messagebox.showerror("Error","All fields are required")
        return
        
      c.execute("SELECT * FROM users WHERE username = ?", (username,))
      step1 = c.fetchone()
      
      
      
      if not step1 :
        
        
        # self.username_bg.place(x=60, y=130)
        self.username_wrong_label.place(x=78, y=170)
        return
          
      else:
        
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username, password))
        step2 = c.fetchone()
        if not step2:
          
          # self.password_bg.place(x=60, y=238)
          self.password_wrong_label.place(x=78, y=280)
          return
        
      
        else:
          self.password_wrong_label.place_forget()
          self.window.withdraw()
          from main_app import page  
          page(username)
      
    def open_signup_page(self):
        self.window.withdraw()
        from sign_up_page import page  
        page()
      

            

            
        
      






# ------------------- RUN APP -------------------

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()
  



if __name__ == '__main__':
    page()
