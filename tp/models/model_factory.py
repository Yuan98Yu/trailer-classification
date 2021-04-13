from tp.utils.device import to_device
from tp.models.resnet_clf import *
from tp.models.timm_clf import *


def create_model(cfg, num_classes):
    model = globals()[cfg['model']]
    model = model(num_classes, cfg['pretrained_model'], cfg['pretrained'])
    model = to_device(model, cfg['device'])
    return model
