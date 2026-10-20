import re
import tkinter as tk
from tkinter import ttk
from database import Database

EMAIL_PATTERN = r"^[\w.-]+@university\.com$"
PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

# ---------- Colours and fonts ----------
PRIMARY = "#2563EB"
PRIMARY_DARK = "#1D4ED8"
HEADER = "#1E293B"
BACKGROUND = "#F1F5F9"
CARD = "#FFFFFF"
TEXT = "#0F172A"
MUTED = "#64748B"
BORDER = "#CBD5E1"
DANGER = "#DC2626"
DANGER_DARK = "#B91C1C"
SUCCESS = "#16A34A"
GREY_BUTTON = "#475569"
GREY_DARK = "#334155"

FONT = "Segoe UI"

GRADE_COLOURS = {"HD": "#7C3AED", "D": "#2563EB", "C": "#0891B2", "P": "#16A34A", "Z": "#DC2626"}


def average_grade(average):
    if average < 50:
        return "Z"
    elif average < 65:
        return "P"
    elif average < 75:
        return "C"
    elif average < 85:
        return "D"
    else:
        return "HD"


def make_button(parent, text, command, colour=PRIMARY, hover=PRIMARY_DARK):
    # flat modern button that changes colour when the mouse is over it
    button = tk.Button(parent, text=text, command=command, bg=colour, fg="white",
                       activebackground=hover, activeforeground="white",
                       font=(FONT, 10, "bold"), relief="flat", bd=0,
                       cursor="hand2", padx=10, pady=8)
    button.bind("<Enter>", lambda e: button.config(bg=hover))
    button.bind("<Leave>", lambda e: button.config(bg=colour))
    return button


def make_header(parent, title, subtitle, colour=HEADER):
    header = tk.Frame(parent, bg=colour)
    header.pack(fill="x")
    tk.Label(header, text=title, bg=colour, fg="white", font=(FONT, 16, "bold")).pack(anchor="w", padx=20, pady=(15, 0))
    tk.Label(header, text=subtitle, bg=colour, fg="#CBD5E1", font=(FONT, 10)).pack(anchor="w", padx=20, pady=(0, 15))
    return header


def center(window, width, height):
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))


# ---------- Window 4: Exception window ----------
class ExceptionWindow:
    def __init__(self, parent, message):
        self.window = tk.Toplevel(parent)
        self.window.title("Exception")
        self.window.configure(bg=CARD)
        self.window.resizable(False, False)
        center(self.window, 360, 190)

        top = tk.Frame(self.window, bg=DANGER)
        top.pack(fill="x")
        tk.Label(top, text="Error", bg=DANGER, fg="white", font=(FONT, 13, "bold")).pack(anchor="w", padx=20, pady=12)

        tk.Label(self.window, text=message, bg=CARD, fg=TEXT, font=(FONT, 10),
                 wraplength=310, justify="left").pack(anchor="w", padx=20, pady=18)

        make_button(self.window, "OK", self.window.destroy, DANGER, DANGER_DARK).pack(anchor="e", padx=20, ipadx=15)

        # Enter or Escape also closes the window
        self.window.bind("<Return>", lambda e: self.window.destroy())
        self.window.bind("<Escape>", lambda e: self.window.destroy())

        # keep this window on top until the user clicks OK
        self.window.transient(parent)
        self.window.grab_set()
        self.window.focus_set()


