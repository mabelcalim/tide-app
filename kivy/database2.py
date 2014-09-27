import mysql.connector
from mysql.connector import errorcode
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
from pylab import *
import json
from kivy.cache import Cache
from kivy.storage.redisstore import RedisStore


def database():
        """ open/read Redelitoral's database
            sea level's plot from database
        """
        # communicate with Redelitoral database
        try:
        	con=mysql.connector.connect(host='54.204.23.126', port=3306, user='mabel', passwd='m@r3gr2af0', db='maregrafo')
        	cur = con.cursor()
        	cur.execute("SELECT * FROM medida")
        	rows = cur.fetchall()
        except mysql.connector.Error as err:
  		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    		   print("Something is wrong with your user name or password")
  		elif err.errno == errorcode.ER_BAD_DB_ERROR:
    		   print("Database does not exists")
  		else:
                   print(err)
	else:
  		con.close()
        # saving data in a list  
        data = []
        for r in rows:
                data.append(r)
        #select only last 3 days data
        sea_level,sea_mean,min10 =[],[],432
        sea_level = [data[e][3] for e in range(data[-1][0]- min10+1,data[-1][0])]
        sea_mean =np.mean([data[e][3] for e in range(len(data))])
        # date for axis
        tlast = data[-1][2].strftime('%m/%d/%Y')
        tmean = data[-min10/2][2].strftime('%m/%d/%Y')
        t0 = data[-min10+1][2].strftime('%m/%d/%Y')
        n0,nlast,nmean = 0,min10+1,min10/2
        # plots  
        plot_mean= [sea_mean]* (min10+1)
        fig = plt.figure(figsize=(5,4),dpi=200)
        ax = fig.add_subplot(111)
        ax.plot(sea_level,'bo')
        ax.plot(plot_mean,'b--')
        ax.set_ylim([0.5, 2.0])
        ax.set_xlim([0,min10+2])
        ax.set_xticks([n0,nmean,nlast])
        ax.set_xticklabels([t0,tmean,tlast])
        # annotate min and max values from the last 3 days 
        id_max=np.where(sea_level==np.max(sea_level))[0][0]
        id_min=np.where(sea_level==np.min(sea_level))[0][0]
        plt.text(id_max-5,sea_level[id_max]+0.07, '%s'%sea_level[id_max],fontsize=10)
        plt.text(id_max-5,sea_level[id_max]+0.14, 'max',fontsize=10)
        plt.text(id_min-5,sea_level[id_min]-0.07, '%s'%sea_level[id_min],fontsize=10)
        plt.text(id_min-5,sea_level[id_min]-0.14, 'min',fontsize=10)
        plt.text(min10-50,sea_mean-0.07, 'mean',fontsize=10)
        # title and legend
        ax.set_ylabel('Meters',fontsize=10)
        ax.set_xlabel('Date',fontsize=10)
        plt.title('Sea level for the last 3 days')  
        savefig('fig_data.png', bbox_inches='tight')
        Cache.register('fig_data.png', limit=10, timeout=5) 
        return
database()
