from sklearn import tree

#[height, weight, shoe_size]
x=[[181,80,44], [177,70,43],[160,60,38]]

#gender=[male/female]
y=['male','female','female']

#assigning Decision tree classifier model to the
#variable named clf
clf=tree.DecisionTreeClassifier()

clf= clf.fit(x,y)

prediction =clf.predict([[190,70,43]])

print (prediction)
