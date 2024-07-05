# Imports
import webbrowser
import os

def open_html_file(filename):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the HTML file
    file_path = os.path.join(script_dir, 'html', filename)
    # Open the HTML file in a new browser tab
    webbrowser.open_new_tab(f'file://{file_path}')

# Function to prompt and validate user input
def prompt_and_validate(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

# This code is for the introduction.
print("Welcome to the support! Select one of the options below:")
qst1 = prompt_and_validate("1 - Hardware  2 - Software: ", ["1", "2"])

# The hardware prompt.
if qst1 == "1":
    print("Select one of the options")
    qst2 = prompt_and_validate("1 - Storage  2 - Motherboard  3 - CPU  4 - GPU  5 - Keyboard  6 - Touchpad: ", ["1", "2", "3", "4", "5", "6"])
    
    # The storage part
    if qst2 == "1":
        print("Select the storage type")
        qst3 = prompt_and_validate("1 - SSD  2 - HDD: ", ["1", "2"])

        # The SSD prompt 
        if qst3 == "1":
            print("We just opened the SSD formulary in your browser. Please close this window.")
            open_html_file('H1-1.html')

        # The HDD prompt
        elif qst3 == "2":
            print("We just opened the HDD formulary in your browser. Please close this window.")
            open_html_file('H1-2.html')

    # The motherboard part
    elif qst2 == "2":
        print("We just opened the motherboard formulary in your browser. Please close this window.")
        open_html_file('H2.html')

    # The CPU part
    elif qst2 == "3":
        print("We just opened the CPU formulary in your browser. Please close this window.")
        open_html_file('H3.html')

    # The GPU part
    elif qst2 == "4":
        print("We just opened the GPU formulary in your browser. Please close this window.")
        open_html_file('H4.html')

    # The keyboard part
    elif qst2 == "5":
        print("We just opened the keyboard formulary in your browser. Please close this window.")
        open_html_file('H5.html')

    # The touchpad part
    elif qst2 == "6":
        print("We just opened the touchpad formulary in your browser. Please close this window.")
        open_html_file('H6.html')

# The software prompt
elif qst1 == "2":
    print("Please select the software")
    qst4 = prompt_and_validate("1 - Windows  2 - Linux: ", ["1", "2"])

    # The Windows part
    if qst4 == "1":
        print("We just opened the Windows formulary in your browser. Please close this window.")
        open_html_file('S1.html')

    # The Linux options
    elif qst4 == "2":
        print("Select your distro")
        qst5 = prompt_and_validate("1 - Debian  2 - Linux 2.4 (up): ", ["1", "2"])

        # The distro choice
        if qst5 == "1":
            print("We just opened the Debian formulary in your browser. Please close this window.")
            open_html_file('S2-1.html')
            
        elif qst5 == "2":
            print("We just opened the Linux 2.4 (up) formulary in your browser. Please close this window.")
            open_html_file('S2-2.html')
