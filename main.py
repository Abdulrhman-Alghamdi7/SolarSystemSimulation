import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel
from astropy.time import Time
from astropy import units as u
from matplotlib.animation import FuncAnimation


def solarSystemSimulation():
    planets = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    solar_system_ephemeris.set('builtin')

    time_start = Time('2023-11-23 00:00:00')
    time_end = Time('2024-11-23 00:00:01')
    time_step = 1 * u.day
    times = Time(np.arange(time_start.jd, time_end.jd, time_step.to(u.day).value), format='jd')
    positions = {}
    velocities = {}

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 2, 1])
    ax.view_init(30, 60)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    bodies = {}
    planet_names = {}

    def update(frame):
        global n
        for body in planets:
            pos, vel = get_body_barycentric_posvel(body, times[frame])
            positions[body] = pos
            velocities[body] = vel
            size = 200 if body == 'Sun' else size
            size = 120 if body == 'Jupiter' else size
            size = 110 if body == 'Saturn' else size 
            size = 90 if body == 'Neptune' else size
            size = 80 if body == 'Uranus' else size 
            size = 60 if body == 'Earth' else size
            size = 50 if body == 'Venus' else size
            size = 30 if body == 'Mars' else size
            size = 20 if body == 'Mercury' else size

            color = 'yellow' if body == 'Sun' else 'grey'
            color = 'red' if body == 'Mars' else color
            color = 'orange' if body == 'Jupiter' else color
            color = 'brown' if body == 'Saturn' else color
            color = 'cyan' if body == 'Uranus' else color
            color = 'b' if body == 'Neptune' else color
            color = 'blue' if body == 'Earth' else color
            color = 'brown' if body == 'Venus' else color
            color = 'grey' if body == 'Mercury' else color
            
            if body in bodies:
                bodies[body].remove()
            
            planet = ax.scatter(positions[body].x.value, positions[body].y.value, positions[body].z.value, s=size*10, c=color)
            bodies[body] = planet

            #this comminted code is for draw the orbit of planets but it make the simulation very slow
            #ax.scatter(positions[body].x.value, positions[body].y.value, positions[body].z.value, color='white',s=size/1000, alpha=1)
            
            if body not in planet_names:
                ax.text(positions[body].x.value, positions[body].y.value, positions[body].z.value, body, color='white', fontsize=10)
                planet_names[body] = True
            # n += 1

    ax.set_axis_off()
    ax.set_facecolor('black')

    animation = FuncAnimation(fig, update, frames=len(times), interval=30)

    plt.show()

solarSystemSimulation()
