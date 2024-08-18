import keyboard


def clear_screen():
    print("\033[H\033[2J", end="")


def get_key_release():
    event = keyboard.read_event(suppress=True)
    if event.event_type == keyboard.KEY_UP:
        return event.name
    else:
        return "null"
