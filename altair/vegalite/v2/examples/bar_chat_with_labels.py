"""
Simple Bar Chart with Labels
============================
This example shows a basic horizontal bar chart with labels created with Altair.
"""

import altair as alt
import pandas as pd

data = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

bars = alt.Chart(data).mark_bar().encode(
    y='a',
    x='b'
)

text = alt.Chart(data).mark_text(align='left',baseline='middle',dx=3).encode(
    y='a',
    x='b', 
    text='b'
)

chart = bars + text