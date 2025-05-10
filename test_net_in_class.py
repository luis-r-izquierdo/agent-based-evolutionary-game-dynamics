#%%

the_net = [ [1,7], [1,8], [4,7], [7,3], [7,9], [9,5], [5,99], [5,7], [5,8], [99,10], [10,1], [2,7], [9, 2], [2,8], [2,4], [4,7], [4,9], [3,7], 
[99,8], [4,8], [8,10], [8,9]]
print( len(the_net))
# %%
degree=0
for i in the_net:
    if 99 in i :
        degree+=1
print(degree)
# %%
print(len([_ for _ in the_net if 99 in _]))
# %%
import networkx as nx
import matplotlib.pyplot as plt
#G = nx.Graph(the_net)
G=nx.lollipop_graph(10,7)
nx.draw(G, with_labels=True, font_weight='bold')
# %%
# Plot the degree distribution
degrees = [deg for _, deg in G.degree()]
print(degrees)
plt.figure()
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%