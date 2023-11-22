 import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hotel Booking App")

# User interface frames
search_frame = tk.Frame(master=window)
results_frame = tk.Frame(master=window)
booking_frame = tk.Frame(master=window)

# Search frame UI
search_label = tk.Label(master=search_frame, text="Search")
location_entry = tk.Entry(master=search_frame)
checkin_label = tk.Label(master=search_frame, text="Check-in Date")
checkin_entry = tk.Entry(master=search_frame)
checkout_label = tk.Label(master=search_frame, text="Check-out Date")
checkout_entry = tk.Entry(master=search_frame)
search_button = tk.Button(master=search_frame, text="Search")

# Pack the search frame UI
search_label.pack()
location_entry.pack()
checkin_label.pack() 
checkin_entry.pack()
checkout_label.pack()
checkout_entry.pack()
search_button.pack()

# Additional frames and UI
...

# Main loop
window.mainloop()
