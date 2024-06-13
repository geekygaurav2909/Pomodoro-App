from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_running = False
# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    canvas.itemconfig(timer_id, text="00:00")
    timer_label.config(text= "Timer")
    comp_label.config(text= "")
    global reps, timer_running
    reps = 0
    timer_running = False

    window.after_cancel(job_id)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps%8 == 0:
            count_down(long_break_sec)
            timer_label.config(text= "Long Break", fg= RED)  
        elif reps%2 == 0:
            count_down(short_break_sec)
            timer_label.config(text= "Short Break", fg= PINK)  
        else:
            count_down(work_sec)
            timer_label.config(text= "Work", fg= GREEN)  


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global job_id
    minute = count // 60
    second = count % 60
    canvas.itemconfig(timer_id, text = "{:02d}:{:02d}".format(minute,second))
    if count > 0:
        job_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        comp_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = canvas_img)
timer_id = canvas.create_text(100,130, text="00:00", font = (FONT_NAME, 25, "bold"), fill = "white")
canvas.grid(row= 1, column=1)

# adding label = Timer

timer_label = Label(text="Timer", font= (FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)


# adding button = Start

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# adding button = Reset

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(row=2, column=2)

# Adding completion tick as label

comp_label = Label(font= (FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW, justify="left")
comp_label.grid(row=3, column=1)



window.mainloop()