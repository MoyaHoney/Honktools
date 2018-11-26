import os
import sys
import logging
import platform

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

    # Function to call whenever a error has happened.
    # error_types: 1 = create_dir_error, TODO fill in error_types
    def on_error(error_type, *on_error_args):
        if error_type == 1:
            print("Failed to create " + on_error_args[0])
            print("""\nYou may be running with improper permissions, or trying to create a
            directory with forbidden characters.""")
            if platform.system() == "Windows":
                print("""Please read http://kizu514.com/blog/forbidden-file-names-on-windows-10/ for
            more information.""")

    # Checks to see if a the supplied output directory should be created if it does not exist.
    def ask_for_arg3():
        print("It looks like ", end="")
        if args_filled:
            print(args[1], end="")
        else:
            pass  # TODO fix else statement to print the dir if *args were not supplied. Don't forget (, end="").
        print(" does not exist.")

        create_2nd_dir = None
        while create_2nd_dir is None:
            create_2nd_dir = (input("Would you like to create it?\nY/N: \n")).upper()
            if create_2nd_dir == "N":
                prompt_exit = (input("Would you like to exit?\nY/N: \n")).upper()
                if prompt_exit == "Y":
                    sys.exit("User prompted to exit.")
                else:
                    create_2nd_dir = None
            return create_2nd_dir

    # Testing if *args has been filled correctly.
    # If *args only has a single argument, raise an error
    if args_filled:
        if number_of_filled_args == 1:
            arg_error()
        # If *args has two statements, check if both dirs are correct.
        # Checking first...
        elif number_of_filled_args == 2:
            create_dirs = None
            if os.path.isdir(args[0]):
                pass
            else:
                arg_error()
            # Checking second...
            if os.path.isdir(args[1]):
                pass
            # If the chosen output directory doesn't exist, prompt if it should be created with the ask_for_arg3 func.
            else:
                while create_dirs is None:
                    if ask_for_arg3() == "Y":
                        try:
                            os.makedirs(args[1])
                        except:
                            on_error(1, args[1])
                    elif ask_for_arg3() == "N":
                        pass
