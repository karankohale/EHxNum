from halo import Halo
import time

def loading_animation():

    spinner = Halo(text='Initializing OSINT modules...', spinner='dots')
    spinner.start()

    time.sleep(2)

    spinner.text = "Connecting telecom databases..."
    time.sleep(2)

    spinner.text = "Scanning open-source intelligence..."
    time.sleep(2)

    spinner.succeed("Modules Loaded")
