from rich.console import Console
from rich.text import Text
import math
import statistics

console = Console()

# Blue gradient from light to dark (but not too dark)
blue_gradient = [
    "#a7d8ff",  # Light blue
    "#7fcaff",
    "#57bcff",
    "#30aeff",
    "#189ed9",
    "#0f7bb8",
    "#0a5b94",
    "#084272",  # Still visible dark blue
]

ascii_art = [
" ▄████████   ▄████████   ▄█         ▄████████  ▄██   ▄   ",
"███    ███  ███    ███  ███        ███    ███  ███   ██▄ ",
"███    █▀   ███    ███  ███        ███    █▀   ███▄▄▄███ ",
"███         ███    ███  ███        ███         ▀▀▀▀▀▀███ ",
"███       ▀███████████  ███        ███         ▄██   ███ ",
"███    █▄   ███    ███  ███        ███    █▄   ███   ███ ",
"███    ███  ███    ███  ███▌    ▄  ███    ███  ███   ███ ",
"████████▀   ███    █▀   █████▄▄██  ████████▀    ▀█████▀  "
]

# Top and bottom line (same length as ASCII art)
line = "▬" * len(ascii_art[0])

# Print top line
console.print(line, style=f"{blue_gradient[0]}")

# Print ASCII art with gradient
for i, row in enumerate(ascii_art):
    console.print(Text(row, style=blue_gradient[i]))

# Print bottom line
console.print(line, style=f"{blue_gradient[-1]}")

# Allowed functions in expressions
allowed_functions = {
    'abs': abs,
    'round': round,
    'pow': pow,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'rad': math.radians,
    'deg': math.degrees,
    'log': math.log,
    'log10': math.log10,
    'log2': math.log2,
    'exp': math.exp,
    'e': math.e,
    'pi': math.pi,
    'mean': lambda *args: statistics.mean(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else statistics.mean(args),
    'median': lambda *args: statistics.median(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else statistics.median(args),
    'mode': lambda *args: statistics.mode(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else statistics.mode(args),
    'stdev': lambda *args: statistics.stdev(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else statistics.stdev(args),
    'variance': lambda *args: statistics.variance(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else statistics.variance(args),
    'sqrt': math.sqrt,
    'cbrt': lambda x: x ** (1/3)  # Cube root
}

console.print("\n[bold cyan]Python Expression Calculator[/bold cyan]")
console.print("Use 'sqrt(x)' for square root, 'cbrt(x)' for cube root.")
console.print("Type 'exit' to quit.\n")

# User input loop
while True:
    user_input = input("Enter expression: ")
    if user_input.lower() in ['exit', 'quit']:
        console.print("[bold green]Goodbye![/bold green]")
        break
    try:
        parsed_input = user_input.replace('^', '**')
        result = eval(parsed_input, {"__builtins__": None}, allowed_functions)
        console.print(f"[bold yellow]Result:[/bold yellow] {result}\n")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}\n")
