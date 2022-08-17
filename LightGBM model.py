lgb_train = lgb.Dataset(train_data, train_set['failure_day'])  
lgb_eval = lgb.Dataset(valid_data, valid_set['failure_day'], reference=lgb_train)
params = {  
'task': 'train',  
'boosting_type': 'gbdt', 

'objective' : 'mse',
'learning_rate': 0.01,
'n_estimators' : 1000,
'num_leaves': 75,
'max_depth' : 5,
'subsample' : 0.9,
'colsample_bytree' : 0.7,
'random_state' : 3, 
}  

my_model = lgb.train(params, lgb_train, num_boost_round=1000, valid_sets=lgb_eval, early_stopping_rounds=20)  
lgb_predictions = my_model.predict(valid_data, num_iteration=my_model.best_iteration)  
print(lgb_predictions)
print(np.asarray(lgb_predictions, dtype = int))
print(classification_report(np.asarray(lgb_predictions, dtype = int),np.asarray(valid_set['failure_day'], dtype = int)))
