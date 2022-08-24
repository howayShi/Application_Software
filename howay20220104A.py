import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.onnx
from net import *
import netron


d = torch.rand(1, 3, 416, 416)
m = Net_v2()
o = m(d)

onnx_path = "onnx_model2.onnx"
torch.onnx.export(m, d, onnx_path)

#netron.start(onnx_path)