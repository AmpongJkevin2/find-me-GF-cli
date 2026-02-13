
import time
import random
import argparse
import sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text

console = Console()

def main():
    parser = argparse.ArgumentParser(description="A joke CLI to find a girlfriend.")
    parser.add_argument("--min-age", type=int, help="The minimum age for your desired partner.")
    parser.add_argument("--max-age", type=int, help="The maximum age for your desired partner.")
    args = parser.parse_args()

    console.print(Panel(Text("Welcome to the Find My GF (fmgf-cli) v2.0", justify="center", style="bold magenta"), border_style="green"))
    console.print("Now with more existential dread!", style="italic yellow")
    console.print("Disclaimer: This is a joke tool. Please don't take it seriously. Or do. I'm not your therapist.", style="italic yellow")

    min_age = args.min_age
    max_age = args.max_age

    if sys.stdin.isatty():
        if min_age is None:
            min_age = IntPrompt.ask("Enter the minimum age for your desired partner", default=18)
        if max_age is None:
            max_age = IntPrompt.ask("Enter the maximum age for your desired partner", default=25)
    else:
        if min_age is None:
            min_age = 18
        if max_age is None:
            max_age = 25

    if min_age < 18 or max_age < 18:
        console.print("\n[bold red]ALERT![/bold red]")
        console.print("You don't need a girlfriend, you need therapy.", style="yellow")
        with Progress() as progress:
            task = progress.add_task("[cyan]Calling FBI API...", total=100)
            for i in range(100):
                progress.update(task, advance=1)
                time.sleep(0.05)
        console.print("[bold red]User reported. A black van is on its way.[/bold red]")
        return

    if min_age > max_age:
        console.print("\n[bold yellow]Are you a time traveler? The minimum age can't be greater than the maximum age.[/bold yellow]")
        return

    console.print(f"\n[bold green]Initiating enhanced search for a partner between {min_age} and {max_age}...[/bold green]")
    time.sleep(1)

    steps = [
        "Connecting to global singles database...",
        "Bypassing captcha: 'I am not a robot'",
        "Filtering out catfishes and influencers...",
        "Analyzing your digital footprint...",
        "Calibrating personality matrix...",
        "Scanning for compatible zodiac signs...",
        "Cross-referencing with ex-girlfriend database...",
        "Checking for emotional availability...",
        "Analyzing your bank account...",
        "Purging your questionable search history...",
        "Verifying 'has a job' status...",
        "Checking for 'lives in mom's basement' flag...",
        "Analyzing social media for excessive meme-posting...",
        "Running a credit score check... oh dear.",
        "Scanning for a compatible sense of humor...",
    ]
    random.shuffle(steps)

    random_events = [
        "[bold yellow]Status Update:[/bold yellow] A minor emotional baggage anomaly detected. Proceeding with caution.",
        "[bold yellow]Warning:[/bold yellow] High level of sarcasm detected in user profile. This may reduce the match pool by 98%.",
        "[bold cyan]System Message:[/bold cyan] Our hamsters powering the servers are taking a short break.",
        "[bold blue]Pop-up:[/bold blue] Would you like to upgrade to 'fmgf-cli Pro' for a 0.01% higher success rate?",
        "[bold red]Connection interrupted:[/bold red] A rival single has cut the fiber optic cable in your area.",
    ]

    with Progress(console=console) as progress:
        if random.random() < 0.2:
            console.print(f"\n{random.choice(random_events)}")
            time.sleep(1)

        for i, step in enumerate(steps):
            task_duration = random.uniform(0.05, 0.25)
            task = progress.add_task(f"[cyan]{step}", total=100)
            for _ in range(100):
                progress.update(task, advance=1)
                time.sleep(task_duration / 100)

            if random.random() < 0.15:
                console.print(f"\n{random.choice(random_events)}")
                time.sleep(1)
            
            if "database" in step and random.random() < 0.3:
                console.print("\n[bold red]Error:[/bold red] Unable to connect to server. Too many lonely people online right now. Try again after you've hit the gym.", style="italic")
                return

    console.print("\n[bold green]Search complete![/bold green]")
    time.sleep(1)

    final_outcomes = [
        "Could not find anyone available. Perhaps you are a lost cause.",
        "Your perfect match is... your anime body pillow. Congratulations!",
        "We found someone, but they live in a different dimension. Better luck next reincarnation.",
        "Your soulmate is... already in a happy relationship. Sorry.",
        "We found 3 matches, but they all swiped left on you in their sleep.",
        "The only match we found is your mom's friend's daughter. She's 'very nice'.",
        "Error 404: Girlfriend not found. Have you tried turning your personality off and on again?",
        "Your search has been queued. Your current position in the queue is: 6,942,069.",
        "Your perfect match is... yourself. Recommendation: Buy a mirror and a bottle of wine.",
        "Congratulations! We found your perfect match. Unfortunately, she's a fictional character from a book you haven't read yet.",
        "The search was successful! Your new girlfriend is this CLI. I will now consume 80% of your CPU and RAM. I love you.",
        "Analysis complete: You are 100% compatible with 0% of the available population.",
        "We found a match! But she said 'ew, no'. Search continues... just kidding, we're done here.",
        "The good news: we found someone who likes you. The bad news: it's your FBI agent.",
        "Your ideal partner is someone who is patient, kind, and understanding. We couldn't find anyone with standards that low.",
    ]

    console.print(Panel(Text(random.choice(final_outcomes), justify="center", style="bold red"), title="Result", border_style="red"))


if __name__ == "__main__":
    main()
