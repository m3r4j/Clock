from tkinter import *
import datetime
import threading
import time


# Create our screen 
root = Tk()

# Title
root.title('Clock')

# Size (Window Size)
root.geometry('800x150') # Width and height

# Background color
root.configure(bg='black')

# Set the icon to a clock
root.iconbitmap('clockicon.ico')

# Make it unresizable
root.resizable(0,0)

# Displays the clock onto the screen and updates every second
def display_clock():
	time_label = None

	while True:
		# Get rid of the time_label for the time updates
		if time_label != None:
			time_label.pack_forget()

		# Get the time
		now = datetime.datetime.now()
		hour = now.hour
		minute = now.minute
		second = now.second
		M = None

		# Check if it's PM or AM
		if hour > 11:
			M = 'PM'
		else:
			M = 'AM'

		# If it finds that it is 24-hour format then change it to 12-hour format
		if hour > 12:
			hour = hour - 12

		if len(str(hour)) == 1:
			hour = '0' + str(hour)

		if len(str(minute)) == 1:
			minute = '0' + str(minute)

		if len(str(second)) == 1:
			second = '0' + str(second)

		full = f'{hour}:{minute}:{second}:{M}'

		# Add it onto the screen with a big font and the text should be lime
		time_label = Label(root, text=full, font=(None, 100), fg='lime', bg='black')
		time_label.pack()

		# Wait 1 second then refresh and continue this loop
		time.sleep(1)



def display_thread():
	t = threading.Thread(target=display_clock)
	t.setDaemon(True)
	t.start()

display_thread()




# Run the mainloop
root.mainloop()