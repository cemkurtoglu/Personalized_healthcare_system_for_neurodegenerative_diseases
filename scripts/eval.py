import numpy as np
from numpy import exp
import torch
import json

from AI.classifier import Classifier


with open('data.json', 'r') as openfile:
    json_object = json.load(openfile)


def softmax(vector):
    e = exp(vector)
    denom = np.expand_dims(e.sum(axis=1), axis=1)
    return e / denom


def prep_data(jobj):
    N = len(jobj)
    x_normalized = []
    y = []
    for i in range(N):
        x = np.array(
            [jobj[i]['cdrsb'], jobj[i]['adas11'], jobj[i]['adas13'], jobj[i]['mmse'], jobj[i]['ravlt_immediate'],
             jobj[i]['ravlt_learning'], jobj[i]['ravlt_forgetting'], jobj[i]['faq'], jobj[i]['ventricles'],
             jobj[i]['hippocampus'], jobj[i]['whole_brain'], jobj[i]['entorhinal'], jobj[i]['fusiform'],
             jobj[i]['midtemp'], jobj[i]['icv']]).astype(np.float32)
        x[:8] = x[:8] / np.linalg.norm(x[:8])
        x[8:] = x[8:] / x[14]
        x_normalized.append(x[:14])
        if jobj[i]['diagnosis'] == 'MCI':
            y.append(0)
        elif jobj[i]['diagnosis'] == 'NL':
            y.append(0)
        else:
            y.append(1)
    return np.array(x_normalized), np.array(y)


data, label = prep_data(json_object)

model_path = 'checkpoint-1000.pth'

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))

num_classes = 2

input_dim = data.shape[1]

model = Classifier(input_dim, num_classes).to(device)

checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
model.load_state_dict(checkpoint['model'])
model.to(device)
model.eval()

logits = model(torch.from_numpy(data).to(device))
predictions = logits.argmax(1).cpu().detach().numpy()
probabilities = softmax(logits.cpu().detach().numpy())

output = []
for i in range(len(predictions)):
    dictionary = {"rid": json_object[i]['rid'], "prediction": str(predictions[i]),
                  "probability": str(probabilities[i][predictions[i]])}
    output.append(dictionary)

with open("output.json", "w") as outfile:
    json.dump(output, outfile)
