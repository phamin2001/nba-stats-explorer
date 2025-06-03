# NBA Player Stats Explorer - A Streamlit web application for exploring NBA player statistics
# This application performs web scraping of NBA player stats and provides interactive data visualization

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

st.title('NBA Player Stats Explorer')
st.markdown("""
This app performs simple web scraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data Source:** [Basketball Reference](https://www.basketball-reference.com/)             
            """)

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2025))))

# Web scraping of NBA player stats
def load_data(year):
    """
    Load NBA player statistics data for a given year from basketball-reference.com.
    
    This function scrapes NBA per-game statistics from basketball-reference.com,
    cleans the data by removing duplicate headers and unnecessary columns,
    and fills missing values.
    
    Args:
        year (int): The NBA season year to retrieve data for (e.g., 2021 for 2020-21 season)
    
    Returns:
        pandas.DataFrame: A cleaned DataFrame containing NBA player per-game statistics
                         with the following modifications:
                         - Duplicate header rows removed
                         - Missing values filled with 'N/A'
                         - 'Rk' (rank) column removed
    
    Example:
        >>> df = load_data(2021)
        >>> print(df.head())
    
    Note:
        Requires internet connection to access basketball-reference.com
        The function expects the website structure to remain consistent
    """
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url,header = 0)
    df = html[0]
    # Delete repeating headers in content if the 'Age' column exists
    if 'Age' in df.columns:
        raw = df.drop(df[df.Age == 'Age'].index)
    else:
        raw = df
    raw = raw.fillna('N/A')
    raw = raw.drop(['Rk'], axis=1)
    return raw
playersstats = load_data(selected_year)
# st.write((playersstats['Team'].unique()))

# Sidebar Team Selection
sorted_unique_team = sorted(playersstats['Team'].unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar Position Selection
unique_pos = sorted(playersstats.Pos.unique())
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

st.header('Display Player Stats of Selected Teams(s)')
df_selected_team = playersstats[(playersstats.Team.isin(selected_team)) & 
                                (playersstats.Pos.isin(selected_pos))]
st.write('Data Dimesion: ' + str(df_selected_team.shape[0]) + ' rows and ' + 
         str(df_selected_team.shape[1]))
st.dataframe(df_selected_team)

# Download NBA player stats data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    
    # Add a checkbox to toggle annotations
    show_annotations = st.checkbox('Show annotations on heatmap (may slow down rendering for large datasets)', value=True)
    
    # Create a copy and exclude non-numeric columns
    df_numeric = df_selected_team.copy()
    
    # Remove obviously non-numeric columns
    columns_to_exclude = ['Player', 'Pos', 'Team']  # Add other text columns
    for col in columns_to_exclude:
        if col in df_numeric.columns:
            df_numeric = df_numeric.drop(col, axis=1)
    
    # Convert remaining columns to numeric, replacing 'N/A' or invalid entries with NaN
    st.write("Note: Non-numeric values in numeric columns are replaced with NaN during conversion.")
    for col in df_numeric.columns:
        df_numeric[col] = pd.to_numeric(df_numeric[col], errors='coerce')
    # Drop columns that are all NaN or have too few valid values
    df_numeric = df_numeric.dropna(axis=1, how='all')
    
    if df_numeric.empty:
        st.error("No numeric data available for correlation analysis after cleaning")
    elif df_numeric.shape[1] < 2:
        st.error("Not enough numeric columns for correlation analysis")
    if df_numeric.shape[1] < 2:
        st.error("Not enough numeric data for correlation analysis")
    else:
        corr = df_numeric.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, mask=mask, vmax=1, square=True, 
                   annot=show_annotations, cmap='coolwarm', center=0,
                   fmt='.2f', ax=ax)
        plt.title(f'NBA Player Stats Correlation Matrix ({selected_year})')
        st.pyplot(fig)