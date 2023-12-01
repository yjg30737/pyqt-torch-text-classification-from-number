import torch
import torch.nn as nn

import numpy as np


class TextClassifier(nn.Module):
    def __init__(self):
        super(TextClassifier, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(8, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.model(x)


class TextPredictor:
    def __init__(self, model_path):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = self.load_model(model_path)

    def load_model(self, model_path):
        model = TextClassifier().to(self.device)
        model.load_state_dict(torch.load(model_path, map_location=self.device))
        model.eval()
        return model

    def predict_text(self, n_arr):
        with torch.no_grad():
            inputs = torch.Tensor(np.array(n_arr)).to(self.device)
            outputs = self.model(inputs)
            return outputs.item() > 0.5