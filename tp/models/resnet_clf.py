import torch
from torch import nn
import torchvision.models as models

from tp.models.model import ImageClassificationBase
from tp.models.resnet import resnet15


class ResFC1CLF(ImageClassificationBase):
    def __init__(self,
                 num_classes=6,
                 pretrained_model='resnet34',
                 pretrained=True):
        super().__init__()
        # Use a pretrained model
        self.network = getattr(models, pretrained_model)(pretrained=pretrained)
        # Replace last layer
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, xb):
        return torch.sigmoid(self.network(xb))

    def freeze(self):
        # To freeze the residual layers
        for param in self.network.parameters():
            param.require_grad = False
        for param in self.network.fc.parameters():
            param.require_grad = True

    def unfreeze(self):
        # Unfreeze all layers
        for param in self.network.parameters():
            param.require_grad = True


class ResFC2CLF(ResFC1CLF):
    def __init__(self,
                 num_classes=6,
                 pretrained_model='resnet34',
                 pretrained=True):
        super.__init__(num_classes, pretrained_model, pretrained)
        # # Use a pretrained model
        # self.network = getattr(models, pretrained_model)(pretrained=pretrained)

        # # Replace last layer
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Sequential(
            nn.Linear(
                num_ftrs,
                num_ftrs // 4,
            ), nn.ReLU(), nn.Linear(
                num_ftrs // 4,
                num_ftrs // 2,
            ), nn.ReLU(), nn.Linear(num_ftrs // 2, num_classes))


class Res15FC1CLF(ImageClassificationBase):
    def __init__(self,
                 num_classes,
                 pretrained_model='resnet15',
                 pretrained=False):
        super().__init__()
        # Use a pretrained model
        self.pretrained_model = pretrained_model
        self.network = resnet15(pretrained=pretrained,
                                progress=True,
                                num_classes=num_classes)

    def forward(self, xb):
        return self.network(xb)