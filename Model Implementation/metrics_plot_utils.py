from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt 

def compute_metrics(predictions, true_labels): 
    """
    Computes metrics for model performance.
    """
    metrics={}
    
    metrics['accuracy'] = accuracy_score(true_labels, predictions)
    metrics['precision'] = precision_score(true_labels, predictions, average='macro')
    metrics['recall'] = recall_score(true_labels, predictions, average='macro')
    metrics['f1'] = f1_score(true_labels, predictions, average='macro')
    
    metrics['precision_weighted'] = precision_score(true_labels, predictions, average='weighted')
    metrics['recall_weighted'] = recall_score(true_labels, predictions, average='weighted')
    metrics['f1_weighted'] = f1_score(true_labels, predictions, average='weighted')
    
    return metrics

def plot_confusion_matrix(true_labels, predictions, label_classes):
    """
    Plots a confusion matrix.
    """
    cm = confusion_matrix(true_labels, predictions)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_classes, yticklabels=label_classes)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')
    plt.show()
    
def plot_losses(model_name, dataset_name, train_losses, val_losses, epochs):
    """
    Plots training and validation losses.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, epochs + 1), train_losses, label='Training Loss')
    plt.plot(range(1, epochs + 1), val_losses, label='Validation Loss')
    plt.title(f'Training and Validation Losses for {model_name} {dataset_name}')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()