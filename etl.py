#!/usr/bin/env python3
import pandas as pd
import numpy as np
import json

def main():
    with open('wave.json', 'r') as f:
        data = json.load(f)

    df_list = []

    col_names = [
        'timestamp_epoch',
        'surf_min',
        'surf_max',
        'surf_humanRelation',
    ]

    # Only ever see 6 diff swells
    for i in range(6):
        col_names.append(f'swell_{i}_height')
        col_names.append(f'swell_{i}_period')
        col_names.append(f'swell_{i}_impact')
        col_names.append(f'swell_{i}_direction')
        col_names.append(f'swell_{i}_directionMin')
        col_names.append(f'swell_{i}_optimalScore')
        
    for d in data['data']['wave']:
        ts = int(d['timestamp'])
        surf_min = float(np.round(d['surf']['raw']['min'], 2))
        surf_max = float(np.round(d['surf']['raw']['max'], 2))
        surf_humanRelation = d['surf']['humanRelation']

        swell_list = list(d['swells'])
        swell_vector = list()
        
        for i in range(6):
            swell_vector.append(np.round(float(swell_list[i]['height']), 2))
            swell_vector.append(int(swell_list[i]['period']))
            swell_vector.append(np.round(float(swell_list[i]['impact']), 2))
            swell_vector.append(np.round(float(swell_list[i]['direction']), 2))
            swell_vector.append(np.round(float(swell_list[i]['directionMin']), 2))
            swell_vector.append(int(swell_list[i]['optimalScore']))

        df_list.append(pd.DataFrame(data=[[ts, surf_min, surf_max, surf_humanRelation, *swell_vector]], columns=col_names))


    wave_df = pd.concat(df_list)
    wave_df['timestamp_utc'] = pd.to_datetime(wave_df['timestamp_epoch'], unit='s')
    wave_df = wave_df.set_index('timestamp_epoch')
    wave_df['rating'] = ''
    
    for i in wave_df.index:
        if wave_df.loc[i, 'surf_max'] >= 2:
            wave_df.loc[i, 'rating'] = 'N'
        else:
            wave_df.loc[i, 'rating'] = 'Y'

    wave_df.to_pickle('wave_data.pkl')
   
if __name__ == '__main__':
    main()

