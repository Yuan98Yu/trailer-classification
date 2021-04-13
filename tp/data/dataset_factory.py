from torchvision.datasets import ImageFolder
import config


def create_full_dataset(cfg):
    return ImageFolder(cfg['data_dir'])
