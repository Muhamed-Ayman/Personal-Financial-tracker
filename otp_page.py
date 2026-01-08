import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import sys
import os



conn = sqlite3.connect("the_base.db")
c = conn.cursor()
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class OTPPage:
    def __init__(self, window,username=None, password=None):
        self.window = window
        

        self.the_username = username
        self.the_password = password
        self.counter = 60
        self.timer_running = False
        
        # Configure window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Monetra')
        
        # Icon

        self.icon = PhotoImage(file=resource_path("images\\app_logo.png"))
        self.window.iconphoto(True, self.icon)


        
        # Background
        self.window.configure(bg="#413E4B")
        self.lgn_frame = Frame(self.window, bg="#413E4B", width=1340, height=735)
        self.lgn_frame.place(x=100, y=63)
        
        # Side Image

        img32 = Image.open(resource_path("images\\bg_panel.png"))
        img32 = img32.resize((1335, 725), Image.Resampling.LANCZOS)
        self.b0g = ImageTk.PhotoImage(img32)
        self.side_image_label = Label(self.lgn_frame, image=self.b0g, bg="#413E4B")
        self.side_image_label.image = self.b0g
        self.side_image_label.place(x=0, y=5)
        # Create OTP verification UI
        
        self.name_label = Label(self.lgn_frame, text="M o n e t r a", font=("Stencil", 52, "bold"), bg="#2d2638", fg="#C7A8FF",height=-10000)
        self.name_label.place(x=30, y=200)
        img11 = Image.open(resource_path("images\\mon.png"))
        img11 = img11.resize((65, 85), Image.Resampling.LANCZOS)
        self.logo2 = ImageTk.PhotoImage(img11)
        self.logos2_label=Label(self.lgn_frame,image=self.logo2,bg="#2d2638")
        self.logos2_label.image = self.logo2
        self.logos2_label.place(x=98,y=190)
        self.quote_label1 = Label(self.lgn_frame, text="Security &", bg="#2d2638", fg="#6D54B5")
        self.quote_label1.config(font=("Forte", 43, "bold"))
        self.quote_label1.place(x=13, y=357)
        self.quote_label2 = Label(self.lgn_frame, text="privacy are", bg="#2d2638", fg="#6D54B5")
        self.quote_label2.config(font=("Forte", 42, "bold"))
        self.quote_label2.place(x=13, y=430)
        self.quote_label2 = Label(self.lgn_frame, text="our top priorities.", bg="#2d2638", fg="#6D54B5")
        self.quote_label2.config(font=("Forte", 25, "bold"))
        self.quote_label2.place(x=13, y=500)        
        # Start countdown
        self.time_left=None
        

        img33 = Image.open(resource_path("images\\joy.png"))
        img33 = img33.resize((400, 65), Image.Resampling.LANCZOS)
        self.email_bg_img = ImageTk.PhotoImage(img33)
        img35 = Image.open(resource_path("images\\joy2.png"))
        img35 = img35.resize((400, 65), Image.Resampling.LANCZOS)
        self.email_bg_act = ImageTk.PhotoImage(img35)
        self.email_bg=Label(self.lgn_frame,bg="#ffffff",image=self.email_bg_img)
        # self.email_bg.image = self.resend_img
        self.email_bg.place(x=650,y=150,width=405,height=70)     
        self.note=Label(self.lgn_frame,text="•",font=("Arial", 22,'bold'),bg="#ffffff")
        self.note.place(x=600,y=96)        
        self.note=Label(self.lgn_frame,text="Enter your email to confirm your account.",font=("Arial", 15,'underline'),bg="#ffffff")
        self.note.place(x=614,y=100)
                             

        # self.eemail.place_forget()
        self.Email = Entry(self.lgn_frame, fg="#000000",bg="#f3f5f7",relief='flat', font=("Arial", 15,'normal'),width=30)
        
        

        self.Email.place(x=666, y=177)
        self.eemail=Label(self.lgn_frame,text="Email",font=("Arial",16,"normal"),bg="#f3f5f7",fg="#b7b7b9")
        self.eemail.place(x=665,y=168)
        self.the_email=Label(self.lgn_frame,text="Email",font=("Arial",12,"normal"),bg="#f3f5f7",fg="#b7b7b9")
        self.the_email.place(x=664,y=157)
        self.the_email.place_forget()
        self.Email.bind("<FocusIn>", self.on_focus_in)
        self.Email.bind("<FocusOut>", self.on_focus_out)      
        self.email_wrong_label = Label(self.lgn_frame, text="Invalid email address", bg="#ffffff",font=("OCR A Extended",11), fg="red",width=0,height=0,padx=0,pady=0)
        self.email_wrong_label.place(x=650, y=220)
        self.email_wrong_label.place_forget()
        self.email_wrong_label2 = Label(self.lgn_frame, text="Email is used before", bg="#ffffff",font=("OCR A Extended",11), fg="red",width=0,height=0,padx=0,pady=0)
        self.email_wrong_label2.place(x=650, y=220)
        self.email_wrong_label2.place_forget()

        img85 = Image.open(resource_path("images\\verify.png"))
        img85 = img85.resize((200, 50), Image.Resampling.LANCZOS)
        self.verify_img = ImageTk.PhotoImage(img85)
        self.email_verify_button = Button(self.lgn_frame, text="Verify", font=("Berlin Sans FB Demi",19,"bold"), bd=0,bg='#ffffff',fg="#05497d",activebackground="#ffffff",borderwidth=0,border=0,image=self.verify_img,relief='flat',command=self.verify_email)        
        self.email_verify_button.config(state='disabled')
        self.email_verify_button.place(x=1090, y=158)
        
      
        self.otp_frame = Frame(self.lgn_frame, bg="#ffffff")
        # self.otp_frame.place(x=550,y=240,width=750,height=480)
        self.otp_img=Image.open(resource_path("images\\otp.png"))
        self.otp_img=self.otp_img.resize((265,150),Image.Resampling.LANCZOS)
        self.otp_img=ImageTk.PhotoImage(self.otp_img)
        self.otp_label=Label(self.otp_frame,image=self.otp_img,bg="#ffffff")
        self.otp_label.image=self.otp_img
        self.otp_label.place(x=230,y=1)
        img2008= Image.open(resource_path("images\\email_note.png"))
        img2008 = img2008.resize((425, 30), Image.Resampling.LANCZOS)
        self.otp_email_img = ImageTk.PhotoImage(img2008)
        
        self.note_opt1=Label(self.otp_frame,image=self.otp_email_img,bg="#ffffff")
        self.note_opt1.image=self.otp_email_img
        self.note_opt1.place(x=155,y=168)
        self.note2_opt1=Label(self.otp_frame,text=" we’ve sent a 6-digit verification code to your email. Enter the code below to confirm and continue setting up your account",font=("Agency FB", 13),bg="#ffffff",fg="#000000",heigh=0)
        self.note2_opt1.place(x=60,y=195)
        self.note2_opt1=Label(self.otp_frame,text="If you don’t see it, check your spam or junk folder—it may take a moment to arrive",font=("Agency FB", 13),bg="#ffffff",fg="#000000",heigh=0)
        self.note2_opt1.place(x=160,y=218)

        
        img87 = Image.open(resource_path("images\\otp_bg.png"))
        img87 = img87.resize((65, 70), Image.Resampling.LANCZOS)
        self.otp_bg = ImageTk.PhotoImage(img87)
        self.otp_bg_label = Label(self.otp_frame, bg="#ffffff",image=self.otp_bg)
        self.otp_bg_label.image = self.otp_bg
      
        
        img45= Image.open(resource_path("images\\otp_bg_act.png"))
        img45 = img45.resize((72, 78), Image.Resampling.LANCZOS)
        self.otp_bg_act = ImageTk.PhotoImage(img45)
        self.otp_bg_label_act = Label(self.otp_frame, bg="#ffffff",image=self.otp_bg_act)
        # self.otp_bg_label_act.place(x=550,y=230,width=76,height=82)
        # self.otp_bg_label.place(x=400,y=230,width=69,height=74)
        img42= Image.open(resource_path("images\\checkkk.png"))
        img42 = img42.resize((320, 100), Image.Resampling.LANCZOS)
        self.check_img = ImageTk.PhotoImage(img42)
        img43= Image.open(resource_path("images\\wrongg.png"))
        img43 = img43.resize((320, 100), Image.Resampling.LANCZOS)
        self.the_wrong_img = ImageTk.PhotoImage(img43)
        img45= Image.open(resource_path("images\\correcttt.png"))
        img45 = img45.resize((320, 100), Image.Resampling.LANCZOS)
        self.the_correct_img = ImageTk.PhotoImage(img45)
     
   
        self.check_btn = Button(self.otp_frame, bg="#ffffff",activebackground="#ffffff",image=self.check_img,bd=0,height=110,relief='flat',border=0,borderwidth=0,command=self.verify_otp)
        self.check_btn.place(x=220,y=330)
        self.exp1=Label(self.otp_frame,text="This code will expire after",font=("Arial", 14,'normal'),bg="#ffffff",fg="#858585",heigh=0)        
        
        self.exp2=Label(self.otp_frame,text="The code is expired. ",font=("Arial", 14,'normal'),bg="#ffffff",fg="#858585",heigh=0)        
        
        
        
        self.exp=Label(self.otp_frame,text="",font=("Berlin Sans FB Demi", 18,'bold'),bg="#ffffff",fg="#858585",heigh=0)        
        
        self.reverify=Label(self.otp_frame,text="veriy your account again",font=("OCR A Extended",16,'underline'),bg="#ffffff",fg="#3B2F32",heigh=0,cursor="hand2") 
        
        
        
        self.create_widgets()


        
                             
        

    def countdown(self):
        if self.time_left >= 0:
            self.exp.config(text=str(self.time_left))
            self.time_left -= 1
            self.window.after(1000, self.countdown)
        else:
            
            self.exp.place_forget()
            self.exp1.place_forget()
            self.exp2.place(x=298,y=417)
            self.check_btn.config(state='disabled')
            self.reverify.place(x=222,y=440)
            
            
            self.email_verify_button.config(state='normal')
            
                                                           
                                          
        

    def is_valid_email(self):
                email = self.Email.get()

                if not email:
                        return False

                # no spaces
                if " " in email:
                        return False

                # must contain exactly one @
                if email.count("@") != 1:
                        return False
                return True



    def unique_email(self):
                email = self.Email.get()
                c.execute("SELECT * FROM users WHERE email =?",(email, ))
                exists = c.fetchone()
                if exists:
                        return False
                else:
                        return True
    def verify_email(self):
                if not self.is_valid_email():
                        self.email_wrong_label.place(x=650, y=220)
                        return False
                else:
                        self.email_wrong_label.place_forget()

                if not self.unique_email():
                        self.email_wrong_label2.place(x=650, y=220)
                        return False
                else:
                        self.email_wrong_label2.place_forget()
                        self.email_wrong_label.place_forget()
                        self.generate_otp()
                        self.otp_frame.place(x=550,y=240,width=750,height=480)
                        
                        self.email_verify_button.config(state='disabled')
                        self.exp2.place_forget()
                        self.exp1.place(x=254,y=419)
                        self.exp.place(x=476,y=416)
                        
                        self.reverify.place_forget()
                        
                        self.check_btn.config(state='normal')

                        self.time_left = 60
                        
                        self.countdown()
                        
                        
                return True
        
    
    def create_widgets(self):
        # OTP Entry Frame - centered in white area
        otp_x_start = 100
        otp_y = 260
        
        # Create 6 OTP entry boxes
        self.otp_entries = []
        for i in range(6):
            otp_bg=Label(self.otp_frame,image=self.otp_bg,bg="#ffffff",width=70,height=75)
            otp_bg.image=self.otp_bg
            entry = Entry(
                self.otp_frame,
                font=("Arial", 28, "bold"),
                width=3,
                justify=CENTER,
                bg="#ededed",
                fg="#413E4B",
                relief='flat',
              
            )

            otp_bg.place(x=otp_x_start + (i * 97),y=otp_y,width=70,height=75)
            entry.place(x=otp_x_start + (i * 97)+10, y=otp_y+10, width=50, height=55)
          
          
            entry.bind("<KeyRelease>", lambda e, idx=i: self.on_key_release(e, idx))
            entry.bind("<BackSpace>", lambda e, idx=i: self.on_backspace(e, idx))
            self.otp_entries.append(entry)
        
        # Focus on first entry
        self.otp_entries[0].focus()
        
        # Timer Label

      
    
    def on_key_release(self, event, index):
        """Move to next entry when a digit is entered"""
        entry = self.otp_entries[index]
        text = entry.get()
        
      
        self.check_btn.config(image=self.check_img)
        
        
        if text and not text.isdigit():
            entry.delete(0, END)
            return
        
        if len(text) > 1:
            entry.delete(1, END)
            text = text[0]
        
        
        if text and index < 5:
            self.otp_entries[index + 1].focus()
        
      

    
    def on_backspace(self, event, index):

        entry = self.otp_entries[index]
        
        
        self.check_btn.config(image=self.check_img)
        
        if not entry.get() and index > 0:
            self.otp_entries[index - 1].focus()
            self.otp_entries[index - 1].delete(0, END)
    

    


    def generate_otp(self):
      Email=self.Email.get()

      from Emails_to_users import send_otp
      try:
          self.correct_otp = str(send_otp(Email))
          
      except:
  
          self.correct_otp = "123456"     
    def verify_otp(self):
        """Verify the entered OTP"""
        otp = "".join([entry.get() for entry in self.otp_entries])
        
        if len(otp) != 6:
            messagebox.showerror("Error", "Please enter all 6 digits")
            return
        
        
        print(self.correct_otp)
        # Verify OTP
        if otp == self.correct_otp:
            self.check_btn.config(image=self.the_correct_img)
            # Here you can proceed to next page or return success
            self.window.after(1050, self.window.withdraw())
            c.execute("""
                      INSERT INTO users(username,password,email)
                      VALUES(?,?,?)"""
                    ,(self.the_username,self.the_password, self.Email.get())
                      )
            conn.commit()
            from Log_in_page import LoginPage
            self.window.destroy()
            LoginPage(self.window.master)

        else:
            # Show wrong image
            self.check_btn.config(image=self.the_wrong_img)
            # Clear all entries


    def on_focus_in(self, event):

        
        self.the_email.place(x=664,y=157)
        self.eemail.place_forget()
        self.email_bg.config(image=self.email_bg_act)
        if self.time_left==0 or self.time_left==None:
          self.email_verify_button.config(state='normal')
                   

    def on_focus_out(self, event):
        self.e = event.widget
        if self.e.get() == "":
            self.email_bg.config(image=self.email_bg_img)
            self.the_email.place_forget()
            self.eemail.place(x=665,y=168)
            
            self.email_verify_button.config(state='disabled')
            
    
            


    
def page(the_username=None, the_password=None):
    
    
    window = Toplevel()
    OTPPage(window, the_username, the_password)
    window.mainloop()


if __name__ == '__main__':
  page()
