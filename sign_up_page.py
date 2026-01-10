import email
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, Image
import sqlite3
import sys
import os




# ------------------- OTP INPUT CLASS -------------------
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
class signPage:

        
      
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Monetra')

        
      
        self.icon = PhotoImage(file=resource_path("images\\app_logo.png")) # PNG icon
        self.window.iconphoto(True, self.icon) 

        self.label_font = ('poppins', 18, "normal")
        password_instructions = [
            "•Use at least 8 characters",
            "•Use one uppercase letter",
            "•Use one number",
            "•Use one special character (e.g. !@#$%)"
        ]
        self.inst_font = ('poppins', 11, "normal")
        
        
        # ----------------- Background -----------------


        self.window.configure(bg="#413E4B")
        self.lgn_frame = Frame(self.window, bg="#413E4B", width=1340, height=735)
        self.lgn_frame.place(x=100, y=63)
        
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#ffffff",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ----------------- Side Image -----------------
        img__bg = Image.open(resource_path("images\\bg_panel.png"))
        img__bg = img__bg.resize((1335, 725), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img__bg)
        self.side_image_label = Label(self.lgn_frame, image=self.bg, bg="#413E4B")
        self.side_image_label.image = self.bg
        self.side_image_label.place(x=0, y=5)
        self.signword=Label(self.lgn_frame,text="Sign Up",font=("Poppines",40,"bold"),bg="#ffffff",fg="#413E4B")
        self.signword.place(x=550,y=30)
        self.name_label = Label(self.lgn_frame, text="M o n e t r a", font=("Stencil", 52, "bold"), bg="#2d2638", fg="#C7A8FF",height=-10000)
        self.name_label.place(x=30, y=200)
        img11 = Image.open(resource_path("images\\dollar_bag_sign.png"))
        img11 = img11.resize((65, 85), Image.Resampling.LANCZOS)
        self.dollar_bag_sign = ImageTk.PhotoImage(img11)
        self.dollar_bag_sign_label=Label(self.lgn_frame,image=self.dollar_bag_sign,bg="#2d2638")
        self.dollar_bag_sign_label.image = self.dollar_bag_sign
        self.dollar_bag_sign_label.place(x=98,y=190)
        self.quote_label1 = Label(self.lgn_frame, text="Start", bg="#2d2638", fg="#6D54B5")
        self.quote_label1.config(font=("Forte", 45, "bold"))
        self.quote_label1.place(x=15, y=357)
        self.quote_label2 = Label(self.lgn_frame, text="our jourey", bg="#2d2638", fg="#6D54B5")
        self.quote_label2.config(font=("Forte", 40, "bold"))
        self.quote_label2.place(x=15, y=447)


        # ----------------- Username -----------------
        self.username = Entry(self.lgn_frame, fg="#BEBEBE",bg="#ffffff",relief='flat', font=("Arial", 15,'normal'),width=45)
        self.username.placeholder = "Username"
        self.username.insert(0, "Username")
        self.username.place(x=600, y=165)
        self.und_line=Canvas(self.lgn_frame,width=550,height=1.5,bg="#d0d0d0",highlightthickness=0)
        self.und_line.place(x=597,y=200)
        self.username.bind("<FocusIn>", self.on_focus_in)
        self.username.bind("<FocusOut>", self.on_focus_out)
  

        self.username_wrong_label= Label(self.lgn_frame, text="Username already taken", bg="#ffffff", fg="red",font=("OCR A Extended",11),width=0,height=0)
        self.username_wrong_label.place(x=600, y=205)
        self.username_wrong_label.place_forget()
        self.username_wrong_label2= Label(self.lgn_frame, text="Empty field", bg="#ffffff", fg="red",font=("OCR A Extended",11),width=0,height=0)
        self.username_wrong_label2.place(x=600, y=205)
        self.username_wrong_label2.place_forget()

        
    #     # ----------------- Password -----------------
        self.password = Entry(self.lgn_frame, fg="#BEBEBE",bg="#ffffff",relief='flat', font=("Arial", 15,'normal'),show='',width=45)
        self.password.placeholder = "Password"
        self.password.insert(0, "Password")
        self.password.place(x=600, y=270)
        img52= Image.open(resource_path("images\\hide.png"))
        img52= img52.resize((20,20), Image.Resampling.LANCZOS)
        self.hide = ImageTk.PhotoImage(img52)
        img51= Image.open(resource_path("images\\show.png"))
        img51= img51.resize((20,20), Image.Resampling.LANCZOS)
        self.show=ImageTk.PhotoImage(img51)

        
        
        

        

        self.und_line3=Canvas(self.lgn_frame,width=550,height=1.5,bg="#d0d0d0",highlightthickness=0)
        self.und_line3.place(x=597,y=305)
        self.password.bind("<FocusIn>", self.on_focus_in)
        
        self.password.bind("<FocusOut>", self.on_focus_out)
        
        self.pass_wrong_label= Label(self.lgn_frame, text="Password does not meet requirements",font=("OCR A Extended",11),bg="#ffffff", fg="red",width=0,height=0)
        self.pass_wrong_label.place(x=600, y=310)
        self.pass_wrong_label.place_forget()
        

        # Password instructions
        self.password_instructions1 = Label(self.lgn_frame, text=password_instructions[0], bg="#ffffff", fg="#A3A3A3", font=self.inst_font)
        self.password_instructions1.place(x=600, y=335)
        self.password_instructions2 = Label(self.lgn_frame, text=password_instructions[1], bg="#ffffff", fg="#A3A3A3", font=self.inst_font)
        self.password_instructions2.place(x=600, y=360)
        self.password_instructions3 = Label(self.lgn_frame, text=password_instructions[2], bg="#ffffff", fg="#A3A3A3", font=self.inst_font)
        self.password_instructions3.place(x=870, y=335)
        self.password_instructions4 = Label(self.lgn_frame, text=password_instructions[3], bg="#ffffff", fg="#A3A3A3", font=self.inst_font)
        self.password_instructions4.place(x=870, y=360)

    #     # ----------------- Confirm Password -----------------
        self.confirmpassword = Entry(self.lgn_frame, fg="#BEBEBE",bg="#ffffff",relief='flat', font=("Arial", 15,'normal'),width=45)
        self.confirmpassword.placeholder = "Confirm password"
        self.confirmpassword.insert(0, "Confirm password")
        self.confirmpassword.place(x=600, y=425)
        self.confirmpassword.bind("<FocusIn>", self.on_focus_in)
        self.confirmpassword.bind("<FocusOut>", self.on_focus_out)
        self.und_line4=Canvas(self.lgn_frame,width=550,height=1.5,bg="#d0d0d0",highlightthickness=0)
        self.und_line4.place(x=597,y=460)        
        
        self.confirm_wrong_label= Label(self.lgn_frame, text="Confirm password mismatch",font=("OCR A Extended",11), bg="#ffffff", fg="red",width=0,height=0)
        self.confirm_wrong_label.place(x=600, y=465)
        self.confirm_wrong_label.place_forget()
        self.mini_show_button=Button(self.lgn_frame,image=self.hide,bg="#ffffff",relief='flat',activebackground="#ffffff",cursor="hand2", borderwidth=0,command=self.show_hide)
        self.mini_show_button2=Button(self.lgn_frame,image=self.hide,bg="#ffffff",relief='flat',activebackground="#ffffff",cursor="hand2", borderwidth=0,command=self.show_hide2)

  
    #     #==================================================================
    #     # ============================continue button=========================
    #     # =================================================================
        img_continue = Image.open(resource_path("images\\continue.png"))
        img_continue = img_continue.resize((300, 80), Image.Resampling.LANCZOS)
        self.continue_img = ImageTk.PhotoImage(img_continue)
        self.continue_button = Button(self.lgn_frame, image=self.continue_img, bd=0,bg='#ffffff',fg="#05497d",relief='flat',cursor="hand2",activebackground="#ffffff",borderwidth=0,command=self.all_chreditials_page1)
        self.continue_button.image=self.continue_img
        self.continue_button.place(x=560, y=520)
    
    def on_focus_in(self, event):
        self.e = event.widget
        if self.e.get() == self.e.placeholder:
            self.e.delete(0, tk.END)
            self.e.config(fg="black")
        if event.widget == self.password:
            self.password.config(show='•')
            self.mini_show_button.place(x=1120,y=275)
        if event.widget == self.confirmpassword:
            self.confirmpassword.config(show='•')
            self.mini_show_button2.place(x=1120,y=425)
        

    def on_focus_out(self, event):
        self.e = event.widget
        if self.e.get() == "":
            self.e.insert(0, self.e.placeholder)
            self.e.config(fg="gray")
            if event.widget == self.password:
                self.mini_show_button.place_forget()
                self.password.config(show='')
            if event.widget == self.confirmpassword:
                self.mini_show_button2.place_forget()
                self.confirmpassword.config(show='')
   

    def userfunc(self):
        username=self.username.get()
        c.execute("SELECT * FROM users WHERE username =?",(username, ))
        exists = c.fetchone()
        if username=="" or username=="Username":
          self.username_wrong_label.place_forget()
          self.username_wrong_label2.place(x=600, y=205)
          
          return False
          
        if exists and username!="":
        
          self.username_wrong_label.place(x=600, y=205)
          return False
        else:
          self.username_wrong_label.place_forget()
          return True


            

    def Passfunc(self):
 
      pas=self.password.get()
      if(len(pas)>=8 and any(char.isupper() for char in pas) and any(char.isdigit() for char in pas) and any(not char.isalnum() for char in pas)):
        self.pass_wrong_label.place_forget()
        return True
      else:
        
        self.pass_wrong_label.place(x=600, y=310)
        return False
    def Confirmpasswordd(self):
    
      if(self.confirmpassword.get() != self.password.get()):
          
          self.confirm_wrong_label.place(x=600, y=465)
          return False 
      else:
          self.confirm_wrong_label.place_forget()
          return True        
        


    def all_chreditials_page1(self):
      if(self.username.get()=="Username" or self.password.get()=="Password" or self.confirmpassword.get()=="Confirm password"):
          messagebox.showerror("Error","All fields are required")
          return
      if( self.userfunc() and self.Passfunc() and self.Confirmpasswordd() ):
            username = self.username.get()
            password = self.password.get()
            self.window.withdraw()

          
            from otp_page import page as nxt_page 
            nxt_page(username, password)
              
            

            

      

            

            
        
    def show_hide(self):
      
      
      if self.password.cget('show') == '':
          self.password.config(show='•')
          self.mini_show_button.config(image=self.hide)
          
      else:
          self.password.config(show='')
          self.mini_show_button.config(image=self.show)
    def show_hide2(self):
      
      
      if self.confirmpassword.cget('show') == '':
          self.confirmpassword.config(show='•')
          self.mini_show_button2.config(image=self.hide)
          
      else:
          self.confirmpassword.config(show='')
          self.mini_show_button2.config(image=self.show)







          




# ------------------- RUN APP -------------------
def page():
    window = Toplevel()
    signPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()