import pandas as pd
import math
import operator
class CF:
    '''
    协同过滤
    '''
    def __init__(self,data):
        '''
        :param data: 清洗后的数据
        '''
        #用户评分字典格式：{userID:[(goodsID,[rate,]),(goodsID,[rate,])...]}
        self.userRates=dict()
        self.data=data
    def getUserRates(self):
        '''
        获得用户评分字典
        :return:
        '''
        dd=self.data.drop_duplicates('userID')#去重,为了获得订单表用户id

        for id in dd['userID']:

            temp2 = {}
            #print(self.data[self.data.userID == id])
            tempdf=self.data[self.data.userID == id]
            for gid in tempdf['goodsID']:
                templist=list((tempdf[tempdf.goodsID == gid])['rate'])#临时储存分数列表
                temp2.setdefault(gid,float(sum(templist)/len(templist)))
                #temp2=(gid,float(sum(templist)/len(templist)))#取分数平均值作为最终评分
                self.userRates.setdefault(id,temp2)

        #print(self.userRates)
    def cosine(self,userID,others):
        #,others):
        '''
        根据余弦相似算法计算相似度
        :param userID:目标用户ID
        :param others:其他用户ID
        :return:
        '''

        thisUser=self.userRates[userID]
        otherUser=self.userRates[others]
        lista=[]
        listb=[]
        for goodsID in thisUser:
            for key in otherUser:
                if goodsID ==key:
                    lista.append(float(thisUser[key]))
                    listb.append(float(otherUser[key]))

        if len(lista)==0:#如果为空，表示该两个用户不相似
            return 0
        up=0
        aa=0
        bb=0

        for a in range(0,len(lista)):#计算余弦算法的数据
            up=up+lista[a]*listb[a]
            aa=aa+lista[a]*lista[a]
            bb=bb+listb[a]*listb[a]
        #print(lista[0])
        #print(lista[1])

        if aa==0 or bb==0:
            return 0
        x=math.sqrt(aa)
        y=math.sqrt(bb)


        degree=float(up/(x*y))#余弦计算相似度，值越接近1越相似

        #print(x*y)
        return degree

    def getSimilarListByuserid(self,userID,num=5):
        '''
        根据用户ID来获取与该ID的相似列表
        :param userID: 用户ID
        :param num:推荐用户个数,默认为5
        :return: 最相似用户列表
        '''
        similarList=dict()
        for key in self.userRates.keys():
            if key!=userID:
                similarList.setdefault(key,self.cosine(userID,key))
        similarList=sorted(similarList.items(), key=lambda x:x[1], reverse=True)
        #根据字典值降序排序并生成元组列表
        lists=similarList[0:num]
        #获取前num个相似度数据元组列表[('ID',相似度)]
        #print(lists)
        usersList=[]
        for item in lists:
            if item[1]!=0:#去除完全不相似的用户
                usersList.append(item[0])
        return usersList

    def recommend(self,userID):
        '''
        获取推荐
        :param userID: 被推荐用户
        :return: 推荐商品列表
        '''
        recommendList=[]
        for id in self.getSimilarListByuserid(userID,):
            for goodsrate in self.userRates[id].items():
                if goodsrate[1]==5:
                    recommendList.append(goodsrate[0])
        recommendList=list(set(recommendList))#获取最终推荐商品id列表
        #print(recommendList)
        return recommendList[0]
	#推荐1条
        #print(self.userRates[userID])
        #uRL=self.userRates[userID]#用户评分列表


    def groupByBehaviour(self):
        pass
