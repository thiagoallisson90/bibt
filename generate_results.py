import pandas as pd

from .plots import *
from .process_logs import *

sms = [200, 400, 600, 800, 1000]
base_dir = '/home/thiago/Documentos/Doutorado/Jisa2024'
km_dir = f'{base_dir}/km'
kmd_dir = f'{base_dir}/kmd'
place_dir = f'{base_dir}/place'
cplace_dir = f'{base_dir}/cplace_pdr'
labels = ['KM', 'KMD', 'Place', 'cPlace']

def execute():
    # PDR
    km_mean = []
    kmd_mean = []
    place_mean = []
    cplace_mean = []
    
    a = [400, 600]
    r = None
    for sm in sms:
        r = pdr(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/pdr_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = pdr(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/pdr_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = pdr(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/pdr_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = pdr(f'{cplace_dir}/{sm}', 'psrc')        
        else:
            r = pdr(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/pdr_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Average PDR', labels=labels, figname=f'{base_dir}/imgs/pdr.png', unit='%')
    
    # Delay
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = delay(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/delay_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = delay(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/delay_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = delay(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/delay_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = delay(f'{cplace_dir}/{sm}', 'delayc')        
        else:
            r = delay(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/delay_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Average Delay', labels=labels, figname=f'{base_dir}/imgs/delay.png', unit='ms')
    
    # Energy
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = energy(f'{km_dir}/{sm}', n=sm)        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/energy_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = energy(f'{kmd_dir}/{sm}', n=sm)        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/energy_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = energy(f'{place_dir}/{sm}', n=sm)        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/energy_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = energy(f'{cplace_dir}/{sm}', 'tputc', n=sm)        
        else:
            r = energy(f'{cplace_dir}/{sm}', n=sm)        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/energy_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Avg. Energy Consumption', labels=labels, figname=f'{base_dir}/imgs/energy.png', unit='J')
    
    # ToA
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = toa(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/toa_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = toa(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/toa_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = toa(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/toa_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = toa(f'{cplace_dir}/{sm}', 'delayc')        
        else:
            r = toa(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/toa_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Average ToA', labels=labels, figname=f'{base_dir}/imgs/toa.png', unit='s')
    
    # Tput
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = tput(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/tput_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = tput(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/tput_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = tput(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/tput_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = tput(f'{cplace_dir}/{sm}', 'tputc')        
        else:
            r = tput(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/tput_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Throughput', labels=labels, figname=f'{base_dir}/imgs/tput.png', unit='b/s')
    
    # Energy Efficiency
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = eff2(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/eff2_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = eff2(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/eff2_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = eff2(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/eff2_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = eff2(f'{cplace_dir}/{sm}', 'tputc')        
        else:
            r = eff2(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/eff2_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Avg. Energy Efficiency', labels=labels, figname=f'{base_dir}/imgs/eff2.png', unit='b/s/kJ')
    
    # Energy Efficiency
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = eff1(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/eff1_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = eff1(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/eff1_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = eff1(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/eff1_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = eff1(f'{cplace_dir}/{sm}', 'tputc')        
        else:
            r = eff1(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/eff1_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Avg. Energy Efficiency', labels=labels, figname=f'{base_dir}/imgs/eff1.png', unit='b/s/J')
    
    # RSSI
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = rssi(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/rssi_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = rssi(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/rssi_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = rssi(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/rssi_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = rssi(f'{cplace_dir}/{sm}', 'lqic')        
        else:
            r = rssi(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/rssi_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Average RSSI', labels=labels, figname=f'{base_dir}/imgs/rssi.png', unit='dBm')
    
    # SNR
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = snr(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/snr_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = snr(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/snr_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = snr(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/snr_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = snr(f'{cplace_dir}/{sm}', 'lqic')        
        else:
            r = snr(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/snr_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Average SNR', labels=labels, figname=f'{base_dir}/imgs/snr.png', unit='dB')
    
    # Collisions
    km_mean.clear()
    kmd_mean.clear()
    place_mean.clear()
    cplace_mean.clear()
    
    for sm in sms:
        r = coll(f'{km_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{km_dir}/{sm}/coll_interval.csv', header=False, index=False)
        km_mean.append(r[0][0])
        
        r = coll(f'{kmd_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{kmd_dir}/{sm}/coll_interval.csv', header=False, index=False)
        kmd_mean.append(r[0][0])
        
        r = coll(f'{place_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{place_dir}/{sm}/coll_interval.csv', header=False, index=False)
        place_mean.append(r[0][0])
        
        if sm in a:
            r = coll(f'{cplace_dir}/{sm}', 'collc')        
        else:
            r = coll(f'{cplace_dir}/{sm}')        
        pd.DataFrame([r[0][0], r[0][1], r[0][2], r[0][3]]).to_csv(f'{cplace_dir}/{sm}/coll_interval.csv', header=False, index=False)
        cplace_mean.append(r[0][0])
    
    y = [km_mean, kmd_mean, place_mean, cplace_mean]
    plot_curves(x=sms, y=y, xlabel='Number of SMs', ylabel='Avg. Collision Rate', labels=labels, figname=f'{base_dir}/imgs/coll.png', unit='%')
    
    # SFs
    data = []
    filename = f'{base_dir}/imgs/sfs.csv'
    
    for i, sm in enumerate(sms):
        r = sf_dist(f'{km_dir}/{sm}')        
        data.append(r)
        
        r = sf_dist(f'{kmd_dir}/{sm}')        
        data.append(r)
        
        r = sf_dist(f'{place_dir}/{sm}')        
        data.append(r)
        
        if sm in a:
            r = sf_dist(f'{cplace_dir}/{sm}', 'sfsc')        
        else:
            r = sf_dist(f'{cplace_dir}/{sm}')        
        data.append(r)
        
        if i == 0:
            save_sfs(data=data, n=sm, filename=filename, mode='w')
        else:
            save_sfs(data=data, n=sm, filename=filename)
        data.clear()
    
    n = 200
    df = pd.read_csv(filename, names=['7', '8', '9', '10', '11', '12', 'n'])
    selected_rows = df[df['n'] == n][['7', '8', '9', '10', '11', '12']].to_numpy().tolist()
    plot_bars(x=[7, 8, 9, 10, 11, 12], y=selected_rows, xlabel='SF Distribution', ylabel='Percentage', 
              labels=labels, figname=f'{base_dir}/imgs/{n}_sfs.png', unit='%')
    
    # PLR    
    plr_u = []
    plr_i = []
    plr_s = []
    plr_t = []
    plr_e = []
    for sm in sms:
        df = losses(f'{kmd_dir}/{sm}')
        plr_u.append(df['u'])
        plr_i.append(df['i'])
        plr_s.append(df['s'])
        plr_t.append(df['t'])
        plr_e.append(df['e'])
    
    plot_stacked_bars(sms, [plr_u, plr_i, plr_s, plr_t, plr_e], 
                      xlabel='Number of SMs', ylabel='Percentage',
                      labels=['PLR-U', 'PLR-I', 'PLR-S', 'PLR-T', 'PLR-E'], figname=f'{base_dir}/imgs/kmd_plr.png')
    
    plr_u.clear()
    plr_i.clear()
    plr_s.clear()
    plr_t.clear()
    plr_e.clear()
    for sm in sms:
        df = losses(f'{cplace_dir}/{sm}')
        plr_u.append(df['u'])
        plr_i.append(df['i'])
        plr_s.append(df['s'])
        plr_t.append(df['t'])
        plr_e.append(df['e'])
    
    plot_stacked_bars(sms, [plr_u, plr_i, plr_s, plr_t, plr_e], 
                      xlabel='Number of SMs', ylabel='Percentage',
                      labels=['PLR-U', 'PLR-I', 'PLR-S', 'PLR-T', 'PLR-E'], figname=f'{base_dir}/imgs/cplace_plr.png')