"""
This is a boilerplate pipeline 'nome_do_pipeline'
generated using Kedro 0.19.12
"""
import pandas as pd

def prepare_data(df_dev):
    return (
        df_dev
        [
        ['lat','lon','minutes_remaining', 'period', 'playoffs', 'shot_distance','shot_made_flag']
        ].dropna()
    )

