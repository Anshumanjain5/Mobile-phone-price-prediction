from sklearn.model_selection import cross_val_score

def model_trainer(models,X,y):
    results = {}
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=5)
        results[name] = scores.mean()
    return results