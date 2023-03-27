########################################
##                                    ##
##      Author : Egemen Gulpinar      ##
##  Mail : egemengulpinar@gmail.com   ##
##     github.com/egemengulpinar      ##
##                                    ##
########################################
import threading
import mouse
import keyboard
import time
mouse_events = []
recording = False
looping = False
pause_bool = True
speed_factor = 2.4
stop_playback_event = threading.Event()
stop_playback_event.clear()
def record_mouse():
    global recording, mouse_events
    recording = True
    mouse_events = []
    mouse.hook(mouse_events.append)

def stop_recording_mouse():
    global recording, mouse_events
    recording = False
    try:
        mouse.unhook(mouse_events.append)
    except:
        print("you already pressed stop key")
def play_mouse():
    global recording, mouse_events, speed_factor


    #custom_play(mouse_events, speed_factor=speed_factor)
    stop_playback_event.clear()
    playback_thread = threading.Thread(target=custom_play, args=(mouse_events, speed_factor))
    playback_thread.start()

def loop_playback():
    global looping, mouse_events
    looping = True
    while looping:
        stop_playback_event.clear()
        custom_play(mouse_events, speed_factor=speed_factor)


def stop_loop():
    global looping

    looping = False

    stop_playback_func()

def custom_play(events, speed_factor=1.0):
    cnt = 0
    for event in events:
        if stop_playback_event.is_set():
            break
        if isinstance(event, mouse.ButtonEvent):
            if event.event_type == mouse.UP:
                mouse.release(event.button)
            else:
                mouse.press(event.button)
        elif isinstance(event, mouse.MoveEvent):
            mouse.move(event.x, event.y)
        elif isinstance(event, mouse.WheelEvent):
            mouse.wheel(event.delta)
        if cnt%3==0:
            time.sleep(0.07 / speed_factor)
        cnt += 1

def stop_playback_func():
    stop_playback_event.set()

def increment_speed():
    global speed_factor
    speed_factor += 0.1
    print("Speed factor: {:.2f}X".format(speed_factor))

def decrement_speed():
    global speed_factor
    speed_factor -= 0.1
    print("Speed factor: {:.2f}X".format(speed_factor))


if __name__ == "__main__":
    print(20* "#" + "     " + "Mouse Event Recorder" +  "     " + 20* "#")

    print("\n \n Follow these instructions\n F1 to start recording \n F2 to stop \n F3 to play\n F4 to loop playback\n F5 to stop looping\n +  to increase speed \n -  to decrease speed\n\n")
    keyboard.on_press_key("f1", lambda _: record_mouse())
    try:
        keyboard.on_press_key("f2", lambda _: stop_recording_mouse())
    except:
        print("you already pressed stop key")
    keyboard.on_press_key("f3", lambda _: threading.Thread(target=play_mouse).start() if not looping else None)
    keyboard.on_press_key("f4", lambda _: threading.Thread(target=loop_playback).start() if not looping else None)
    keyboard.on_press_key("f5", lambda _: stop_loop())
    keyboard.on_press_key("+", lambda _: increment_speed())
    keyboard.on_press_key("-", lambda _: decrement_speed())

    print("Speed factor: {:.2f}X".format(speed_factor))
    keyboard.wait()
