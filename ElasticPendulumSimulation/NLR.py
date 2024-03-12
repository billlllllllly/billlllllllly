import torch
from torch import nn
from torch.utils.data import DataLoader
from dataset import EPSdataset


TRAIN_CSV = "C:/Users/sunfar/Desktop/billy/for竹中/物探二/datasetforregression/EPSdata.csv"
device = "cuda" if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 3e-4


class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(9, 16),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        result = self.linear_relu_stack(x)
        return result


trainset = EPSdataset(TRAIN_CSV)
trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True)
valloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=False)

model = LR().to(device)
lossfunc = nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

def train(dataloader, model, loss_fn, optimizer):
    model.train()
    for batch, (X,y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        pred = model(X.float())
        loss = loss_fn(pred, y.float())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X.float())
            test_loss += loss_fn(pred, y).item()
    test_loss /= num_batches
    print(f"Test Error: \n Accuracy: ------, Avg loss: {test_loss:>8f} \n")



for t in range(EPOCHS):
    print(f"----------epoch {t + 1}--------------")
    train(trainloader, model, lossfunc, optimizer)
    test(valloader, model, lossfunc)

print("DONE!")

#draw()