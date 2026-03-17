from banner import show_banner
from animations import loading_animation
from modules.phone_lookup import lookup
from modules.social_scan import social_links
from rich.console import Console
from rich.panel import Panel

console = Console()

show_banner()

loading_animation()

number = input("\nEnter phone number with country code: ")

try:

    data = lookup(number)
    socials = social_links(number)

    result = f"""
Target Number : {number}

Country       : {data['country']}
Carrier       : {data['carrier']}
Timezone      : {data['timezone']}
Valid Number  : {data['valid']}

OSINT Links
-------------------------
"""

    for k,v in socials.items():
        result += f"{k} : {v}\n"

    console.print(Panel(result, title="EHxNum Results", style="cyan"))

except:
    console.print("[red]Invalid phone number[/red]")
