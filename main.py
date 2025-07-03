import customtkinter as Tk
import math

#define colors
black = "#000"
white = "#fff"
red = "#b51010"
blue = "#149bb3"
light_black="#373838"
button_font = ("Roboto", 20)

#create calculator window
app = Tk.CTk()
app.resizable(False, False)
app.geometry("400x550")
app.title("Calculator")
app.config(background="#202120")

#create display frame for display
display_frame = Tk.CTkFrame(app, width=380, height=120, fg_color=black)
display_frame.place(x=10, y=10)
#creaate button frame for calculator buttons
button_container = Tk.CTkFrame(app, width=380, height=446, fg_color=black)
button_container.grid(columnspan=4, padx=10, pady=140)

#create equation show display
equation_display = Tk.CTkEntry(display_frame, font=("Consolas", 20), justify="right", width=370, height=20, border_width=0, corner_radius=0, fg_color=black)
equation_display.place(x=5, y=20)
#create main mathematical terms display
main_display = Tk.CTkEntry(display_frame, justify="right", text_color=blue, placeholder_text="0", placeholder_text_color=blue, font=("Consolas", 44), width=370, height=44, border_width=0, corner_radius=0, fg_color=black)
main_display.place(x=5, y=60)

# display clear function
def clear_display():
    equation_display.delete(0, Tk.END)
    main_display.delete(0, Tk.END)

#clear those displays and show error message on main display
def error_message(msg):
    clear_display()
    main_display.insert(Tk.END, msg)

#when calculator button pressed then the button value added on main display
def cliked_btn(value):
    current_equation = main_display.get()
    equation = current_equation + value
    main_display.delete(0, Tk.END)
    main_display.insert(Tk.END, equation)

#show result function recieve eqution and result that shows on thos display
def show_result(equation, result):
    clear_display()
    equation_display.insert(Tk.END, f"{equation}=")
    main_display.insert(Tk.END, round(result, 9))

#solve the trigonometry related calculation like sin cos tan
def handle_trigonometry(degree, func, calc):
    radians = math.radians(degree)
    if calc != "tan":
        result = round(func(radians), 9)
        show_result(degree, result)
    elif calc == "tan" and degree == 90:
        error_message("math error")
    else:
        result = round(func(radians), 9)
        show_result(degree, result)

#when pressed the "=" button then this function is triggered for advance mathematical calculation
def handle_calculation():
    equation = main_display.get()

    #if display has no value the stop working from here
    if(not equation):
        return
    
    #block for square root calculations
    elif("\u221a" in equation):
        try:
            square_root(equation)
        except :
            error_message("math error")
        return
    
    #block for power calculation
    elif("^" in equation):
        try:
            power_calc(equation)

        except Exception as e:
            error_message("syntax error")
        return
        
    #block for handle trigonometry calculation
    elif(equation.startswith(("sin", "cos", "tan"))):
        try:
            value = main_display.get()
            if("tan" in value):
                degree = float(value.split("tan")[1])
                handle_trigonometry(degree, math.tan, "tan")

            elif("cos" in value):
                degree = float(value.split("cos")[1])
                handle_trigonometry(degree, math.cos, "")

            else:
                degree = float(value.split("sin")[1])
                print(degree)
                handle_trigonometry(degree, math.sin, "")
                
        except Exception as e:
            print(e)
            error_message("math error")
        return
    
    try:
        result = eval(equation)
        show_result(equation, result)
    except Exception as e:
        error_message("syntax error")

#this function is for to delete on by one number or operator from main display
def handle_delete():
    equation = main_display.get()

    if(equation == ""):
        clear_display()
    
    else:
        split = [e for e in equation]
        new_equation = "".join(split)[0: len(split)-1]
        main_display.delete(0, Tk.END)
        main_display.insert(Tk.END, new_equation)

#generate pi value when clicked pi button
def value_of_PI():
    result = round(math.pi, 9)
    main_display.insert(Tk.END, result)

