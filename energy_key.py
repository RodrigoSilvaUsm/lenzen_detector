import math
import decimals


def energy_key(distance, range_particle, max_step):
    """
    Returns the key for the dictionary energy.
    """
    #decimals = str(max_step)[::-1].find('.')
    #num_decimals = decimals.count_decimals(max_step)
    if distance == 0:
        return 0
    elif distance > range_particle:
        return math.inf
    else:
        return round(distance, -int(math.log(max_step, 10)))


if __name__ == "__main__":
    energy_key()
