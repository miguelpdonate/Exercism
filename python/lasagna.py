"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    
#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """function:  preparation_time_in_minutes
    arg: number_of_layers number of layers of the lasagna
    returns lasagna preparation time in minutes
    """
    return PREPARATION_TIME * number_of_layers

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """function: elapsed_time_in_minutes
    arg: number_of_layers
         elapsed_bake_time
    returns the total lasagna elapsed time in minutes
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


bake_elapsed = int(input('Please enter the bake time elapsed in minutes: '))
layers = int(input('Please enter the number of layers of your lasagna: ')) 

print(f"The bake time remaining is: {bake_time_remaining(bake_elapsed)}")
print(f"The preparation time is: {preparation_time_in_minutes(layers)}")
print(f"The total elapsed time is: {elapsed_time_in_minutes(layers, bake_elapsed)}")


