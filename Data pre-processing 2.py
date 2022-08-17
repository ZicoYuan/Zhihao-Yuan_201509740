file=pd.read_csv('ssd_failure_label.csv')
file

date_day=[] #Empty list
for i,row in file.iterrows():#Iteration loops
    date_str=str(datetime.datetime.strptime(row['failure_time'],"%Y/%m/%d %H:%M").date()) #String conversion to date form
    date_str1=date_str[0:10]
    date_day.append(date_str1)
file.insert(len(file.columns),'failure_date',date_day)
file


file_name=os.listdir('/Users/yuanzhihao/Desktop/smartlog2019ssd' )
for i in range(len(file_name)):
    file_path=r'/Users/yuanzhihao/Desktop/smartlog2019ssd'+'/'+file_name[i]
    file_path1='/Users/yuanzhihao/Desktop/train'+'/'+file_name[i]
    file_path2='/Users/yuanzhihao/Desktop/valid'+'/'+file_name[i]
    df1=pd.read_csv(file_path)
    df1=df1.dropna(axis=1,how="all")
    df1['5']=df1['n_5']-df1['r_5']
    df1['9']=df1['n_9']-df1['r_9']
    df1['12']=df1['n_12']-df1['r_12']
    df1['183']=df1['n_183']-df1['r_183']
    df1['184']=df1['n_184']-df1['r_184']
    df1['187']=df1['n_187']-df1['r_187']
    df1['188']=df1['n_188']-df1['r_188']
    df1['196']=df1['n_196']-df1['r_196']
    df1['197']=df1['n_197']-df1['r_197']
    df1['198']=df1['n_198']-df1['r_198']
    df1['199']=df1['n_199']-df1['r_199']

    df1.drop(columns = df1.columns[3:69],inplace = True)
    fail_d=[]
    for j,row in df1.iterrows():
        a=datetime.date(int(str(row['ds'])[0:4]),int(str(row['ds'])[4:6]),int(str(row['ds'])[6:8]))
        fail_day=30
        df2=file[file['disk_id']== row['disk_id']]
        if len(df2)!=0:
            day=[]
            for b in list(df2['failure_date'].unique()):
                day.append(a.__rsub__(datetime.datetime.strptime(b,"%Y-%m-%d").date()).days)
            if(min(day)<30 and min(day)>=0):
                fail_day=min(day)
        fail_d.append(fail_day)
    df1.insert(len(df1.columns),'failure_day',fail_d)
    new_df=pd.DataFrame(columns=df1.columns,index=[0])
    for i in range(0,31):
        df2=df1[df1['failure_day']==i]
        for j in df1.columns[4:]:
            df2[j]= df2[j].fillna(df2[j].median())
        new_df=new_df.append(df2)
    new_df.drop(new_df.index[0], inplace=True) 
    new_df.drop(new_df.columns[0],axis=1, inplace=True)
    new_df=new_df.reset_index(drop=True)
    train, valid= model_selection.train_test_split( new_df, test_size=0.3, random_state=42)
    train.to_csv(file_path1)
    valid.to_csv(file_path2)
