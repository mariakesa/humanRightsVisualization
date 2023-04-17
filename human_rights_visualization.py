import pandas as pd
import pandas as pd
import plotly.express as px
import seaborn as sns
import json

X_embedded = pd.read_csv("human_rights_articles_embedded.csv", header=0)

fig = px.scatter_3d(X_embedded, x="0", y="1", z="2",
                    color="classes",
                    size=[5] * len(X_embedded),
                    hover_data=["Article", "Title", "Text"],
                    opacity=0.8)

# Set the title and axes labels
fig.update_layout(title='Embeddings in 3D', scene=dict(
    xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Show the plot
fig.show()
