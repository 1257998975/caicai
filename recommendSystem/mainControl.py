import  pymysql as pys
import numpy
import pandas as pd
from DataCleaning import dataCleaning as dc
from Calculate import CollaborativeFiltering as cfc

def recommand(request):

    '''
    获取推荐列表
    :param userID:样例ID
    :return: 推荐商品ID
    '''
    userID=request.GET.get('id')
    conn=pys.connect('39.106.19.189','root','caicai','caicai',charset='gbk')
    cursor=conn.cursor()
    cursor.execute("SELECT * from caicai_order_xiebin") #执行SQL语句
    data =list(cursor.fetchall()) #获取返回数据转为列表
    data=pd.DataFrame(data,columns=['userID','goodsID','status','orderID','price','address','tel','rate','count'])#转为pd数据
    #print(data)

    data=dc.ReduceColumns(['orderID','address','tel'],data)#去除相应的列
    cf=cfc.CF(data)
    cf.getUserRates()#获取评分
    cursor2=conn.cursor()
    cursor2.execute("SELECT * FROM caicai_caicai WHERE Goods_id='%s'"%cf.recommend(userID))
    data2=cursor2.fetchall()

    recommenData=[]
    for row in data2:
        result={}
        result['Goods_id']=row[0]
        result['Goods_name']=row[1]
        result['Goods_price']=row[2]
        result['Discount']=row[3]
        result['Goods_picture']=row[4]
        result['Reserves']=row[5]
        result['Goods_location']=row[6]
        result['Goods_count']=row[7]
        result['Goods_states']=row[8]
        recommenData.append(result)
    conn.close()
    return recommenData
    #print(cf.recommend(userID))

if '__main__'==__name__:
    print(recommand('63'))

