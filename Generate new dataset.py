file_name=os.listdir('/Users/yuanzhihao/Desktop/valid')
file_name.sort()
print(file_name[0])
print(file_name[354])

file_name=os.listdir('/Users/yuanzhihao/Desktop/newvalid')
df1=pd.read_csv('/Users/yuanzhihao/Desktop/newvalid/20190101.csv')
file_name.sort()
new_df=pd.DataFrame(columns=df1.columns,index=[0])
for i in range(0,354):
    file_path='/Users/yuanzhihao/Desktop/valid'+'/'+file_name[i]
    df=pd.read_csv(file_path)
    for i in range(0,30):
        df2=df[df['failure_day']==i]
        new_df=new_df.append(df2)
    df3=df[df['failure_day']==30]
    max=len(df[df['failure_day']==7])
    new_df=new_df.append(df3.sample(n=max))
new_df.drop(new_df.index[0], inplace=True) 
new_df.drop(new_df.columns[0],axis=1, inplace=True)
new_df=new_df.reset_index(drop=True)
new_df=new_df.reset_index(drop=True)
new_df1=pd.DataFrame(columns=new_df.columns,index=[0])
for i in range(0,31):
    df2=new_df[new_df['failure_day']==i]
    for j in new_df.columns[1:12]:
        df2[j]= df2[j].fillna(df2[j].median())
    new_df1=new_df1.append(df2)
new_df1.drop(new_df1.index[0], inplace=True) 
new_df1=new_df1.reset_index(drop=True)

new_df1.to_csv('1-12_ssd_valid.csv')

file_name=os.listdir('/Users/yuanzhihao/Desktop/newtrain')
file_name.sort()
new_df=pd.DataFrame(columns=df1.columns,index=[0])
for i in range(0,354):
    file_path='/Users/yuanzhihao/Desktop/newtrain'+'/'+file_name[i]
    df=pd.read_csv(file_path)
    for i in range(0,30):
        df2=df[df['failure_day']==i]
        new_df=new_df.append(df2)
    df3=df[df['failure_day']==30]
    max=len(df[df['failure_day']==7])
    new_df=new_df.append(df3.sample(n=max))
new_df.drop(new_df.index[0], inplace=True) 
new_df.drop(new_df.columns[0],axis=1, inplace=True)
new_df=new_df.reset_index(drop=True)
new_df=new_df.reset_index(drop=True)
new_df1=pd.DataFrame(columns=new_df.columns,index=[0])
for i in range(0,31):
    df2=new_df[new_df['failure_day']==i]
    for j in new_df.columns[1:12]:
        df2[j]= df2[j].fillna(df2[j].median())
    new_df1=new_df1.append(df2)
new_df1.drop(new_df1.index[0], inplace=True) 
new_df1=new_df1.reset_index(drop=True)
print(new_df1.columns)
new_df1.to_csv('1-12_ssd_train.csv')
