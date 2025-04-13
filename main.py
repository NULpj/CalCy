import math

colors = [
    "\033[38;2;128;223;255m",  
    "\033[38;2;96;191;255m",
    "\033[38;2;64;159;255m",
    "\033[38;2;32;127;223m",
    "\033[38;2;16;95;191m",
    "\033[38;2;8;63;159m",
    "\033[38;2;4;31;127m",
    "\033[38;2;2;15;95m",
    "\033[38;2;1;7;63m",
    "\033[38;2;0;0;42m",
    "\033[38;2;0;0;42m",    
]

logo_lines = [
    "   █████████            ████    █████████            ",
    "  ███▒▒▒▒▒███          ▒▒███   ███▒▒▒▒▒███           ",
    " ███     ▒▒▒   ██████   ▒███  ███     ▒▒▒  █████ ████",
    "▒███          ▒▒▒▒▒███  ▒███ ▒███         ▒▒███ ▒███ ",
    "▒███           ███████  ▒███ ▒███          ▒███ ▒███ ",
    "▒▒███     ███ ███▒▒███  ▒███ ▒▒███     ███ ▒███ ▒███ ",
    " ▒▒█████████ ▒▒████████ █████ ▒▒█████████  ▒▒███████ ",
    "  ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒███ ",
    "                                            ███ ▒███ ",
    "                                           ▒▒██████  ",
    "                                            ▒▒▒▒▒▒   "
]

for i, line in enumerate(logo_lines):
    color = colors[i % len(colors)]
    print(f"{color}{line}\033[0m")

print("\033[1mScientific Calculator - Python Edition\033[0m")
print("Supported functions: +, -, *, /, ^, sqrt(x), sin(x), cos(x), tan(x), log(x), exp(x), pi, e")
print("Type 'exit' to quit.\n")

def calc(expr):
    try:
        expr = expr.replace('^', '**')
        for fn in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
            expr = expr.replace(fn, f'math.{fn}')
        expr = expr.replace('pi', 'math.pi').replace('e', 'math.e')
        result = eval(expr)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

while True:
    user_input = input(">>> ")
    if user_input.lower() == 'exit':
        print("Bye!")
        break
    output = calc(user_input)
    print("= " + str(output))
