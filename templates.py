import os

def create_init(path):
    """
    Recursively creates '__init__.py' files in all subdirectories of the given path,
    except for those named '.git'.

    Args:
        path (str): The root directory where the function will begin creating '__init__.py'.
    """
    try:
        # List all directories in the current path
        dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
        
        for dir in dirs:
            # Skip the '.git' directory
            if dir == ".git":
                continue

            # Define the path for the '__init__.py' file
            init_file = os.path.join(path, dir, '__init__.py')

            # If the '__init__.py' file does not exist, create it
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    f.write('')  # Creates an empty __init__.py file

            # Recursively process subdirectories
            create_init(os.path.join(path, dir))

    except Exception as e:
        print(f"Error occurred while processing {path}: {e}")

# Starting the process from the current working directory
create_init(os.getcwd())
