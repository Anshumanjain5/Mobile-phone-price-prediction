import pickle

def save_object(obj, path):
    """
    Saves a Python object to a file using pickle.

    Args:
        obj (object): The Python object to be saved.
        path (str): The file path where the object should be saved.

    Raises:
        IOError: If there is an error while writing to the file.
        pickle.PicklingError: If the object cannot be pickled.
    """
    try:
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
        print(f"Object saved successfully at {path}")
    except IOError as e:
        print(f"Error while saving object to {path}: {e}")
        raise
    except pickle.PicklingError as e:
        print(f"Error while pickling the object: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred while saving the object: {e}")
        raise