# ---------- Window 3: Subject window ----------
class SubjectWindow:
    def __init__(self, parent, student):
        self.student = student
        self.window = tk.Toplevel(parent)
        self.window.title("Subjects")
        self.window.configure(bg=BACKGROUND)
        self.window.resizable(False, False)
        center(self.window, 480, 560)

        make_header(self.window, "Enrolled Subjects", student.name + "  |  ID " + student.id)

        # table card
        card = tk.Frame(self.window, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", padx=20, pady=(20, 10))

        columns = ("subject", "mark", "grade")
        self.table = ttk.Treeview(card, columns=columns, show="headings", height=4, style="Modern.Treeview")
        self.table.heading("subject", text="Subject ID")
        self.table.heading("mark", text="Mark")
        self.table.heading("grade", text="Grade")
        self.table.column("subject", width=180, anchor="center")
        self.table.column("mark", width=110, anchor="center")
        self.table.column("grade", width=110, anchor="center")
        for grade in GRADE_COLOURS:
            self.table.tag_configure(grade, foreground=GRADE_COLOURS[grade])
        self.table.pack(fill="x", padx=10, pady=10)

        self.empty_label = tk.Label(card, text="< Nothing to Display >", bg=CARD, fg=MUTED, font=(FONT, 10, "italic"))

        # summary card: average + overall result
        summary = tk.Frame(self.window, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        summary.pack(fill="x", padx=20, pady=10)
        self.average_label = tk.Label(summary, text="", bg=CARD, fg=TEXT, font=(FONT, 11, "bold"))
        self.average_label.pack(side="left", padx=15, pady=12)
        self.result_label = tk.Label(summary, text="", fg="white", font=(FONT, 10, "bold"), padx=12, pady=3)
        self.result_label.pack(side="right", padx=15, pady=12)

        # grading system key
        key = tk.Frame(self.window, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        key.pack(fill="x", padx=20, pady=10)
        tk.Label(key, text="Grading System", bg=CARD, fg=TEXT, font=(FONT, 10, "bold")).pack(anchor="w", padx=15, pady=(10, 4))
        grades = [("HD", "High Distinction", "85-100"), ("D", "Distinction", "75-84"),
                  ("C", "Credit", "65-74"), ("P", "Pass", "50-64"), ("Z", "Fail", "below 50")]
        for code, name, marks in grades:
            row = tk.Frame(key, bg=CARD)
            row.pack(fill="x", padx=15)
            tk.Label(row, text=code, width=4, bg=GRADE_COLOURS[code], fg="white", font=(FONT, 9, "bold")).pack(side="left", pady=2)
            tk.Label(row, text="  " + name + " (" + marks + ")", bg=CARD, fg=MUTED, font=(FONT, 9)).pack(side="left")
        tk.Frame(key, bg=CARD, height=8).pack()

        make_button(self.window, "Close", self.window.destroy, GREY_BUTTON, GREY_DARK).pack(anchor="e", padx=20, pady=10, ipadx=15)

        self.refresh()

    def refresh(self):
        for row in self.table.get_children():
            self.table.delete(row)

        if len(self.student.subjects) == 0:
            self.empty_label.pack(pady=(0, 10))
        else:
            self.empty_label.pack_forget()

        for s in self.student.subjects:
            self.table.insert("", tk.END, values=(s.id, s.mark, s.grade), tags=(s.grade,))

        average = self.student.get_average()
        self.average_label.config(text="Average mark: " + "{:.2f}".format(average) + "   (" + average_grade(average) + ")")
        if average >= 50:
            self.result_label.config(text="PASS", bg=SUCCESS)
        else:
            self.result_label.config(text="FAIL", bg=DANGER)


# ---------- Window 2: Enrolment window ----------
class EnrolmentWindow:
    def __init__(self, parent, student, students, db):
        self.parent = parent
        self.student = student
        self.students = students
        self.db = db
        self.subject_window = None

        self.window = tk.Toplevel(parent)
        self.window.title("Enrolment")
        self.window.configure(bg=BACKGROUND)
        self.window.resizable(False, False)
        center(self.window, 420, 420)

        make_header(self.window, "Welcome, " + student.name, "Student ID " + student.id + "  |  " + student.email)

        card = tk.Frame(self.window, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(card, text="Subject Enrolment", bg=CARD, fg=TEXT, font=(FONT, 12, "bold")).pack(anchor="w", padx=20, pady=(15, 5))

        # progress bar: how many of the 4 subjects are used
        self.progress = ttk.Progressbar(card, maximum=4, length=340, style="Modern.Horizontal.TProgressbar")
        self.progress.pack(padx=20, pady=(5, 2))
        self.count_label = tk.Label(card, text="", bg=CARD, fg=MUTED, font=(FONT, 9))
        self.count_label.pack(anchor="w", padx=20)

        self.status_label = tk.Label(card, text="", bg=CARD, fg=SUCCESS, font=(FONT, 10, "bold"))
        self.status_label.pack(anchor="w", padx=20, pady=(8, 5))

        make_button(card, "+  Enrol Subject", self.enrol).pack(fill="x", padx=20, pady=4)
        make_button(card, "Show Subjects", self.show_subjects, GREY_BUTTON, GREY_DARK).pack(fill="x", padx=20, pady=4)
        make_button(card, "Logout", self.logout, DANGER, DANGER_DARK).pack(fill="x", padx=20, pady=(4, 15))

        # clicking the X button works like Logout
        self.window.protocol("WM_DELETE_WINDOW", self.logout)
        self.update_count()

    def update_count(self):
        total = len(self.student.subjects)
        self.progress["value"] = total
        self.count_label.config(text="You are enrolled in " + str(total) + " out of 4 subjects")

    def enrol(self):
        if len(self.student.subjects) >= 4:
            ExceptionWindow(self.window, "Students are allowed to enrol in 4 subjects only")
            return
        self.student.enroll()
        self.db.save(self.students)
        self.update_count()
        new_subject = self.student.subjects[-1]
        self.status_label.config(text="Enrolled in Subject-" + new_subject.id)

        # if the subject window is open, update it
        if self.subject_window is not None and self.subject_window.window.winfo_exists():
            self.subject_window.refresh()

    def show_subjects(self):
        if self.subject_window is not None and self.subject_window.window.winfo_exists():
            self.subject_window.refresh()
            self.subject_window.window.lift()
        else:
            self.subject_window = SubjectWindow(self.window, self.student)

    def logout(self):
        self.window.destroy()
        self.parent.deiconify()   # show the login window again


# ---------- Window 1: Login window (main window) ----------
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.db = Database()

        self.root.title("GUIUniApp")
        self.root.configure(bg=BACKGROUND)
        self.root.resizable(False, False)
        center(self.root, 400, 460)
        self.set_styles()

        make_header(root, "GUIUniApp", "University Student Portal")

        card = tk.Frame(root, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=25, pady=25)

        tk.Label(card, text="Sign in", bg=CARD, fg=TEXT, font=(FONT, 14, "bold")).pack(anchor="w", padx=25, pady=(20, 0))
        tk.Label(card, text="Use your university email", bg=CARD, fg=MUTED, font=(FONT, 9)).pack(anchor="w", padx=25, pady=(0, 15))

        tk.Label(card, text="Email", bg=CARD, fg=TEXT, font=(FONT, 10)).pack(anchor="w", padx=25)
        self.email_entry = self.make_entry(card)

        tk.Label(card, text="Password", bg=CARD, fg=TEXT, font=(FONT, 10)).pack(anchor="w", padx=25, pady=(10, 0))
        self.password_entry = self.make_entry(card, show="*")

        self.show_var = tk.BooleanVar()
        tk.Checkbutton(card, text="Show password", variable=self.show_var, command=self.toggle_password,
                       bg=CARD, fg=MUTED, activebackground=CARD, font=(FONT, 9), bd=0).pack(anchor="w", padx=22, pady=(4, 0))

        make_button(card, "Login", self.login).pack(fill="x", padx=25, pady=(15, 20))

        # pressing Enter also logs in
        self.root.bind("<Return>", lambda e: self.login())
        self.email_entry.focus_set()

    def set_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Modern.Treeview", font=(FONT, 10), rowheight=28, background=CARD,
                        fieldbackground=CARD, bordercolor=CARD, borderwidth=0)
        style.configure("Modern.Treeview.Heading", font=(FONT, 10, "bold"), background=BACKGROUND,
                        foreground=TEXT, relief="flat")
        style.map("Modern.Treeview", background=[("selected", "#DBEAFE")], foreground=[("selected", TEXT)])
        style.configure("Modern.Horizontal.TProgressbar", troughcolor="#E2E8F0", background=PRIMARY,
                        bordercolor="#E2E8F0", lightcolor=PRIMARY, darkcolor=PRIMARY, thickness=10)

    def make_entry(self, parent, show=""):
        entry = tk.Entry(parent, font=(FONT, 11), bg="#F8FAFC", fg=TEXT, relief="flat", show=show,
                         highlightthickness=1, highlightbackground=BORDER, highlightcolor=PRIMARY)
        entry.pack(fill="x", padx=25, ipady=6)
        return entry

    def toggle_password(self):
        if self.show_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        # 1. empty fields
        if email == "" or password == "":
            ExceptionWindow(self.root, "Email and password cannot be empty")
            return

        # 2. wrong format
        if re.match(EMAIL_PATTERN, email) is None or re.match(PASSWORD_PATTERN, password) is None:
            ExceptionWindow(self.root, "Incorrect email or password format")
            return

        # 3. check the student in students.data
        students = self.db.load()
        student = None
        for s in students:
            if s.email == email and s.password == password:
                student = s

        if student is None:
            ExceptionWindow(self.root, "Student does not exist")
            return

        # 4. login OK -> open the enrolment window
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.root.withdraw()   # hide the login window
        EnrolmentWindow(self.root, student, students, self.db)


root = tk.Tk()
LoginWindow(root)
root.mainloop()
