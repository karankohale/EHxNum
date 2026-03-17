from pyfiglet import figlet_format
from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():

    banner = figlet_format("EHxNum")

    console.print(Panel(
        f"""{banner}
Phone OSINT Framework
Created by EHxAnomity
YouTube: EHxAnomity
""",
        style="green"
    ))

    console.print("[yellow]Disclaimer:[/yellow]")
    console.print("This tool gathers only publicly available information.")
    console.print("Do not use this tool for harassment or illegal activities.\n")
