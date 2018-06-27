import pandas as pd
import numpy
def ReduceColumns(columns,df):
    '''
    :param df:要操作的数据表
    :param columns: 要删除的列名列表
    :return: 删除列之后的dataframe
    '''
    df.drop(columns,axis=1,inplace=True)
    return df