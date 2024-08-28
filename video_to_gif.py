import imageio
import pygifsicle


reader = imageio.get_reader('vidd.mp4')
frames = []

for frame in reader:
    frames.append(frame)


imageio.mimsave('output.gif', frames, format='GIF', duration=0.5)


pygifsicle.optimize('output.gif')