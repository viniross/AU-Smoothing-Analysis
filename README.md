<div align="right">
  🇺🇸 <strong>English</strong> | <a href="README.pt.md">🇧🇷 Português</a>
</div>

# Quantitative Analysis of Action Units in Facial Expressions: Real Humans vs. Virtual Avatars

This project presents a data analysis and visualization system to quantify the loss of intensity and variance in facial expressions transferred from real humans to virtual avatars. Using Action Unit (AU) data extracted with OpenFace, the system provides detailed statistical analysis to investigate the "Domain Gap" between original and digitally recreated expressions.

## 📜 Context

Transferring facial expressions to digital avatars often results in "smoothing." This can lead to less expressive animations and impact emotional perception, contributing to the *Uncanny Valley* effect. This project was developed to objectively measure this loss by comparing the dynamics of real actors' AUs with those of their corresponding avatars.

## 🏗️ Project Structure

The project is organized as follows:

```text
.
├── 0_Home.py                    # Streamlit application home page
├── data
│   ├── processed
│   │   └── dataset_consolidated.csv # Consolidated dataset after preprocessing
│   └── raw
│       ├── real_human          # Raw facial expression data from real humans
│       └── virtual_human       # Raw facial expression data from virtual avatars
├── pages
│   ├── 1_General_Statistics.py # Descriptive statistics analysis
│   ├── 2_Temporal_Analysis.py   # Analysis of AU temporal dynamics
│   ├── 3_Peak_Inspection.py     # Inspection of AU intensity peaks
│   ├── 4_Dispersion_Variance.py # Dispersion and variance analysis
│   └── 5_Severe_Smoothing.py   # Analysis of smoothing per AU
├── src
│   ├── analysis.py             # Functions for statistical analysis
│   ├── data_loader.py          # Script to load and consolidate data
│   ├── plots.py                # Functions for plot generation
│   └── utils.py                # Utility functions and constants
├── requirements.txt            # List of project dependencies
└── README.md                   # This file
```

## 📚 Libraries Used

The project utilizes the following Python libraries:

- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **scipy**: For statistical calculations, such as Pearson correlation and T-Test.
- **streamlit**: For building the interactive dashboard.
- **matplotlib** and **seaborn**: For data visualization and plot generation.

To install dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## 📊 Formulas and Analyses

The system implements the following metrics and statistical analyses:

### 1. Descriptive Statistics

For each Action Unit, the following descriptive statistics are calculated for both real human and virtual avatar data:

- **Median**: Represents the central value of AU intensity, serving as a measure of central tendency robust to outliers.
- **Variance**: Measures the dispersion of intensity values around the mean, indicating expression variability.
- **Maximum**: The peak intensity recorded for the AU.

### 2. Percentage Smoothing

Smoothing quantifies the loss of expression intensity when transferred to the avatar. The formula is:

$$
\text{Smoothing} = \frac{\text{Median}_{\text{Real}} - \text{Median}_{\text{Virtual}}}{\text{Median}_{\text{Real}}} \times 100
$$

A positive value indicates intensity loss (the avatar's expression is weaker), while a negative value suggests intensification.

### 3. Temporal Correlation (Pearson Coefficient)

To evaluate temporal synchrony between real human and avatar expressions, the Pearson correlation coefficient is calculated for the time series of each AU:

$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

Where:
- $x_i$ and $y_i$ are the AU intensities at frame $i$ for real and virtual data, respectively.
- $\bar{x}$ and $\bar{y}$ are the mean intensities.

A value close to 1 indicates a high positive correlation (the avatar matches the human's timing), while a value close to 0 indicates no correlation.

### 4. Statistical Significance Test (Independent T-Test)

To test whether the intensity difference between real and virtual expressions is statistically significant, an independent samples T-Test is applied. The null hypothesis ($H_0$) states that there is no difference between the mean intensities. A p-value under 0.05 indicates a statistically significant difference.

## 🚀 How to Run

1. Make sure Python and pip are installed.
2. Clone this repository:

   ```bash
   git clone [https://github.com/viniross/AU-Smoothing-Analysis.git](https://github.com/viniross/AU-Smoothing-Analysis.git)
   cd AU-Smoothing-Analysis
   ```

3. Install dependencies: `pip install -r requirements.txt`.
4. If raw data was updated, run the consolidation script: `python src/data_loader.py`.
5. To launch the application, run the following command in your terminal from the project root:

   ```bash
   streamlit run 0_Home.py
   ```

   The application will open in your default browser.
