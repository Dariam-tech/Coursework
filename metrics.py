def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    confusion_matrix = [tp,fp,tn,fn]
    
    for i in range(len(ground_truth)):
        if prediction[i] == ground_truth[i] and ground_truth[i] == True:
            tp += 1
        elif prediction[i] == ground_truth[i] and ground_truth[i] == False:
            tn += 1
        elif ground_truth[i] == False and prediction[i] == True:
            fp += 1
        elif ground_truth[i] == True and prediction[i] == False:
            fn += 1

    if (tp + fp) != 0:
        precision = tp / (tp + fp)
    else:
        precision = 0
    
    if (tp + fn) != 0:
        recall = tp / (tp + fn)
    else:
        recall = 0 
    
    if (precision + recall) != 0:
        f1 = 2 * precision * recall / (precision + recall)
    else:
        f1 = 0 
    accuracy = (tp+tn)/len(prediction)
    
    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    return (prediction == ground_truth).sum() / len(prediction)
