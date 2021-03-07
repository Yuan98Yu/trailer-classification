# from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import torch


def plt_confusion_matrix(outputs, y_true, num_classes):
    sns.set()

    confusion_matrix = torch.zeros(num_classes, num_classes)
    with torch.no_grad():
        _, preds = torch.max(outputs, 1)
        for t, p in zip(y_true.view(-1), preds.view(-1)):
            confusion_matrix[t.long(), p.long()] += 1
    f, ax = plt.subplots()
    print(confusion_matrix)  # 打印出来看看
    print(confusion_matrix.diag()/confusion_matrix.sum(1))
    sns.heatmap(confusion_matrix, annot=True, ax=ax)  # 画热力图

    ax.set_title('confusion matrix')  # 标题
    ax.set_xlabel('predict')  # x轴
    ax.set_ylabel('true')  # y轴

    return f