#calculate the x to the power y equation
def power_calc(e):
    split = e.split("^")
    number1 = float(split[0])
    number2 = float(split[1])

    result = round(math.pow(number1, number2))
    show_result(e, result)

#complex square root
def square_root(value):
    split = value.split("\u221a")
    if(split[0] != ""):
        negative_number = float(split[0])
        positive = float(split[1])
        result = negative_number * math.sqrt(positive)
        show_result(f"{value}", result)

    elif(split[0] == ""):
        number = float(split[1])
        result = round(math.sqrt(number), 9)
        show_result(value, result)

    else:
        number1 = float(split[0])
        result = float(split[1]) * round(math.sqrt(number1), 9)
        show_result(value, result)

    
#simple square function using math pow
def square():
    n = main_display.get()
    if not n:
        return
    try:
        number = float(n)
        result = round(math.pow(number, 2), 9)
        show_result(f"{number}\u00B2", result)

    except:
        error_message("syntax error")

#calculate and show the factorial n value on main display
def factorial_calc():
    value = main_display.get()
    if not value:
        return

    try:
        number = int(value)
        if not number:
            return

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
                
        for n in range(0, number+1):
            result = factorial(n)
            
        show_result(f"{number}!", result)

    except:
        error_message("math error")

keymap = [
    "sin ", "cos ", "tan ", "DEL", "AC",

    "x\u00B2", "(", ")", "%", "/",

    "x!", "7", "8", "9", "*",

    "\u221a", "4", "5", "6", "-",

    "^", "1", "2", "3", "+",

    "\u03C0", "0", ".", "=",
]

#create calculator buttons on GUI and handle operations
row = 0
col = 0

button_width = 60
button_height = 50

for key in keymap:
    #create buttons based on keymap condition
    if(key == "="):
        Tk.CTkButton(button_container, text=key, command=lambda: handle_calculation(), width=130, height=button_height, font=("Roboto", 24), fg_color=blue, text_color=black, corner_radius=10, border_width=1, border_color=light_black).grid(row=row, column=col, columnspan=2, padx=8, pady=8)
    elif(key == "AC"):
        Tk.CTkButton(button_container, text=key, command=lambda: clear_display(), width=button_width, height=button_height, font=button_font, fg_color=red, text_color=black, corner_radius=10).grid(row=row, column=col, padx=8, pady=8)
    elif(key == "DEL"):
        Tk.CTkButton(button_container, text=key, command=lambda: handle_delete(), width=button_width, height=button_height, font=button_font, fg_color=red, text_color=black, corner_radius=10).grid(row=row, column=col, padx=8, pady=8)
    elif(key == "\u03C0"):
        Tk.CTkButton(button_container, text=key, text_color=blue, command=lambda: value_of_PI(), width=button_width, height=button_height, font=button_font, fg_color=black, corner_radius=10, border_width=1, border_color=light_black).grid(row=row, column=col, padx=8, pady=8)
    elif(key == "x\u00B2"):
        Tk.CTkButton(button_container, text=key, text_color=blue, command=lambda: square(), width=button_width, height=button_height, font=button_font, fg_color=black, corner_radius=10, border_width=1, border_color=light_black).grid(row=row, column=col, padx=8, pady=8)
    elif(key == "x!"):
        Tk.CTkButton(button_container, text=key, text_color=blue, command=lambda: factorial_calc(), width=button_width, height=button_height, font=button_font, fg_color=black, corner_radius=10, border_width=1, border_color=light_black).grid(row=row, column=col, padx=8, pady=8)
    else:
        Tk.CTkButton(button_container, text=key, text_color=blue, command=lambda value = key: cliked_btn(value), width=button_width, height=button_height, font=button_font, fg_color=black, corner_radius=10, border_width=1, border_color=light_black).grid(row=row, column=col, padx=8, pady=8)

    col += 1
    if col == 5:
        col = 0
        row += 1

#run the main GUI loop function
app.mainloop()