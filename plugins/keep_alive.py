import pyautogui
import time
import click


@click.command(help="keep the target alive")
@click.option('--delay', default=120, help="Enter the time you want move the mouse to keep the target awake")
def stayalive(delay):
    # This simply draws a square oon your screen to keep your target alive
    click.echo("\nYou computer is being kept alive by this terminal\n")
    while True:
        pyautogui.moveTo(100, 100, duration=1)
        time.sleep(.1)
        pyautogui.moveTo(100, 800, duration=1)
        time.sleep(.1)
        pyautogui.moveTo(1200, 800, duration=1)
        time.sleep(.1)
        pyautogui.moveTo(1200, 100, duration=1)
        time.sleep(.1)
        pyautogui.moveTo(100, 100, duration=1)
        time.sleep(delay)
