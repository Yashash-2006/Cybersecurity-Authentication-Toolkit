"""
Utilities & Rich Formatting Helper Module
----------------------------------------
Provides console formatting using Rich (with fallback to standard ANSI text), 
data loading (JSON & CSV log parsers), and visual report helpers.
"""

import os
import json
import csv
from typing import List, Dict, Any, Union

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.prompt import Prompt
    from rich import print as rprint
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


def print_banner(title: str, subtitle: str = ""):
    """Prints a styled header banner."""
    if HAS_RICH and console:
        grid_text = f"[bold cyan]{title}[/bold cyan]"
        if subtitle:
            grid_text += f"\n[italic yellow]{subtitle}[/italic yellow]"
        console.print(Panel(grid_text, expand=False, border_style="cyan"))
    else:
        print("=" * 65)
        print(f"      {title.upper()}")
        if subtitle:
            print(f"      {subtitle}")
        print("=" * 65)


def print_alert(message: str, style: str = "red"):
    """Prints a security alert message."""
    if HAS_RICH and console:
        if style == "red" or style == "error":
            console.print(Panel(f"[bold red]ALERT:[/bold red] {message}", border_style="bold red"))
        elif style == "warning" or style == "yellow":
            console.print(Panel(f"[bold yellow]WARNING:[/bold yellow] {message}", border_style="bold yellow"))
        else:
            console.print(Panel(f"[bold green]SUCCESS:[/bold green] {message}", border_style="bold green"))
    else:
        print(f"\n[!] {message}\n")


def load_json_logs(filepath: str) -> List[Dict[str, Any]]:
    """Loads authentication attempt logs from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"JSON log file not found at: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def load_csv_logs(filepath: str) -> List[Dict[str, Any]]:
    """Loads authentication attempt logs from a CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV log file not found at: {filepath}")
    
    logs = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append(dict(row))
    return logs
