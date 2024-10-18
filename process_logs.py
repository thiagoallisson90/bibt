import numpy  as np
import pandas as pd
from scipy import stats

file_names = {
    'apps': 'apps.csv', 'appsc': 'appsc.csv', 'coll': 'coll.csv', 'collc': 'collc.csv', 
    'delay': 'delay.csv', 'delayc': 'delayc.csv', 'losses': 'losses.csv', 'lossesc': 'lossesc.csv',
    'lqi': 'lqi.csv', 'lqic': 'lqic.csv', 'pkts': 'pkts.csv', 'psr': 'psr.csv', 
    'psrc': 'psrc.csv', 'sfs': 'sfs.csv', 'tput': 'tput.csv', 'tputc': 'tputc.csv'
}

def analysis(data: pd.Series, verbose=False):
    confidence_level = 0.95

    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    n = len(data)

    standard_error = std_dev / np.sqrt(n)

    confidence_interval = stats.t.interval(confidence_level, n-1, loc=mean, scale=standard_error)

    if verbose:
        print(f"Mean: {mean:.3f}")
        print(f"Std: {std_dev:.3f}")
        print(f"Confidence Interval {confidence_level*100:.0f}%: {confidence_interval}")
    
    return mean, std_dev, confidence_interval[0], confidence_interval[1]

def pdr(path: str, name='psr'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_pdr = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                         names=['ulpdr', 'cpsr', 'psr', 'nrun'])
    
    return analysis(df_pdr['psr']), df_pdr['psr'].to_list()

def delay(path: str, name='delay'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_delay = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                           names=['delay', 'unc_delay', 'cpsr_delay', 'avg_toa', 'nrun'])
    
    return analysis(df_delay['delay']), df_delay['delay'].to_list()

def toa(path: str, name='delay'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_toa = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                           names=['delay', 'unc_delay', 'cpsr_delay', 'avg_toa', 'nrun'])
    
    return analysis(df_toa['avg_toa']), df_toa['avg_toa'].to_list()

def energy(path: str, name='tput', n=200):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_energy = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                           names=['tot_bytes', 'tput', 'energy', 'eff1', 'eff2', 'nrun'])
    
    df_energy['energy'] = df_energy['energy'] / n
    return analysis(df_energy['energy']), df_energy['energy'].to_list()

def tput(path: str, name='tput'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_tput = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                           names=['tot_bytes', 'tput', 'energy', 'eff1', 'eff2', 'nrun'])
    
    return analysis(df_tput['tput']), df_tput['tput'].to_list()

def eff2(path: str, name='tput'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_eff2 = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                           names=['tot_bytes', 'tput', 'energy', 'eff1', 'eff2', 'nrun'])
    
    return analysis(df_eff2['eff2']), df_eff2['eff2'].to_list()

def eff1(path: str, name='tput'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df_eff1 = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                           names=['tot_bytes', 'tput', 'energy', 'eff1', 'eff2', 'nrun'])
    
    return analysis(df_eff1['eff1']), df_eff1['eff1'].to_list()

def rssi(path: str, name='lqi'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                        names=['rssi', 'ok_rssi', 'snr', 'ok_snr', 'nrun'])
    
    return analysis(df['rssi']), df['rssi'].to_list()

def snr(path: str, name='lqi'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                        names=['rssi', 'ok_rssi', 'snr', 'ok_snr', 'nrun'])
    
    return analysis(df['snr']), df['snr'].to_list()

def coll(path: str, name='coll'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                        names=['ncoll', 'coll', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'nrun'])
    
    return analysis(df['coll']), df['coll'].to_list()

def losses(path: str, name='losses'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df = pd.read_csv(f'{path}/{k}_{file_names[name]}', 
                        names=['n_i', 'i', 'n_u', 'u', 'n_s', 's', 'n_t', 't', 'n_e', 'e', 'nrun'])
    
    return df[['i', 'u', 's', 't', 'e']].mean()

def sf_dist(path: str, name='sfs'):
    df_k = pd.read_csv(f'{path}/k.csv', names=['d'])
    k = df_k['d'].iloc[0]
    
    df = pd.read_csv(f'{path}/{k}_{name}.csv', names=['7', '8', '9', '10', '11', '12', 'nrun'])    
    data = [df[column].mean() if column != 'nrun' else "" for column in df.columns.to_list()]
    return data
    
