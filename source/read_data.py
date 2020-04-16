#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:58:06 2020

@author: zackkingbackup
"""

import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns

df1418 = pd.read_csv("../data/2014To2018Drafts-refined.csv")
df13 = pd.read_csv("../data/players_2013-12-12.csv")
dfm = pd.read_csv("../data/Madden20ratings.csv")

dftest = dfm.merge(df1418, left_on='Name', right_on='Player', how='inner')
#dftest[['Name','ovr rating','Rnd','Pick']]

# Get rid of duplicates by keeping higher overall player
dftest.sort_values(by=['ovr rating'], inplace=True, ascending=False)
dftest = dftest.drop_duplicates(subset=['Name'])

# Couple quick insights for players drafted 2014 and after
# 1. Average overall for first rounders picks 1-16
# 2. Average overall for first rounders picks 17-32
df116 = dftest[(dftest.Rnd == 1) & (dftest.Pick < 17)]
df1732 = dftest[(dftest.Rnd == 1) & (dftest.Pick > 16)]

bins=15
pyplot.hist(df116['ovr rating'], bins, alpha=0.5, label='early first')
pyplot.hist(df1732['ovr rating'], bins, alpha=0.5, label='late first')
pyplot.legend(loc='upper right')
pyplot.title("First Round Pick Overall (2014-2018)")
pyplot.annotate("Early 1st Avg: {}".format(str(df116['ovr rating'].mean())[:5]), xy=(56,14))
pyplot.annotate("Late 1st Avg: {}".format(str(df1732['ovr rating'].mean())[:5]), xy=(56,10))
pyplot.show()

df1 = dftest[dftest.Rnd == 1]
#pyplot.scatter(list(df1.Pick), list(df1['ovr rating']))
#pyplot.xlabel("First round draft slot")
#pyplot.ylabel("Madden 20 Overall Rating")
#pyplot.title("Draft Pick v. Overall")
#pyplot.show()
sns.regplot(list(df1.Pick), list(df1['ovr rating']),
            x_jitter=.1, y_jitter=.1)
pyplot.xlabel("First round draft slot")
pyplot.ylabel("Madden 20 Overall Rating")
pyplot.title("Draft Pick v. Overall")
pyplot.show()
