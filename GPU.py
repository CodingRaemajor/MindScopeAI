import torch 
print(torch.cuda.is_available()) # it should return True
print(torch.cuda.get_device_name(0))