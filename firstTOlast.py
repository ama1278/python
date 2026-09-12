colors = ["red", "green", "purple", "yellow", "crimson", "white", "black", "pink"]
for i in colors:
    colors[0],colors[-1]=colors[-1],colors[0]
    break
print(colors)