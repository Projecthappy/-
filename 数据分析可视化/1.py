import pandas as pd
df=pd.read_excel(r'C:\Users\哈哈哈\Downloads\电影导演演员.xlsx')
print(df)
pairs=[]
for i in range(len(df)):
    actors = df.at[i,'演员'].split('，')
    for actor in actors:
        pair = (actor, df.at[i,'电影名称'])
        pairs.append(pair)
pairs = sorted(pairs, key=lambda item:int(item[0][2:]))
index = [item[0] for item in pairs]
data = [item[1] for item in pairs]
df1 = pd.DataFrame({'演员':index,'电影名称':data})
result = df1.groupby('演员', as_index=False).count()
result.columns = ['演员', '参演电影数量']
result=result.sort_values('参演电影数量').nlargest(3,'参演电影数量')
print(result)