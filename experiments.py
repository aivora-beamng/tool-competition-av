import click
import os

BEAMNG_HOME = r"C:\\BeamNG\\BeamNG.drive-0.24.0.2.13392"
BEAMNG_USER = rf"{BEAMNG_HOME}\\Bin64"

@click.group()
def cli():
    pass


@cli.command()
@click.option('--generator', default='frenetic', help='Test case generator')
@click.option('--time-budget', default=10, help='Time budget for generating tests')
@click.option('--oob-tolerance', default=0.95, help='Proportion of the car allowd to go off the lane')
@click.option('--speed-limit', default=70, help='Speed limit in km/h')
@click.option('--map-size', default=200, help='Size of the road map')
def run_simulations(generator, time_budget, oob_tolerance, speed_limit, map_size):

    command = r"python .\competition.py "
    command += r"--visualize-tests "
    command += r"--time-budget " + str(time_budget) + r" "
    command += r"--oob-tolerance " + str(oob_tolerance) + r" "
    command += r"--speed-limit " + str(speed_limit) + r" "
    command += r"--executor beamng "
    command += rf"--beamng-home {BEAMNG_HOME} "
    command += rf"--beamng-user {BEAMNG_USER} "
    command += r"--map-size " + str(map_size) + r" "
    command += r"--module-name frenetic.src.generators.random_frenet_generator "
    command += r"--class-name CustomFrenetGenerator"

    if generator == 'frenetic':
        os.system(command)
    else:
        print('Unknown test generator: {}'.format(generator))
    

if __name__ == '__main__':
    cli()
