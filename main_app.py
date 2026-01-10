import sqlite3

from tkinter import *
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import date, datetime

from tkcalendar import Calendar
import numpy as np
import sys
import os

# Database setup
conn = sqlite3.connect("the_base.db")
c = conn.cursor()

def get_week_of_month(d):
    return (d.day - 1) // 7 + 1

def log_transaction(trans_id, action):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    c.execute("INSERT INTO logs (trans_id, action, timestamp) VALUES (?, ?, ?)",
              (trans_id, action, timestamp))
    conn.commit()
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ------------------- TRANSACTION PAGE -------------------
class main_app:
    def __init__(self, window, username=None):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Monetra')
        self.username = username
        

        

        
        self.icon = PhotoImage(file=resource_path("images\\app_logo.png"))
        self.window.iconphoto(True, self.icon)
        
        # Background
        self.window.configure(bg="#2d2638")
        
        #categories list
        self.EXPENSE_CATEGORIES = [
                                    "Food",
                                    "Transportation",
                                    "Education",
                                    "Health",
                                    "Entertainment",
                                    "Subscriptions",
                                    "Other"
                                  ]
        
        
        #transaction bg
        imgtrans = Image.open(resource_path("images\\transaction_bg.png"))
        imgtrans = imgtrans.resize((1535, 842), Image.Resampling.LANCZOS)
        self.trans_bg = ImageTk.PhotoImage(imgtrans)
        self.transaction_frame = Frame(self.window, bg="#4e2099", width=1535, height=842)
        self.transaction_frame.place(x=0, y=0)
        self.main_image_label = Label(self.transaction_frame, image=self.trans_bg, bg="#2d2638")
        self.main_image_label.place(x=0, y=0)
        
        #dashboard bg
        imgdash = Image.open(resource_path("images\\dashboard_bg.png"))
        imgdash = imgdash.resize((1535, 842), Image.Resampling.LANCZOS)
        self.dash_bg = ImageTk.PhotoImage(imgdash)
        self.dashboard_frame = Frame(self.window, bg="#4e2099", width=1535, height=842)
        self.main_image_dashboard_label = Label(self.dashboard_frame, image=self.dash_bg, bg="#2d2638")
        self.main_image_dashboard_label.place(x=0, y=0)
        # self.draw_expenses_pie_chart()  
        
        #history bg     
        imghist = Image.open(resource_path("images\\history_bg.png"))
        imghist = imghist.resize((1535, 842), Image.Resampling.LANCZOS)
        self.hist_bg = ImageTk.PhotoImage(imghist)
        self.history_frame = Frame(self.window, bg="#4e2099", width=1535, height=842)    
        self.main_image_history_label = Label(self.history_frame, image=self.hist_bg, bg="#2d2638")
        self.main_image_history_label.place(x=0, y=0)
        
        #main buttons for trnasaction page
        self.dashboard_btn = Label(self.transaction_frame, text="D a s h b o a r d",fg="#292828",bg="#6a5b72", font=('Britannic Bold',25, 'bold'),cursor='hand2')
        self.dashboard_btn.bind("<Button-1>",self.dash_board_place)
        self.dashboard_btn.place(x=643, y=76)
        self.history_btn = Label(self.transaction_frame, text="H i s t o r y",fg="#292828",bg="#6a5b72", font=('Britannic Bold',25, 'bold'),cursor='hand2')
        self.history_btn.bind("<Button-1>",self.history_place)
        self.history_btn.place(x=1135, y=76)
        self.transaction_text = Label(self.transaction_frame, text="T r a n s a c t i o n",fg="#000000",bg="#e4beeb", font=('Britannic Bold',25, 'bold'))
        self.transaction_text.place(x=161, y=76)
        
        #main buttons for dashboard page
        self.dashboard_text = Label(self.dashboard_frame, text="D a s h b o a r d",fg="#000000",bg="#e4beeb", font=('Britannic Bold',25, 'bold'),cursor='hand2')
        self.dashboard_text.place(x=643, y=76)
        self.history_btn = Label(self.dashboard_frame, text="H i s t o r y",fg="#292828",bg="#6a5b72", font=('Britannic Bold',25, 'bold'),cursor='hand2')
        self.history_btn.bind("<Button-1>",self.history_place)
        self.history_btn.place(x=1135, y=76)
        self.transaction_btn = Label(self.dashboard_frame, text="T r a n s a c t i o n",fg="#292828",bg="#6a5b72", font=('Britannic Bold',25, 'bold'))
        self.transaction_btn.bind("<Button-1>",self.transactions_place)
        self.transaction_btn.place(x=161, y=76)      
        
        #main buttons for history page
        self.dashboard_btn = Label(self.history_frame, text="D a s h b o a r d",fg="#292828",bg="#6a5b72", font=('Britannic Bold',25, 'bold'),cursor='hand2')
        self.dashboard_btn.bind("<Button-1>",self.dash_board_place)
        self.dashboard_btn.place(x=643, y=76)
        self.history_text = Label(self.history_frame, text="H i s t o r y",fg="#000000",bg="#e4beeb", font=('Britannic Bold',25, 'bold'),cursor='hand2')
        self.history_text.place(x=1135, y=76)
        self.transaction_btn = Label(self.history_frame, text="T r a n s a c t i o n",fg="#292828",bg="#6a5b72", font=('Britannic Bold',25, 'bold'))
        self.transaction_btn.bind("<Button-1>",self.transactions_place)
        self.transaction_btn.place(x=161, y=76) 
          
        

        
        
        

        
        # Info label
        self.info_icon = Label(self.transaction_frame, bg='#2d2638', text="💰", 
                              fg='#ffffff', font=('poppins', 20, "normal"))
        self.info_icon.place(x=175, y=280)
        
        self.info_text = Label(self.transaction_frame, bg='#2d2638',
                              text="Record your financial transactions below.", 
                              fg='#ffffff', font=('poppins', 16, "normal"))
        self.info_text.place(x=213, y=289)
        
             

        # Transaction Type Section
        self.type_label = Label(self.transaction_frame, text="Transaction Type:", 
                               bg="#2d2638", fg="#ffffff", font=('Bauhaus 93', 15, 'bold'))
        self.type_label.place(x=225, y=340)
        
        self.transaction_type = StringVar()
        self.transaction_type.set("Profit")
        
        # Radio buttons with custom styling
        self.profit_radio = Radiobutton(self.transaction_frame, text="➕ Profit (Addition)", 
                                       variable=self.transaction_type, value="Profit",
                                       bg="#2d2638", fg="#4CAF50", font=('poppins', 12, 'bold'),
                                       activebackground="#2d2638", activeforeground="#4CAF50", 
                                       selectcolor="#4a4054")
        self.profit_radio.place(x=245, y=395)
        
        self.loss_radio = Radiobutton(self.transaction_frame, text="➖ Loss (Subtraction)", 
                                     variable=self.transaction_type, value="Loss",
                                     bg="#2d2638", fg="#FF5252", font=('poppins', 12, 'bold'),
                                     activebackground="#2d2638", activeforeground="#FF5252",
                                     selectcolor="#4a4054")
        self.loss_radio.place(x=245, y=445)
        
        
        # Category Section
        self.category_label = Label(self.transaction_frame, text="Category:", 
                                   bg="#2d2638", fg="#ffffff", font=('Bauhaus 93', 17, 'bold'))
        self.category_label.place(x=220, y=525)
        
        # Styled dropdown
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TCombobox', 
                       fieldbackground='#4a4054',
                       background='#4a4054',
                       foreground='#ffffff',
                       arrowcolor='#ffffff',
                       bordercolor='#6a6074',
                       lightcolor='#4a4054',
                       darkcolor='#4a4054')
        style.map('Custom.TCombobox',
                 fieldbackground=[('readonly', '#4a4054')],
                 foreground=[('readonly', '#ffffff')],
                 selectbackground=[('readonly', '#4a4054')],
                 selectforeground=[('readonly', '#ffffff')])
        
        self.category_dropdown = ttk.Combobox(self.transaction_frame, 
                                             values=[ "Entertainment",
                                                      "Transportation",
                                                      "Education",
                                                      "Health",
                                                      "Food",
                                                      "Subscriptions",
                                                      "Other"
                                                    ]
                                             
                                             ,state="readonly",
                                             font=('poppins', 13),
                                             style='Custom.TCombobox')
        self.category_dropdown.set("Choose a Category")
        self.category_dropdown.place(x=380, y=523, width=260, height=32)
        
        # Amount Section
        self.amount_label = Label(self.transaction_frame, text="Amount ($):", 
                                 bg="#2d2638", fg="#ffffff", font=('Bauhaus 93', 17, 'bold'))
        self.amount_label.place(x=220, y=595)
        
        # Amount entry with validation
        vcmd = (self.window.register(self.validate_number), '%P')
        self.amount_entry = Entry(self.transaction_frame, 
                                 font=("Segoe UI", 14),
                                 bd=2,
                                 relief="solid",
                                 fg="#ffffff",
                                 bg="#4a4054",
                                 insertbackground="#ffffff",
                                 validate='key',
                                 validatecommand=vcmd)
        self.amount_entry.place(x=380, y=598, width=260, height=32)
        submit_btn_image = Image.open(resource_path("images\\submit_btn.png"))
        submit_btn_image = submit_btn_image.resize((250, 110), Image.Resampling.LANCZOS)
        self.submit_btn_img = ImageTk.PhotoImage(submit_btn_image)
        self.submit_btn = Button(self.transaction_frame, image=self.submit_btn_img, borderwidth=0, command=self.submit_transaction,background="#2d2638", activebackground="#2d2638")
        self.submit_btn.place(x=305, y=650)

        # Date display
        today = date.today().strftime("%B %d, %Y")
        self.date_label = Label(self.transaction_frame, text=f" Date: {today}", 
                               bg="#2d2638", fg="#b8b8b8", font=('poppins', 15, 'italic'))
        self.date_label.place(x=1025, y=289)
        self.date_icon = Label(self.transaction_frame, bg='#2d2638', text="📅",fg="#b8b8b8", font=('poppins', 17, 'normal'))
        self.date_icon.place(x=1000, y=285)
        
        
        
        self.total_logs=[]
        #sub tabel information
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        self.the_calender=Calendar(self.history_frame, selectmode='day', year=year, month=month, day=day)
        self.the_calender.place(x=92,y=260)
        self.collect_date_btn=Button(self.history_frame,text="search by day",cursor="hand2",bg="#2d2638",font=("poppines",15,"bold"),command=self.set_table)
        self.collect_date_btn.place(x=142,y=460)
        
        
        #tabel idea 
        previous_arrow_img = Image.open(resource_path("images\\back_btn.png"))
        previous_arrow_img = previous_arrow_img.resize((46, 46), Image.Resampling.LANCZOS)
        previous_arrow_img = ImageTk.PhotoImage(previous_arrow_img)
        self.previous_arrow_btn = Button(self.history_frame, image=previous_arrow_img, borderwidth=0, background="#2d2638", activebackground="#2d2638",relief="flat", cursor="hand2",command=self.back)
        self.previous_arrow_btn.image = previous_arrow_img
        self.previous_arrow_btn.place(x=605, y=231)
        self.previous_arrow_btn.config(state="disabled")
        next_arrow_img = Image.open(resource_path("images\\next_btn.png"))
        next_arrow_img = next_arrow_img.resize((46, 46), Image.Resampling.LANCZOS)
        next_arrow_img = ImageTk.PhotoImage(next_arrow_img)
        self.next_arrow_btn = Button(self.history_frame, image=next_arrow_img, borderwidth=0, background="#2d2638", activebackground="#2d2638",relief="flat", cursor="hand2",command=self.forward)
        self.next_arrow_btn.image = next_arrow_img
        self.next_arrow_btn.place(x=1011, y=231)
        





     
        self.num_widgets=[]
        self.act_widg=[]
        self.start = 0
        
        
        self.the_total=Label(self.history_frame,text=f"{len(self.total_logs)}",bg="#ffffff",fg="#000000",font=('Britannic Bold',20,'bold'))
        self.the_total.place(x=860,y=235)
        self.the_total2=Label(self.history_frame,text=f"",bg="#ffffff",fg="#000000",font=('Franklin Gothic Mediu...',18,'normal'))
        self.the_total2.place(x=739,y=238)
        
        


        
        for i in range(10):
            act_text=Label(self.history_frame, text="",bg="#221c2d",fg="#FD33C4", font=('poppins', 15, 'normal'))
            act_text.place(x=657,y=345+ (i*50))
            self.act_widg.append(act_text)
            act_no=Label(self.history_frame, text="",bg="#221c2d",fg="#F20069", font=('poppins', 15, 'normal'))
            act_no.place(x=557,y=344+ (i*50))
            self.num_widgets.append(act_no)
            
            if i%2!=0:
              act_text.config(bg="#241d2f")
              act_no.config(bg="#241d2f")
        

          
        
    def validate_number(self, value):
        """Only allow numbers and decimal point"""
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def submit_transaction(self):
        """Handle transaction submission to database"""
        amount_text = self.amount_entry.get().strip()
        category = self.category_dropdown.get()
        trans_type = self.transaction_type.get()
        
        # Validation
        if category == "Choose a Category":
            messagebox.showerror("Error", "Please select a category!",parent=self.window)
            return
        if not amount_text:
            messagebox.showerror("Error", "Please enter an amount!",parent=self.window)
            return
        
        try:
            amount = float(amount_text)
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0!",parent=self.window)
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid amount!",parent=self.window)
            return
        
        # Check week and month limits
        today = date.today()
        year = today.year
        month = today.month
        week = get_week_of_month(today)
        
        c.execute("""
            SELECT trans_id, date FROM transactions
            WHERE username = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        """, (self.username, str(year), f"{month:02d}"))
        
        month_entries = c.fetchone()
        
        # Insert transaction
        transaction_date = today.strftime("%Y-%m-%d")
        
        try:
            c.execute("""
                INSERT INTO transactions (username, amount, type, category, date)
                VALUES (?, ?, ?, ?, ?)
            """, (self.username, amount, trans_type, category, transaction_date))
            
            conn.commit()
            trans_id = c.lastrowid
            
            # Log the transaction
            log_transaction(trans_id, 
                          f"Added {trans_type} of {amount} (category '{category}')")
            
            # Update user's balance based on type

            

            
            messagebox.showinfo("Success", 
                               f"Transaction recorded successfully!\n\n"
                               f"Type: {trans_type}\n"
                               f"Category: {category}\n"
                               f"Amount: ₱{amount:.2f}",parent=self.window)
            
            
            # Clear fields
            self.amount_entry.delete(0, END)
            self.category_dropdown.set("Choose a Category")
            self.transaction_type.set("Profit")
            
            
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to save transaction:\n{str(e)}")

    def transactions_place(self, event=None):
      self.history_frame.place_forget()
      self.dashboard_frame.place_forget()
      self.transaction_frame.place(x=0, y=0)
    def dash_board_place(self, event=None):
      self.history_frame.place_forget()
      self.transaction_frame.place_forget()
      self.dashboard_frame.place(x=0, y=0)
      self.draw_expenses_pie_chart()
      self.daily_expenses_data = self.get_daily_expenses(self.username)
      self.draw_daily_expenses_graph(self.daily_expenses_data)
      # Info boxes
      self.draw_expense_rate_box()
      self.draw_max_daily_expense_box()
      self.draw_top_category_box()

      
      
    def history_place(self,event=None):
      self.dashboard_frame.place_forget()
      self.transaction_frame.place_forget()
      self.history_frame.place(x=0, y=0)
      
      
      
    
    def looping_table_show(self):
      
      for i in range(10):
          self.act_widg[i].config(text="")
          self.num_widgets[i].config(text="")

      if not self.total_logs:
          self.the_total2.config(text="")
          self.next_arrow_btn.config(state="disabled")
          return

      end = min(self.start + 10, len(self.total_logs))

      for i in range(end - self.start):
          idx = self.start + i
          self.act_widg[i].config(text=self.total_logs[idx])
          self.num_widgets[i].config(text=str(idx + 1))

      self.the_total2.config(text=f"{self.start + 1}-{end}")

      
      self.previous_arrow_btn.config(
          state="normal" if self.start > 0 else "disabled"
      )
      self.next_arrow_btn.config(
          state="normal" if end < len(self.total_logs) else "disabled"
      )
        
        
          
          
          
              
    def back(self):
        
            
        if self.start - 10 > 0:
            self.start -= 10
            self.looping_table_show()
        else:
          self.start=0
          self.looping_table_show()
          

    def forward(self):
        
        if self.start + 10 < len(self.total_logs):
            self.start += 10
            
            self.looping_table_show()
            
    def get_user_logs(self,username, date_input=None):
      if date_input:
          c.execute("""
              SELECT logs.action
              FROM logs
              JOIN transactions
              ON logs.trans_id = transactions.trans_id
              WHERE transactions.username = ?
              AND DATE(logs.timestamp) = ?
          """, (username, date_input))
      else:
          c.execute("""
              SELECT logs.action
              FROM logs
              JOIN transactions
              ON logs.trans_id = transactions.trans_id
              WHERE transactions.username = ?
          """, (username,))
      
      records = c.fetchall()   # [(action1,), (action2,), ...]
      action_list = [action for (action,) in records]

      return  action_list
        
    def set_table(self):

    
      
      the_day=self.the_calender.get_date()
      
        

      the_day = self.the_calender.get_date()  # e.g., "12/26/25"
      day_obj = datetime.strptime(the_day, "%m/%d/%y")  # note: %y for 2-digit year
      self.formatted_day = day_obj.strftime("%Y-%m-%d")  # now "2025-12-26"
      
      print(self.formatted_day)
      self.total_logs=self.get_user_logs(self.username,self.formatted_day)
      self.start = 0  
      self.previous_arrow_btn.config(state="disabled")
      self.the_total.config(text=f"{len(self.total_logs)}")
      self.looping_table_show()
      
    def get_expenses_by_category(self,username):
        expenses = {cat: 0.0 for cat in self.EXPENSE_CATEGORIES}

        c.execute("""
            SELECT category, SUM(amount)
            FROM transactions
            WHERE username = ?
            AND type = 'Loss'
            GROUP BY category
        """, (username,))

        for category, total in c.fetchall():
            expenses[category] = total

        return expenses
              
        
          
    # ------------- PIE Chart ----------   
    def draw_expenses_pie_chart(self):
        self.expenses_dict = self.get_expenses_by_category(self.username)

        labels, values = [], []

        for category, amount in self.expenses_dict.items():
            if amount > 0:
                labels.append(category)
                values.append(amount)

        if not values:
            Label(
                self.dashboard_frame,
                text="No expenses to display",
                bg="#1E1E2E",
                fg="white",
                font=("Segoe UI", 11)
            ).place(x=1000, y=300)
            return

        colors = [
            "#C77DFF", "#9D4EDD", "#7B2CBF",
            "#5A189A", "#3C096C", "#E0AAFF", "#B5179E"
        ]

        fig, ax = plt.subplots(figsize=(5.5, 5.5))
        fig.patch.set_facecolor("#927fb3")
        ax.set_facecolor("#927fb3")

        ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            startangle=90,
            explode=[0.05] * len(values),
            textprops={"color": "white", "fontsize": 9}
        )

        ax.set_title(
           "Expenses by Category", 
           fontsize=13, 
           fontweight="bold", 
           color="#E0AAFF",
           pad=15, x=0.5)

        ax.axis("equal")
        fig.tight_layout()
        fig.subplots_adjust(bottom=0.25)

        canvas = FigureCanvasTkAgg(fig, master=self.dashboard_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=1020, y=420,height=370,width=400)
        plt.close(fig)
    

    # ---------- Prepare data for Expenses Graph ----------
    def get_daily_expenses(self, username):
        c.execute("""
            SELECT date, SUM(amount)
            FROM transactions
            WHERE username = ?
            AND type = 'Loss'
            GROUP BY date
            ORDER BY date
        """, (username,))

        return c.fetchall()
    

    # ---------- Expenses Graph ----------
    def draw_daily_expenses_graph(self, daily_expenses_data):
        if not daily_expenses_data:
            Label(
                self.dashboard_frame,
                text="No expenses to display",
                bg="#1E1E2E",
                fg="white",
                font=("Segoe UI", 11)
            ).place(x=300, y=450)
            return

        # ---------------- Prepare data ----------------
        dates = [row[0] for row in daily_expenses_data]
        totals = [row[1] for row in daily_expenses_data]

        # ---------------- Figure & Axes ----------------
        fig, ax = plt.subplots(figsize=(7.5, 4.5))

        # Background colors (match dashboard)
        fig.patch.set_facecolor("#5f4a87")
        ax.set_facecolor("#2A2138")

        # ---------------- Line + Fill ----------------
        ax.plot(
            dates,
            totals,
            marker="o",
            linewidth=2.5,
            color="#C77DFF",
            markersize=6
        )

        ax.fill_between(
            dates,
            totals,
            color="#9D4EDD",
            alpha=0.25
        )

        # ---------------- Titles & Labels ----------------
        ax.set_title(
            "Daily Expenses",
            fontsize=14,
            fontweight="bold",
            color="#E0AAFF",
            pad=15
        )

        ax.set_xlabel("Date", color="white", fontweight = "bold", labelpad=10)
        ax.set_ylabel("Amount Spent", color="white", fontweight = "bold", labelpad=10)

        # ---------------- Grid & Ticks ----------------
        ax.grid(
            True,
            linestyle="--",
            linewidth=0.6,
            alpha=0.4,
            color="white"
        )

        ax.tick_params(axis="x", rotation=45, colors="white")
        ax.tick_params(axis="y", colors="white")

        # Remove top & right borders
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#BFA8FF")
        ax.spines["bottom"].set_color("#BFA8FF")

        fig.tight_layout()
        fig.subplots_adjust(bottom=0.25)

        # ---------------- Embed in Tkinter ----------------
        canvas = FigureCanvasTkAgg(fig, master=self.dashboard_frame)
        canvas.draw()

        canvas.get_tk_widget().place(
            x=150,
            y=382,
            width=800,
            height=415
        )

        plt.close(fig)



    def calculate_expense_rate(self, daily_data):
        if len(daily_data) < 2:
            return 0.0

        totals = [row[1] for row in daily_data]
        days = list(range(len(totals)))  # 0,1,2,3,...

        slope, _ = np.polyfit(days, totals, 1)
        return round(slope, 2)


    def calculate_max_daily_expense(self, daily_expenses_data):
        """Maximum expense in a single day."""
        return max((amt for _, amt in daily_expenses_data), default=0.0)

    def calculate_top_category(self):
        """Category with highest total expense."""
        expenses = self.get_expenses_by_category(self.username)
        if not expenses or all(v == 0 for v in expenses.values()):
            return "N/A"
        return max(expenses, key=expenses.get)

    # --- Styling constants ---
    BOX_BG = "#927fb3"
    BOX_VALUE_COLOR = "#FFFFFF"

    def draw_info_box(self, value, pos_x):
        """Reusable box drawer with consistent alignment."""
    
        box_width = 260
        # Value (below title)
        Label(
            self.dashboard_frame,
            text=value,
            bg=self.BOX_BG,
            fg=self.BOX_VALUE_COLOR,
            font=("Segoe UI", 16, "bold")
        ).place(x=pos_x, y=270, width=box_width, height=70)


    def draw_expense_rate_box(self):
        rate = self.calculate_expense_rate(self.daily_expenses_data)
        self.draw_info_box(f"{rate} / Day", 200)

    def draw_max_daily_expense_box(self):
        max_daily = self.calculate_max_daily_expense(self.daily_expenses_data)
        self.draw_info_box(f"{max_daily:.2f}", 645)

    def draw_top_category_box(self):
        top_category = self.calculate_top_category()
        self.draw_info_box(top_category, 1100)
      
    
              
        
          
          

      
      
        
      

        
# ------------------- RUN APP -------------------
def page(username=None):
    window = Toplevel()
    # Replace "testuser" with actual logged-in username
    main_app(window, username=username)
    window.mainloop()


if __name__ == '__main__':
    page()
