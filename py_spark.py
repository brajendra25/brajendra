# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 23:28:46 2019

@author: Anjali Brajendra
"""
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext

conf = SparkConf()
conf.set("spark.driver.memory","4g")
conf.set("spark.cores.max","2")
conf.setAppName("Brajendra spark")
sc = SparkContext.getOrCreate()
print("ok")
fileData = sc.textFile("1.txt")
rdd1 = fileData.filter(lambda x: "What" in x).count()
print(rdd1.collect())
