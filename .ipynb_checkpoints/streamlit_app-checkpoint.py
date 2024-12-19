import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/archive/vgsales.csv")
    df['Decade'] = (df['Year'] // 10) * 10  # Adding the Decade feature
    return df

df = load_data()

# Sidebar for Filters
st.sidebar.title("Filters")
selected_platform = st.sidebar.multiselect("Select Platforms", df['Platform'].unique())
selected_genre = st.sidebar.multiselect("Select Genres", df['Genre'].unique())

# Apply Filters
filtered_df = df.copy()
if selected_platform:
    filtered_df = filtered_df[filtered_df['Platform'].isin(selected_platform)]
if selected_genre:
    filtered_df = filtered_df[filtered_df['Genre'].isin(selected_genre)]

# Main Title
st.title("Video Game Sales Dashboard")

# Show Summary Statistics
st.header("Key Summary Statistics")
st.write(filtered_df.describe())

# Pair Plot Section
st.header("Pair Plot of Sales Data")
st.write("Explore relationships between regional sales.")
fig = sns.pairplot(filtered_df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']])
st.pyplot(fig)

# Correlation Heatmap
st.header("Correlation Heatmap")
st.write("Visualize correlations between numerical columns.")
plt.figure(figsize=(8, 6))
sns.heatmap(filtered_df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr(), annot=True, cmap='coolwarm')
st.pyplot(plt)

# Bar Chart for Global Sales by Genre
st.header("Global Sales by Genre")
sales_by_genre = filtered_df.groupby('Genre')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False)
st.bar_chart(sales_by_genre.set_index('Genre'))

# additional code 

# Pairplot for Global Sales and Regional Sales
import seaborn as sns
import matplotlib.pyplot as plt

# Create a pair plot for selected numerical features
sns.pairplot(df[['Global_Sales', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']])
plt.suptitle("Pairplot of Global and Regional Sales", y=1.02)

# Show plot
st.pyplot(plt)





