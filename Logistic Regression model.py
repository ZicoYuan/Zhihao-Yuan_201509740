from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
clf = LogisticRegression(random_state=0).fit(train_data.astype(float),train_set['failure_day'].astype(float))  ##Define the model and fit it directly
lr_pred = clf.predict(valid_data.astype(float))

print(classification_report(np.asarray(lr_pred),np.asarray(valid_set['failure_day'], dtype = int)))

print(lr_pred)
