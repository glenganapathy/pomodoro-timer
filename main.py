import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer= None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER⏱️",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    sb_sec=SHORT_BREAK_MIN*60
    lb_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(lb_sec)
        timer_label.config(text="Long Break",fg=RED)
    elif reps%2==0:
        count_down(sb_sec)
        timer_label.config(text="Short Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    cmin =count//60
    csec =count%60
    if csec<10:
        csec= f"0{csec}"
    canvas.itemconfig(timer_text,text=f"{cmin}:{csec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        tick=""
        for _ in range(reps//2):
            tick+="✓"
        check_label.config(text=tick)
# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro🍅")
window.config(padx=100,pady=50)
window.config(bg=YELLOW)

canvas=tkinter.Canvas(height=224,width=200,highlightthickness=0)


tomato=tkinter.PhotoImage(file="tomato.png")

canvas.create_image(100,112, image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="White",font=(FONT_NAME ,30, "bold"))
canvas.config(background=YELLOW)
canvas.grid(row=1,column=1)

timer_label= tkinter.Label(text="TIMER⏱️",font=(FONT_NAME,30,"bold"),background=YELLOW,foreground=GREEN)
timer_label.grid(row=0,column=1)



start_button=tkinter.Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button=tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

check_label=tkinter.Label(text="",background=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))
check_label.grid(row=3,column=1)

window.mainloop()
