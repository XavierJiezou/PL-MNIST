import os
import torch
import pytorch_lightning as pl


data_config = {
    'data_dir': os.getcwd(),
    'dims': (1, 28, 28),
    'num_classes': 10,
    'batch_size': 100,
    'num_workders': 16
}


model_config = {
    'channels': 1,
    'width': 28,
    'height': 28,
    'hidden_size': 64
}


lighting_config = {
    'debug': True,
    'example_dims': (100, 1, 28, 28),
    'learning_rate': 1e-3
}


train_config = {
    'max_epochs': 100,
    'gpus': torch.cuda.device_count(),
    'precision': 16,
    'callbacks': [
        pl.callbacks.EarlyStopping(
            monitor='val_loss',
            mode='min',
            patience=10
        )
    ]
}


pl_config = {
    'data': data_config,
    'model': model_config,
    'lightning': lighting_config,
    'train': train_config
}
