import streamlit as st
import pandas as pd
import plotly.express as px
import json

X_embedded = pd.read_csv("human_rights_articles_embedded.csv", header=0)

fig = px.scatter_3d(X_embedded, x="0", y="1", z="2",
                    color="classes",
                    size=[5] * len(X_embedded),
                    hover_data=["Article", "Title", "Text"],
                    opacity=0.8)

# Set the title and axes labels
fig.update_layout(title='Node2Vec Embeddings for European Court of Human Rights Article co-triggering graph in 3D', scene=dict(
    xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

fig.update_layout(height=1000, width=1000)

st.plotly_chart(fig, theme=None, use_container_width=False,
                height=1000, width=1000)
