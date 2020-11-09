#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
post_season = pd.read_csv("../Data/nba_2020_shooting_playoffs.csv", index_col=0)
regular_season = pd.read_csv("../Data/nba_2020_shooting.csv", index_col=0)
#COMPARADOR %FG, 2P%, 3P% regular vs post season
#OPCIÓN 1
def plot_regular_season(choice):
    Index_label_r = regular_season[regular_season["Player"] == choice].index
    row_r = regular_season.index[Index_label_r].values
    fg_r = (regular_season["FG%"][row_r[0]])
    fg2_r =(regular_season["2P FG%"][row_r[0]])
    fg3_r = (regular_season["3P FG%"][row_r[0]])
    names_regular = ["FG%", "2P FG%", "3P FG%"]
    values_regular = [fg_r, fg2_r, fg3_r]
    axes = plt.gca()
    plt.scatter(x = names_regular, y = values_regular, alpha=0.5, color="r", label = "Regular Season")

def plot_post_season(choice):
    Index_label_p = post_season[post_season["Name"] == choice].index
    row_p = post_season.index[Index_label_p].values
    fg_p = (post_season["FG%"][row_p[0]])
    fg2_p =(post_season["2P FG%"][row_p[0]])
    fg3_p = (post_season["3P FG%"][row_p[0]])
    names_post = ["FG%", "2P FG%", "3P FG%"]
    values_post = [fg_p, fg2_p, fg3_p]
    axes = plt.gca()
    plt.scatter(x = names_post, y = values_post, alpha=0.5, color="b", label = "Post Season")

def comparison_player(choice):
    plot1 = plot_regular_season(choice)
    plot2 = plot_post_season(choice)
    plt.legend()
    plt.title(choice)

#OPCIÓN 2
def plot_regular_season1(choice):
    Index_label_r = regular_season[regular_season["Player"] == choice].index
    row_r = regular_season.index[Index_label_r].values
    fg_r = (regular_season["FG%"][row_r[0]])
    fg2_r =(regular_season["2P FG%"][row_r[0]])
    fg3_r = (regular_season["3P FG%"][row_r[0]])
    names_regular = ["FG%", "2P FG%", "3P FG%"]
    values_regular = [fg_r, fg2_r, fg3_r]
    axes = plt.gca()
    axes.set_ylim((0, 1))
    plt.bar(x = names_regular, height = values_regular, alpha=0.5, color="c", label = "Regular Season")

def plot_post_season1(choice):
    Index_label_p = post_season[post_season["Name"] == choice].index
    row_p = post_season.index[Index_label_p].values
    fg_p = (post_season["FG%"][row_p[0]])
    fg2_p =(post_season["2P FG%"][row_p[0]])
    fg3_p = (post_season["3P FG%"][row_p[0]])
    names_post = ["FG%", "2P FG%", "3P FG%"]
    values_post = [fg_p, fg2_p, fg3_p]
    axes = plt.gca()
    axes.set_ylim((0, 1))
    plt.bar(x = names_post, height = values_post, alpha=0.5, color="g", label = "Post Season")

def comparison_player1(choice):
    plot1 = plot_regular_season1(choice)
    plot2 = plot_post_season1(choice) 
    plt.title(choice)

#OPCIÓN 3
def comparison_player2(choice):
    Index_label_p = post_season[post_season["Name"] == choice].index
    row_p = post_season.index[Index_label_p].values
    fg_p = (post_season["FG%"][row_p[0]])
    fg2_p =(post_season["2P FG%"][row_p[0]])
    fg3_p = (post_season["3P FG%"][row_p[0]])
    Index_label_r = regular_season[regular_season["Player"] == choice].index
    row_r = regular_season.index[Index_label_r].values
    fg_r = (regular_season["FG%"][row_r[0]])
    fg2_r =(regular_season["2P FG%"][row_r[0]])
    fg3_r = (regular_season["3P FG%"][row_r[0]])

    # set width of bar 
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8)) 

    # set height of bar 
    data1 = [fg_r, fg2_r, fg3_r]
    data2 = [fg_p, fg2_p, fg3_p]

    # Set position of bar on X axis 
    br1 = np.arange(len(data1)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2] 

    # Make the plot 
    plt.bar(br1, data1, color ='r', width = barWidth, 
            edgecolor ='grey', label ='Regular Season') 
    plt.bar(br2, data2, color ='g', width = barWidth, 
            edgecolor ='grey', label ='Post Season')
    plt.legend()

    # Adding Xticks  
    plt.xlabel('Type of Shot', fontweight ='bold') 
    plt.ylabel("Shooting%", fontweight ='bold') 
    plt.xticks([r + barWidth for r in range(len(data1))], 
               ['FG%', '2P FG%', '3P FG%']) 

