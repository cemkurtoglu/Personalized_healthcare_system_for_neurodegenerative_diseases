import torch
from torch import nn


class Classifier(nn.Module):
    def __init__(self, input_dim, out_dim):
        super(Classifier, self).__init__()
        self.linear_relu = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.LeakyReLU(0.2),
            # nn.ReLU(),
            # nn.BatchNorm1d(64),
            nn.Dropout(p=0.2),
            nn.Linear(32, 64),
            nn.LeakyReLU(0.2),
            nn.Dropout(p=0.2),
            nn.Linear(64, 16),
            nn.LeakyReLU(0.2),
            nn.Linear(16, out_dim),
        )

    def forward(self, x):
        logits = self.linear_relu(x)
        return logits
