import pickle

def save_object(obj,path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
