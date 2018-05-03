from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.pixels[2] = (255, 0, 0)
    elif cpx.button_b:
        cpx.pixels[7] = (0, 255, 0)
    else:
        cpx.pixels.fill((0, 0, 0))
