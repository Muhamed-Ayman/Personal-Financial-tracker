# Monetra 💰

**Your Lifetime Financial Partner**

Monetra is a desktop financial tracking application built with Python that helps users manage their personal finances through an intuitive GUI interface. Track expenses, visualize spending patterns, and maintain financial records with ease.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite3-orange.svg)

## 📋 Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Application Flow](#application-flow)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Authentication & Security
- **User Registration** - Create new accounts with username and password
- **Email Verification** - OTP-based email verification for account security
- **Secure Login** - Username and password authentication
- **Password Recovery** - Forgot password functionality with email recovery
- **Session Management** - Secure user session handling

### Transaction Management
- **Add Transactions** - Record profit (income) and loss (expenses)
- **Category Organization** - Categorize expenses into predefined categories:
  - Food & Dining
  - Transportation
  - Shopping
  - Entertainment
  - Healthcare
  - Utilities
  - Education
  - Travel
  - Insurance
  - And more...
- **Date Tracking** - Automatic timestamp for all transactions
- **Amount Validation** - Input validation for monetary values
<img width="1718" height="980" alt="transaction" src="https://github.com/user-attachments/assets/d712746c-f1f6-414c-957d-941e3d2c6f3b" />

### Dashboard & Analytics
- **Visual Analytics** - Interactive charts and graphs
  - Pie chart for expense breakdown by category
  - Line graph for daily expense trends
- **Expense Rate** - Calculate daily spending rate
- **Max Daily Expense** - Track highest single-day spending
- **Top Category** - Identify spending patterns
- **Real-time Updates** - Dynamic data visualization
<img width="1718" height="980" alt="dashboard" src="https://github.com/user-attachments/assets/42c34178-367c-4ceb-a02a-c08a3878a265" />

### Transaction History
- **Searchable History** - View transactions by specific date
- **Calendar Integration** - Easy date selection with calendar widget
- **Pagination** - Browse through transaction records (10 per page)
- **Transaction Logs** - Complete audit trail of all activities
<img width="1725" height="983" alt="history" src="https://github.com/user-attachments/assets/3d96f8ff-1abd-4e0c-b082-38c47b4e6847" />

## 🛠️ Technologies

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework
- **SQLite3** - Local database
- **Pillow (PIL)** - Image processing and handling
- **Matplotlib** - Data visualization and charting
- **NumPy** - Numerical computations
- **tkcalendar** - Calendar widget for date selection
- **smtplib** - Email sending functionality
- **SymPy** - Symbolic mathematics

## 📦 Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/monetra.git
cd monetra
```

### Step 2: Install Required Dependencies

```bash
pip install pillow matplotlib numpy tkcalendar sympy
```

Or use the requirements file (if available):

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Email Configuration

Edit `Emails_to_users.py` and configure your Gmail credentials:

```python
sender_email = "your-email@gmail.com"
app_password = "your-app-password"
```

**Note**: Use Gmail App Password, not your regular password. [Learn how to generate an app password](https://support.google.com/accounts/answer/185833).

### Step 4: Create Database

The application will automatically create `the_base.db` on first run. Ensure you have write permissions in the project directory.

## 🚀 Usage

### Running the Application

```bash
python Log_in_page.py
```

### First Time Setup

1. **Sign Up**: Click "Sign up" on the login page
2. **Verify Email**: Enter your email and verify with the OTP code sent
3. **Create Account**: Set your username and password
4. **Login**: Use your credentials to access the application
### 🔄 Application Flow

This flowchart outlines a login system process:

<img width="760" height="857" alt="image" src="https://github.com/user-attachments/assets/1196b103-77cb-47a5-ad80-f5e2fc7d266d" />

### Adding Transactions

1. Navigate to the **Transaction** page
2. Select transaction type (Profit/Loss)
3. Choose a category from the dropdown
4. Enter the amount
5. Click **Submit** to record the transaction

### Viewing Dashboard

1. Click on **Dashboard** tab
2. View expense breakdown pie chart
3. Analyze daily expense trends
4. Check key metrics (expense rate, max daily expense, top category)

### Checking History

1. Go to the **History** tab
2. Select a date from the calendar
3. Click "search by day" to view transactions
4. Use navigation arrows to browse through records

## 📁 Project Structure

```
Monetra/
│
├── Log_in_page.py              # Login interface and authentication
├── sign_up_page.py             # User registration interface
├── otp_page.py                 # OTP verification page
├── forget_password_page.py     # Password recovery interface
├── main_app.py                 # Main application (transactions, dashboard, history)
├── Emails_to_users.py          # Email sending functionality
├── Log_in_page.spec            # PyInstaller specification file
│
├── images/                     # Application images and icons
│   ├── app_logo.png
│   ├── bg_panel.png
│   └── ... (other UI assets)
│
├── build/                      # Build files (generated)
├── __pycache__/               # Python cache files
│
├── the_base.db                # SQLite database (auto-generated)
└── README.md                  # This file
```


## 🗄️ Database Schema
View the database design in this presentation:  
[Database Presentation](https://www.canva.com/design/DAG9EV9C9aI/FdXoCRqGLqvD2R_qhHxLog/edit?utm_content=DAG9EV9C9aI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

The application uses SQLite with the following main tables:

### Users Table
```sql
- username (PRIMARY KEY)
- password
- email
```

### Transactions Table
```sql
- trans_id (PRIMARY KEY)
- username (FOREIGN KEY)
- transaction_type (Profit/Loss)
- category
- amount
- date
```

### Logs Table
```sql
- log_id (PRIMARY KEY)
- trans_id (FOREIGN KEY)
- action
- timestamp
```
![schema](https://github.com/user-attachments/assets/c53ad4a3-5aeb-4ee2-b252-a95c4098a14e)

## 🔒 Security

- **Password Storage**: Implement password hashing (consider using bcrypt or hashlib)
- **Email Security**: Uses Gmail App Passwords instead of regular passwords
- **Input Validation**: All user inputs are validated before processing
- **Session Management**: Secure user session handling
- **OTP Verification**: Email-based verification for new accounts

**⚠️ Security Notice**: The current implementation stores passwords in plain text. For production use, implement proper password hashing using libraries like `bcrypt` or `argon2`.

## 🎨 Building Executable

The project includes a PyInstaller spec file for creating a standalone executable:

```bash
pyinstaller Log_in_page.spec
```

The executable will be generated in the `dist/` folder.

## 📝 Notes

- Ensure stable internet connection for email OTP functionality
- OTP codes expire after 60 seconds
- Transaction limits can be configured in the code
- The application stores all data locally in `the_base.db`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

You can reach us via the following emails:

| Name                                      | Email                                                |
|------------------------------------------|------------------------------------------------------|
| Ahmed Hossam Saeed Mohamed                | [ahmed.gabr.me@gmail.com](mailto:ahmed.gabr.me@gmail.com) |
| Mohamed Ayman Abd-elhakim Ibrahim         | [mohammed.a.ibrahim@gmail.com](mailto:mohammed.a.ibrahim@gmail.com) |
| Ibrahim Mohamed Mousa Mohamed Hussein     | [ibrahimmohamed22008@gmail.com](mailto:ibrahimmohamed22008@gmail.com) |

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Icons and images from various sources and some of them is self-made
- Inspired by personal finance management needs

---

**Monetra** - *Start your journey with security & privacy as our top priorities* 🚀
