from sklearn.metrics import r2_score

def model_trainer(models, X_train, y_train, X_test, y_test):
    """
    Trains multiple models using cross-validation, evaluates their performance,
    and returns the best-performing model after sorting by their scores.

    Args:
        models (dict): A dictionary where keys are model names (str) and values are model objects.
        X_train (array-like): Feature matrix for training.
        y_train (array-like): Target variable for training.
        X_test (array-like): Feature matrix for testing (optional, not used in this function).
        y_test (array-like): Target variable for testing (optional, not used in this function).
        cv (int): Number of cross-validation folds. Default is 5.

    Returns:
        tuple: A tuple containing the best model (model object), its mean cross-validation score,
               and a sorted list of all models based on their cross-validation scores.
    """
    results = {}
    for name, model in models.items():
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)
        score = r2_score(y_test,y_pred)
        results[name] = score
    print(results)
    best_model_score = max(sorted(results.values()))
    best_model_name = list(results.keys())[list(results.values()).index(best_model_score)]
    best_model = models[best_model_name]

    return best_model, best_model_score, best_model_name