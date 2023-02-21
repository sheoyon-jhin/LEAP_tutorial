import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='LEAP')
    parser.add_argument('--seed', type=int, default=118,help='Seed - Test your luck!')   
    parser.add_argument('--intensity', type=bool, default=True,help='Intensity')
    parser.add_argument('--model', type=str, default='ncde',help='Model Name')
    parser.add_argument('--h_channels', type=int, default=49,help='Hidden Channels')   
    parser.add_argument('--ode_hidden_hidden_channels', type=int, default=40,help='ODE Func Hidden Hidden Channels')    
    parser.add_argument('--hh_channels', type=int, default=49,help='Hidden Hidden Channels')          
    parser.add_argument('--layers', type=int, default=4,help='Num of Hidden Layers')   
    parser.add_argument('--lr', type=float, default=0.0001,help='Learning Rate')  
    parser.add_argument('--epoch',type=int,default = 200,help ='Epoch') 
    parser.add_argument('--step_mode', type=str, default='valloss',help='Learning Rate Scheduler')
    parser.add_argument('--dataset_name', type=str,help='Dataset Name')
    parser.add_argument('--missing_rate', type=float, default=0.3,help='Missing Rate')
    parser.add_argument('--c1', type=float, default=0,help='mse loss coefficient')
    parser.add_argument('--c2', type=float, default=0,help='Hutchinson coefficient')
    parser.add_argument('--method', type=str, default='rk4', help='ode solver')
    parser.add_argument('--weight_decay', type=float, default=1e-5, help='weight_decay')
    parser.add_argument('--time_seq', type=int, default=50, help='time_seq')
    parser.add_argument('--y_seq', type=int, default=10, help='y_seq')
    parser.add_argument('--gpu', type=int, default=0,help='GPU')

    
    return parser.parse_args()