import tkinter as tk
from datetime import datetime
import time

class YearEndCountdown:
    def __init__(self, root):
        self.root = root
        self.root.title("Year End Countdown")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg="#2c3e50")
        
        # Header
        self.header = tk.Label(
            root, 
            text="TIME REMAINING UNTIL NEW YEAR", 
            font=("Helvetica", 18, "bold"), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        self.header.pack(pady=(20, 10))
        
        # Current time label
        self.current_time_label = tk.Label(
            root, 
            text="", 
            font=("Helvetica", 12), 
            fg="#bdc3c7", 
            bg="#2c3e50"
        )
        self.current_time_label.pack()
        
        # Countdown frame
        self.countdown_frame = tk.Frame(root, bg="#2c3e50")
        self.countdown_frame.pack(pady=20)
        
        # Days
        self.days_label = tk.Label(
            self.countdown_frame, 
            text="00", 
            font=("Helvetica", 36, "bold"), 
            fg="#e74c3c", 
            bg="#2c3e50"
        )
        self.days_label.grid(row=0, column=0, padx=10)
        self.days_text = tk.Label(
            self.countdown_frame, 
            text="DAYS", 
            font=("Helvetica", 12), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        self.days_text.grid(row=1, column=0)
        
        # Hours
        self.hours_label = tk.Label(
            self.countdown_frame, 
            text="00", 
            font=("Helvetica", 36, "bold"), 
            fg="#e74c3c", 
            bg="#2c3e50"
        )
        self.hours_label.grid(row=0, column=1, padx=10)
        self.hours_text = tk.Label(
            self.countdown_frame, 
            text="HOURS", 
            font=("Helvetica", 12), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        self.hours_text.grid(row=1, column=1)
        
        # Minutes
        self.minutes_label = tk.Label(
            self.countdown_frame, 
            text="00", 
            font=("Helvetica", 36, "bold"), 
            fg="#e74c3c", 
            bg="#2c3e50"
        )
        self.minutes_label.grid(row=0, column=2, padx=10)
        self.minutes_text = tk.Label(
            self.countdown_frame, 
            text="MINUTES", 
            font=("Helvetica", 12), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        self.minutes_text.grid(row=1, column=2)
        
        # Seconds
        self.seconds_label = tk.Label(
            self.countdown_frame, 
            text="00", 
            font=("Helvetica", 36, "bold"), 
            fg="#e74c3c", 
            bg="#2c3e50"
        )
        self.seconds_label.grid(row=0, column=3, padx=10)
        self.seconds_text = tk.Label(
            self.countdown_frame, 
            text="SECONDS", 
            font=("Helvetica", 12), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        self.seconds_text.grid(row=1, column=3)
        
        # Progress bar frame
        self.progress_frame = tk.Frame(root, bg="#2c3e50")
        self.progress_frame.pack(pady=(20, 0))
        
        self.progress_label = tk.Label(
            self.progress_frame, 
            text="Year Progress:", 
            font=("Helvetica", 10), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        self.progress_label.grid(row=0, column=0)
        
        self.progress = tk.Label(
            self.progress_frame, 
            text="0%", 
            font=("Helvetica", 10, "bold"), 
            fg="#2ecc71", 
            bg="#2c3e50"
        )
        self.progress.grid(row=0, column=1, padx=5)
        
        # Update the countdown immediately and then every second
        self.update_countdown()
        
    def update_countdown(self):
        now = datetime.now()
        current_year = now.year
        
        # Set the end of the year (December 31st at 23:59:59)
        end_of_year = datetime(current_year, 12, 31, 23, 59, 59)
        
        # Calculate time difference
        time_left = end_of_year - now
        
        # Extract days, hours, minutes, seconds
        days = time_left.days
        seconds = time_left.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Update labels
        self.current_time_label.config(text=f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        self.days_label.config(text=f"{days:02d}")
        self.hours_label.config(text=f"{hours:02d}")
        self.minutes_label.config(text=f"{minutes:02d}")
        self.seconds_label.config(text=f"{seconds:02d}")
        
        # Calculate year progress percentage
        year_start = datetime(current_year, 1, 1)
        year_end = datetime(current_year + 1, 1, 1)
        total_seconds_in_year = (year_end - year_start).total_seconds()
        elapsed_seconds = (now - year_start).total_seconds()
        progress_percent = (elapsed_seconds / total_seconds_in_year) * 100
        
        self.progress.config(text=f"{progress_percent:.2f}%")
        
        # Schedule the next update in 1 second
        self.root.after(1000, self.update_countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = YearEndCountdown(root)
    root.mainloop()