from sklearn.model_selection import cross_val_score

def model_trainer(models, X, y, cv=5):
    """
    Trains multiple models using cross-validation and evaluates their performance.

    Args:
        models (dict): A dictionary where keys are model names (str) and values are model objects.
        X (array-like): Feature matrix for training.
        y (array-like): Target variable.
        cv (int): Number of cross-validation folds. Default is 5.

    Returns:
        dict: A dictionary with model names as keys and their mean cross-validation scores as values.
    """
    results = {}
    for name, model in models.items():
        try:
            scores = cross_val_score(model, X, y, cv=cv)
            results[name] = scores.mean()
        except Exception as e:
            results[name] = f"Error: {e}"
    return results
