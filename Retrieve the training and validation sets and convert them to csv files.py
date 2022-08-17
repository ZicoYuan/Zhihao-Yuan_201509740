train_set=pd.read_csv('1-12_ssd_train.csv')
valid_set=pd.read_csv('1-12_ssd_valid.csv')
train_set.drop(train_set.columns[0],axis=1, inplace=True)
valid_set.drop(valid_set.columns[0],axis=1, inplace=True)
train_data=train_set.iloc[:,1:12]
valid_data=valid_set.iloc[:,1:12]
train_data=np.log(abs(train_data)+1)
valid_data=np.log(abs(valid_data)+1)
