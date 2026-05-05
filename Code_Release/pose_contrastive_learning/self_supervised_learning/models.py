
import torch
import torch.nn as nn
from torchvision import models

class my_resnet:
    @staticmethod
    def resnet18(pretrained=False):
        model = models.resnet18(weights=None)
        model.fc = nn.Identity()
        return model

class linear_layers:
    class linear_layers(nn.Module):
        def __init__(self, input_dim=512, output_dim=128):
            super().__init__()
            self.net = nn.Sequential(
                nn.Linear(input_dim, 256),
                nn.ReLU(),
                nn.Linear(256, output_dim)
            )

        def forward(self, x):
            return self.net(x)
