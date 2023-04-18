# humanRightsVisualization

Update: the visualization is currently deployed on Streamlit. You can view it here https://mariakesa-humanrightsvisualization-app-p8ba4o.streamlit.app/

Visualization of processed data from European Court of Human Rights API. Currently doesn't include the processing steps, but these will be added soon.

Basically, I made a multi-graph from Articles that were triggered in court decisions (i.e. draw an edge between nodes-Articles if they were triggered together
in a court decision). I then used Node2Vect obtain 10 dimensional embeddings for those European Convention of Human Rights articles and lowered their dimensionality 
further using PCA. The result is this visualization, which conveniently includes interactivity so that you can read the Articles as you browse the nodes.

So basically this plot visualizes the similarity of connectivity in the court decision - Article graph. Articles that are connected to other Articles
in similar patterns are closer together in the visualized space. The interesting research question is what do the PCA dimensions correspond to, because
it is apparent that different classes of Articles vary along different dimensions.

Install poetry here https://python-poetry.org/docs/ To run the visualization clone the repository, cd into it, run "poetry install" and then "poetry run python human_rights_visualization.py" Of course you can also just pip install pandas and plotly and simply running "python human_rights_visualization.py" should work:-) But I'm a fan of poetry!

![alt text](https://github.com/mariakesa/humanRightsVisualization/blob/main/humrightsviz.png)
