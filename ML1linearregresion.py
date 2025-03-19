import pandas as pd
# import numpy as np
# from sklearn import preprocessing import StandardScalar
from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_slipt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv('bangalore house price prediction OHE-data.csv')

x= df.drop('price',axis=1)
y=df['price']
print("shape of x=",x.shape)
print("shape of y=",y.shape)

# train_test_slipt(x,y,test_size=0.2)
# train_test_slipt(x,y,test_size=0.2,random_state=50)
# x_train, x_test, y_train, y_test = train_test_slipt(
#     x, y, test_size=0.2, random_state=50)

# print("the shape of x train is ",x_train.shape)
# print("the shape of x test is ", x_test.shape)
# print("the shape of y train is ",y_train.shape)
# print("the shape of y test is ", y_test.shape)

# # feature scaling
# sc = StandardScaler()
# sc.fit(x_train)
# x_train=sc.transform(x_train)
# x_test=sc.transform(x_test)


# # linear regression 
# lr = LinearRegression()
# lr.fit(x_train,x_test)
# lr.coef_
# lr.intersecpt_


# x_test[0,:]
# lr.predict([x_test[0, :]])

# lr.predict(x_test)
# y_test

# # checking the acurracy of ml model 
# lr.score(x_test,y_test)
