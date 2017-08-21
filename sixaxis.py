from triangula.input import SixAxis, SixAxisResource

# Button handler, will be bound to the square button later
def handler(button):
  print 'Button {} pressed'.format(button)

# Get a joystick, this will fail unless the SixAxis controller is paired and active
# The bind_defaults argument specifies that we should bind actions to the SELECT and START buttons to
# centre the controller and reset the calibration respectively.
with SixAxisResource(bind_defaults=True) as joystick:
    # Register a button handler for the square button
    joystick.register_button_handler(handler, SixAxis.BUTTON_SQUARE)
    while 1:
        # Read the x and y axes of the left hand stick, the right hand stick has axes 2 and 3
        x = joystick.axes[0].corrected_value()
        y = joystick.axes[1].corrected_value()
        print(x,y)