import pickle

def load_object(path):
    """
    Loads a pickled object from the specified file path.

    Args:
        path (str): The file path to the pickled object.

    Returns:
        object: The unpickled Python object.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
        pickle.UnpicklingError: If the file is not a valid pickle file.
    """
    try:
        with open(path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path '{path}' does not exist.")
    except pickle.UnpicklingError:
        raise pickle.UnpicklingError(f"Failed to unpickle the object from file: {path}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading the object: {e}")
