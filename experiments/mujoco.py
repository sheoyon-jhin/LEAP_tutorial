import common
import torch
from random import SystemRandom
import datasets
import numpy as np
import os 
import random
from parse import parse_args

from tensorboardX import SummaryWriter
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"

args = parse_args()

def main(
    manual_seed=args.seed,
    intensity=args.intensity, 
    device="cuda",
    max_epochs=args.epoch,
    missing_rate=args.missing_rate,
    pos_weight=10,
    *,  
    model_name=args.model,
    hidden_channels=args.h_channels,
    hidden_hidden_channels=args.hh_channels,
    num_hidden_layers=args.layers,
    ode_hidden_hidden_channels=args.ode_hidden_hidden_channels,
    lr=args.lr,
    c1=args.c1,
    c2=args.c2,
    weight_decay = args.weight_decay,
    dry_run=False,
    method = args.method,
    step_mode = args.step_mode,
    time_seq=args.time_seq,
    y_seq=args.y_seq,
    **kwargs
):                                                                
    
    batch_size = 1024
    lr = lr 
    PATH = os.path.dirname(os.path.abspath(__file__))
    
    np.random.seed(manual_seed)
    random.seed(manual_seed)
    torch.manual_seed(manual_seed)

    torch.cuda.manual_seed(manual_seed)
    torch.cuda.manual_seed_all(manual_seed)
    torch.random.manual_seed(manual_seed)
    
    time_augment = intensity 
    # data loader
    times, train_dataloader, val_dataloader, test_dataloader = datasets.mujoco.get_data(batch_size, missing_rate,time_augment, time_seq,y_seq)
    
    output_time = y_seq
    experiment_id = int(SystemRandom().random()*100000)
    
    file = PATH+'/h_0/'+f'mujoco_{experiment_id}.npy'    
    # feature and time_augmentation.
    input_channels =  time_augment + 14 
    folder_name = 'MuJoCo'
    test_name = "step_" + "_".join([ str(j) for i,j in dict(vars(args)).items()]) + "_" + str(experiment_id)
    result_folder = PATH+'/tensorboard_mujoco'
    writer = SummaryWriter(f"{result_folder}/runs/{folder_name}/{str(test_name)}")
    #model initialize
    make_model = common.make_model(model_name, input_channels, 1, hidden_channels,
                                   hidden_hidden_channels, ode_hidden_hidden_channels, num_hidden_layers, file,use_intensity=intensity, initial=True, output_time=output_time)
    
    if dry_run:
        name = None
    else:
        name = 'MuJoCo'
    
    # main for forecasting 
    return common.main_forecasting(name, model_name, times, train_dataloader, val_dataloader, test_dataloader, device,
                       make_model, max_epochs, lr, weight_decay, writer, file, kwargs, pos_weight=torch.tensor(10),
                       step_mode=step_mode, c1=args.c1, c2 =args.c2)


if __name__ == "__main__":
    main(method = args.method)
    
