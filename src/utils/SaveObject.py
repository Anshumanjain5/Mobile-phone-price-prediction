import pickle

def save_object(obj):
    with open('data.pkl', 'wb') as f:
        pickle.dump(obj, f)
        