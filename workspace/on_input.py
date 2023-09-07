from pynput.mouse import Listener
mouse_clicked = False

# public
def was_clicked():
    global mouse_clicked
    did_click = mouse_clicked
    mouse_clicked = False
    return did_click

# private
def on_click_handler(x, y, button, pressed):
    global mouse_clicked
    if pressed:
        print("Mouse clicked at ({0}, {1}) with {2}".format(x, y, button))
        mouse_clicked = True

# Start the mouse listener
mouse_listener = Listener(on_click=on_click_handler)
mouse_listener.start()
    
# Stop the mouse listener
mouse_listener.stop()