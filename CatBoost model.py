cb_model = CatBoostRegressor(
                              learning_rate=0.01,
                              iterations=50000,
                              depth=5,
                              verbose = 100,
                              early_stopping_rounds=200,
                             
                              eval_metric='RMSE',
                              )
cb_model.fit(train_data, train_set['failure_day'],
             eval_set=(valid_data, valid_set['failure_day']),
             use_best_model=True,
             verbose=True)
cb_prediction=cb_model.predict(valid_data)
print(classification_report(a,np.asarray(valid_set['failure_day'], dtype = int)))


a=np.asarray(cb_prediction, dtype = int)
for i in range(0,len(a)):
    if a[i]<0:
        a[i]=0
    if a[i]>30:
        a[i]=30
print(classification_report(a,np.asarray(valid_set['failure_day'], dtype = int)))


print(cb_prediction)
print(np.asarray(cb_prediction, dtype = int))
