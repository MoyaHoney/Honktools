import os
import logging

honktools_logger = logging.getLogger(os.path.split(os.getcwd())[1] + "\\" + __name__ + ".py")
logging.basicConfig(level=logging.DEBUG)


def skeleton_folders(*args):
    """Makes a copy of a folder and all subfolders, while ignoring files."""
    honktools_logger.debug("*args == " + str(args))
    # Testing if *args have been filled out.
    if not args:
        args_filled = False
    elif args:
        args_filled = True
        number_of_filled_args = len(args)

    # Output statement if *args filled out incorrectly
    def arg_error():
        print("""You have supplied """ + str(len(args)) + """ arguments. Either you have not supplied valid
        arguments, or too few arguments. Function will now continue in a 'input mode'""")
        # TODO Replace with a proper logging/raise.

    # Checks to see if a the supplied output directory should be created if it does not exist.
    def ask_for_arg3():
        print("It looks like ", end="")
        if args_filled:
            print(args[1], end="")
        else:
            pass  # TODO fix else statement to print the dir if *args were not supplied. Don't forget (, end="").
        print(" does not exist.")

        create_2nd_dir = None
        while create_2nd_dir != "Y" or create_2nd_dir != "N":
            create_2nd_dir = (input("Would you like to create it?\nY/N")).upper()

    # Testing if *args has been filled correctly.
    # If *args only has a single argument, raise an error
    if args_filled:
        if number_of_filled_args == 1:
            arg_error()
        # If *args has two statements, check if both dirs are correct.
        # Checking first...
        elif number_of_filled_args == 2:
            if os.path.isdir(args[0]):
                pass
            else:
                arg_error()
            # Checking second...
            if os.path.isdir(args[1]):
                pass
            else:
                ask_for_arg3()
