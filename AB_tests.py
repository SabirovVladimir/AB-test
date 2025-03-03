# here I wnnt to investigate A/B tetsts mechanisms and how to implement them in python

'''
 Accuracy is the proportion of correct answers in the test. 
 Accuracy does not account for the cost of errors. 
 False positive and false negative results equally reduce accuracy. 
 Accuracy is not applicable in cases of an imbalance between positive and negative results. 
 False positive and false negative cases should be analyzed separately.

 False Positive (FP) - incorrect identification of a disease in a healthy person (Type I error in statistics). %FP (FPRate) = FP / Negative_real. 
 False Negative (FN) - incorrect identification of a sick person as healthy (Type II error in statistics). %FN (FNRate) = FN / Positive_real. 
 True Positive (TP) TPRate = TP / Positive_real. Sensitivity metric. Accuracy for positive results. 1 - FNRate.
 True Negative (TN) TNRate = TN / Negative_real. Specificity metric. Accuracy for negative results. 1 - FPRate.

 https://en.wikipedia.org/wiki/Receiver_operating_characteristic more about identifications 
 https://en.wikipedia.org/wiki/Confusion_matrix - about confusion matrix
'''

# Importing libraries
import numpy as np
import pandas as pd



