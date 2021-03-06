import nbformat as nbf

nb = nbf.v4.new_notebook()

text = """\
# Lowcode model generator
Generated recommneder system from model."""

code = """\
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
##TODO Generating dataset





dataset=pd.read_csv('Social_Network_Ads.csv')
#X = dataset.iloc[:,:-1].values
#y = dataset.iloc[:, -1].values

	#if len(dataset.columns) < 2:
	#    print('The dataset must have at least two columns')
	#	return None, None
	#else:
if 'Label' in dataset.columns:
	y = dataset["Label"]
else:
	print("Cannot find column for labels. Using the last one as default")
	y = dataset.iloc[:, -1].values
X = dataset.iloc[:, :-1].values






from sklearn.neural_network import MLPClassifier	
solver='ADAM'
alpha=0.0
random_state=0		


clf = MLPClassifier(solver=solver, alpha=alpha,hidden_layer_sizes=hidden_layers, random_state=random_state)

clf.fit(X_train, y_split)
y_pred = clf.predict(X_test)






n_splits=0
prec_all = 0
acc_all = 0
rec_all = 0
f1_all = 0
from sklearn.model_selection import  KFold
kf = KFold(n_splits = n_splits)
for  train, test in kf.split(X):
	X_split, X_test, y_split, y_test = X[train],X[test], y[train], y[test]
	
		
	
	
	from sklearn.neural_network import MLPClassifier	
	solver='ADAM'
	alpha=0.0
	random_state=0		
	
	
	clf = MLPClassifier(solver=solver, alpha=alpha,hidden_layer_sizes=hidden_layers, random_state=random_state)
	
	clf.fit(X_train, y_split)
	y_pred = clf.predict(X_test)
	
	
	
	
print(prec_all)
print(rec_all)
print(f1_all)






"""
nb["cells"] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code) ]

nbf.write(nb, 'Aurora.ipynb')
