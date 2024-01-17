import datetime
import time
import pygame
import sys

def set_alarm():
    print("Enter the time for the alarm (HH:MM AM/PM):")
    alarm_time_input = input(">> ")

    try:
        alarm_time = datetime.datetime.strptime(alarm_time_input, "%I:%M %p")
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    print("Alarm set for", alarm_time.strftime("%I:%M %p"))

    while current_time != alarm_time.strftime("%I:%M %p"):
        current_time = datetime.datetime.now().strftime("%I:%M %p")

        # Simple spinning animation
        spinner = "|/-\\"
        sys.stdout.write('\r')
        sys.stdout.write("Waiting for the alarm " + spinner[0])
        sys.stdout.flush()
        time.sleep(0.5)

        for char in spinner[1:]:
            sys.stdout.write('\r')
            sys.stdout.write("Waiting for the alarm " + char)
            sys.stdout.flush()
            time.sleep(0.5)

    print("\nWake up!")

    # Play a sound using pygame (cross-platform)
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\ASUS\Desktop\debotics internship python\Night by ikson.mp3")  # Replace with your sound file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    set_alarm()
