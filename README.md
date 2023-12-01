# pyqt-torch-text-classification-from-number
<div align="center">
  <img src="https://user-images.githubusercontent.com/55078043/229002952-9afe57de-b0b6-400f-9628-b8e0044d3f7b.png" width="150px" height="150px"><br/><br/>
  
  [![](https://dcbadge.vercel.app/api/server/cHekprskVE)](https://discord.gg/cHekprskVE)
  
  [![](https://img.shields.io/badge/한국어-readme-green)](https://github.com/yjg30737/pyqt-torch-text-classification-from-number/blob/main/README.kr.md)
</div>

Example of Text Classification Using Numbers with a PyTorch Model in a Python PyQt GUI

In this example, the text classification model is utilized for diagnosing diabetes based on provided values.

The trained dataset is presented as follows.

![image](https://github.com/yjg30737/pyqt-torch-text-classification-from-number/assets/55078043/6da5b457-5abf-43a2-bfbc-f60729e839a5)

See the "Outcome" column; 0 indicates a negative result, and 1 indicates a positive result, suggesting the presence of diabetes in the patient's record.

You can see the dataset in the "input" tab on the <a href="https://www.kaggle.com/yoonjunggyu/diabetes-diagnosis-model-development-for-gui">Kaggle Notebook</a> and find the source code as well.

Generated model is already included in the repo.

If you want to do text classification from string, <a href="https://github.com/yjg30737/pyqt-torch-text-classification.git">try this</a>.

## Requirements
* PyQt5 >= 5.14
* torch
* numpy

## How to Run
1. git clone ~
2. pip install -r requirements.txt
3. python run ~

## Preview
![image](https://github.com/yjg30737/pyqt-torch-text-classification-from-number/assets/55078043/9017da2a-eb6a-4180-b3d8-d76cf7706cc1)

## Correlation between each attribute and label

When building a dataset, it is very important to understand the correlation between each attribute and the label (outcome). I prefer the following method:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

df = pd.read_csv('../input/pima-indians-diabetes-database/diabetes.csv')

colormap = plt.cm.gist_heat
plt.figure(figsize=(12,12))

sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)
plt.show()
```

![image](https://github.com/yjg30737/pyqt-torch-text-classification-from-number/assets/55078043/758788b7-1e66-46f2-8bb3-d8cd8b63e817)

If you look at the far right column "diabetes", there are correlation figures for each attribute. The closer it is to 1, the higher it is.
