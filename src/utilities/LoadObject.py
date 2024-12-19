import pickle

def load_object(path):
    with open(path, 'rb') as file:
        return pickle.load(file)
    
