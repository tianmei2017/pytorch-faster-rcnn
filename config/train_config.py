import sys


def add_pypath(path):
    if path not in sys.path:
        sys.path.insert(0, path)


class Config:

    backbone = 'mobilenet'  # [vgg16, resnet-fpn, mobilenet]
    pretrained_weights = None  # [path or None]

    train_horizon_flip_prob = 0.5  # data horizon flip probility in train transform

    anchor_size = [64, 128, 256]
    anchor_ratio = [0.5, 1, 2.0]

    device_name = 'cuda:2'

    resume = ''  # pretrained_weights
    start_epoch = 0  # start epoch
    num_epochs = 500  # train epochs

    lr = 5e-4
    lr_gamma = 0.5
    lr_dec_epoch = list(range(6, 40, 6))

    batch_size = 32
    weight_decay = 1e-5

    num_class = 80 + 1  # foreground + 1 background
    data_root_dir = " "
    model_save_dir = " "


cfg = Config()