#COMPARADAOR ESTADÍSTICAS 2 JUGADORES TEMPORADA REGULAR
def comparison_two_player_regular (player1, player2):
    #1er Jugador
    Index_label_r1 = regular_season[regular_season["Player"] == player1].index
    row_r1 = regular_season.index[Index_label_r1].values
    fg_r1 = (regular_season["FG%"][row_r1[0]])
    fg2_r1 =(regular_season["2P FG%"][row_r1[0]])
    fg3_r1 = (regular_season["3P FG%"][row_r1[0]])
    #2do Jugador
    Index_label_r2 = regular_season[regular_season["Player"] == player2].index
    row_r2 = regular_season.index[Index_label_r2].values
    fg_r2 = (regular_season["FG%"][row_r2[0]])
    fg2_r2 =(regular_season["2P FG%"][row_r2[0]])
    fg3_r2 = (regular_season["3P FG%"][row_r2[0]])
    # set width of bar 
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8)) 
    # set height of bar 
    data1 = [fg_r1, fg2_r1, fg3_r1]
    data2 = [fg_r2, fg2_r2, fg3_r2]
        # Set position of bar on X axis 
    br1 = np.arange(len(data1)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2] 

    # Make the plot 
    plt.bar(br1, data1, color ='r', width = barWidth, 
            edgecolor ='grey', label =player1) 
    plt.bar(br2, data2, color ='g', width = barWidth, 
            edgecolor ='grey', label =player2)
    plt.legend()

    # Adding Xticks  
    plt.xlabel('Type of Shot', fontweight ='bold') 
    plt.ylabel("Shooting%", fontweight ='bold') 
    plt.xticks([r + barWidth for r in range(len(data1))], 
               ['FG%', '2P FG%', '3P FG%']) 

#COMPARADAOR ESTADÍSTICAS 2 JUGADORES PLAYOFFS   
def comparison_two_player_post (player1, player2):
    #1er Jugador
    Index_label_p1 = post_season[post_season["Name"] == player1].index
    row_p1 = post_season.index[Index_label_p1].values
    fg_p1 = (post_season["FG%"][row_p1[0]])
    fg2_p1 =(post_season["2P FG%"][row_p1[0]])
    fg3_p1 = (post_season["3P FG%"][row_p1[0]])
    #2do Jugador
    Index_label_p2 = post_season[post_season["Name"] == player2].index
    row_p2 = post_season.index[Index_label_p2].values
    fg_p2 = (post_season["FG%"][row_p2[0]])
    fg2_p2 =(post_season["2P FG%"][row_p2[0]])
    fg3_p2 = (post_season["3P FG%"][row_p2[0]])
    # set width of bar 
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8)) 
    # set height of bar 
    data1 = [fg_p1, fg2_p1, fg3_p1]
    data2 = [fg_p2, fg2_p2, fg3_p2]
        # Set position of bar on X axis 
    br1 = np.arange(len(data1)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2] 

    # Make the plot 
    plt.bar(br1, data1, color ='r', width = barWidth, 
            edgecolor ='grey', label =player1) 
    plt.bar(br2, data2, color ='g', width = barWidth, 
            edgecolor ='grey', label =player2)
    plt.legend()

    # Adding Xticks  
    plt.xlabel('Type of Shot', fontweight ='bold') 
    plt.ylabel("Shooting%", fontweight ='bold') 
    plt.xticks([r + barWidth for r in range(len(data1))], 
               ['FG%', '2P FG%', '3P FG%']) 