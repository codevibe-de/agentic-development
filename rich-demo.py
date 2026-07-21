#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich>=15.0.0",
# ]
# ///
"""Rich library demonstration with various formatting and UI elements."""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.syntax import Syntax
from rich.tree import Tree
from rich.markdown import Markdown
from rich.layout import Layout
import time

console = Console()

def demo_basic_output():
    """Demonstrate basic text output with colors and styling."""
    console.print("[bold cyan]Welcome to Rich Demo![/bold cyan]")
    console.print("[red]This is red text[/red], [green]this is green[/green], and [yellow]this is yellow[/yellow]")
    console.print("[bold]Bold text[/bold] and [italic]italic text[/italic]")
    console.print()

def demo_panel():
    """Demonstrate panel display."""
    console.print(Panel("[bold blue]This is a Panel[/bold blue]",
                        title="Panel Demo",
                        border_style="cyan"))
    console.print()

def demo_table():
    """Demonstrate table display."""
    table = Table(title="Employee Data")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Position", style="magenta")
    table.add_column("Salary", style="green")

    table.add_row("Alice Johnson", "Manager", "$120,000")
    table.add_row("Bob Smith", "Developer", "$95,000")
    table.add_row("Carol White", "Designer", "$85,000")
    table.add_row("David Brown", "DevOps", "$105,000")

    console.print(table)
    console.print()

def demo_syntax_highlighting():
    """Demonstrate syntax highlighting."""
    code = '''def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(f"Result: {result}")'''

    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title="Python Code Example", border_style="green"))
    console.print()

def demo_tree():
    """Demonstrate tree structure display."""
    tree = Tree("📁 Project Root")
    src = tree.add("src")
    src.add("📄 main.py")
    src.add("📄 utils.py")
    src.add("🗂️ models")
    models = src.children[-1]
    models.add("📄 user.py")
    models.add("📄 product.py")

    tree.add("📄 README.md")
    tree.add("📄 requirements.txt")

    console.print(Panel(tree, title="Directory Structure", border_style="blue"))
    console.print()

def demo_progress():
    """Demonstrate progress bar."""
    console.print("[bold]Processing items with progress bar:[/bold]")
    for i in track(range(10), description="Processing..."):
        time.sleep(0.2)
    console.print("[green]✓ Complete![/green]")
    console.print()

def demo_markdown():
    """Demonstrate markdown rendering."""
    md = """
# Rich Markdown Support

Rich can render **Markdown** with proper formatting including:

- Ordered and unordered lists
- *Italic* and **bold** text
- `code blocks`
- And much more!
"""
    console.print(Markdown(md))

def demo_layout():
    """Demonstrate layout system."""
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )

    layout["header"].update(Panel("[bold cyan]Header[/bold cyan]"))
    layout["body"].update(Panel("[yellow]Body Content[/yellow]"))
    layout["footer"].update(Panel("[magenta]Footer[/magenta]"))

    console.print(layout)

def main():
    """Run all demonstrations."""
    console.rule("[bold]Rich Library Demonstrations[/bold]")
    console.print()

    console.print("[bold]1. Basic Output[/bold]")
    demo_basic_output()

    console.print("[bold]2. Panel[/bold]")
    demo_panel()

    console.print("[bold]3. Table[/bold]")
    demo_table()

    console.print("[bold]4. Syntax Highlighting[/bold]")
    demo_syntax_highlighting()

    console.print("[bold]5. Tree Structure[/bold]")
    demo_tree()

    console.print("[bold]6. Progress Bar[/bold]")
    demo_progress()

    console.print("[bold]7. Markdown[/bold]")
    demo_markdown()

    console.print("[bold]8. Layout[/bold]")
    demo_layout()

    console.rule("[bold green]Demo Complete![/bold green]")

if __name__ == "__main__":
    main()