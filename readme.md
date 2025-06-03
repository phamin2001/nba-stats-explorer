# NBA Player Stats Explorer

A Streamlit web application for exploring and analyzing NBA player statistics through interactive data visualization and filtering.

![NBA Stats Explorer](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 🏀 Overview

This application performs web scraping of NBA player statistics from [Basketball Reference](https://www.basketball-reference.com/) and provides an interactive interface for data exploration, filtering, and visualization. Users can analyze player performance across different seasons, teams, and positions.

## ✨ Features

- **📅 Season Selection**: Choose from NBA seasons spanning 1950-2024
- **🏆 Team Filtering**: Filter players by specific NBA teams
- **🎯 Position Filtering**: Filter by player positions (PG, SG, SF, PF, C)
- **📊 Interactive Data Table**: View filtered player statistics in a clean, sortable format
- **📈 Correlation Analysis**: Generate correlation heatmaps to identify relationships between statistics
- **💾 Data Export**: Download filtered data as CSV files
- **🔄 Real-time Updates**: Dynamic filtering with instant results

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (required for web scraping)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/nba-stats-explorer.git
   cd nba-stats-explorer
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn
   ```

3. **Run the application**
   ```bash
   streamlit run mainapp.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📦 Dependencies

```python
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

## 🚀 Usage

### Basic Navigation

1. **Select Year**: Use the sidebar dropdown to choose an NBA season
2. **Filter Teams**: Select one or multiple teams from the multiselect dropdown
3. **Filter Positions**: Choose specific player positions to analyze
4. **View Data**: The main panel displays filtered player statistics
5. **Download Data**: Click the download link to export filtered data as CSV

### Advanced Features

#### Correlation Analysis
- Click the "Intercorrelation Heatmap" button to generate correlation matrices
- Toggle annotations on/off for better visualization of large datasets
- Analyze relationships between different statistical categories

#### Data Export
- Filtered data can be downloaded as CSV files
- Files are named with descriptive titles for easy organization

## 📊 Data Source

This application scrapes data from [Basketball Reference](https://www.basketball-reference.com/), specifically the per-game statistics tables. The data includes:

- **Player Information**: Name, Team, Position, Age
- **Game Statistics**: Games played, minutes, field goals, rebounds, assists
- **Advanced Metrics**: Shooting percentages, efficiency ratings
- **Season Coverage**: 1950-present (subject to data availability)

## 🔧 Technical Details

### Data Processing Pipeline

1. **Web Scraping**: Uses `pandas.read_html()` to extract NBA statistics tables
2. **Data Cleaning**: Removes duplicate header rows and handles missing values
3. **Type Conversion**: Ensures proper data types for analysis
4. **Filtering**: Applies user-selected filters in real-time

### Key Functions

- `load_data(year)`: Scrapes and cleans NBA data for specified year
- `filedownload(df)`: Creates downloadable CSV files using base64 encoding
- Interactive filtering using pandas boolean indexing

## 📁 Project Structure

```
nba-stats-explorer/
│
├── mainapp.py          # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Bug Reports**: Open an issue describing the problem
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with enhancements
4. **Documentation**: Improve or expand the documentation

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Limitations

- **Internet Dependency**: Requires active internet connection for data scraping
- **Website Changes**: Functionality depends on Basketball Reference's website structure
- **Rate Limiting**: Excessive requests may be blocked by the source website
- **Data Availability**: Historical data availability varies by year

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Basketball Reference** for providing comprehensive NBA statistics
- **Streamlit** for the amazing web app framework
- **pandas** for powerful data manipulation capabilities
- **freeCodeCamp** for the educational inspiration

## 📞 Contact

- **Author**: Amin Pahlavani
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/aminpahlavani/)

---

⭐ **Star this repository if you found it helpful!**