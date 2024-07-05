# Python Libraries

NumPy, Pandas, and MatplotLib

## Files Included

1. `NumPy.py`
2. `Pandas.py`
3. `Matplotlib_covid19.py`
4. `WHO-COVID-19-global-data.csv`

### `NumPy.py`

Demonstrates basic operations with NumPy arrays including:
- Creation
- Reshaping
- Indexing
- Slicing
- Stacking
- Sorting
- Using universal functions (ufuncs)

### `Pandas.py`

Illustrates Pandas Series and DataFrame operations:
- Creating Series and DataFrames
- Indexing and slicing using `loc` and `iloc`
- Handling NaN values with `fillna` and `dropna`
- Adding and removing columns
- Conditional indexing and filtering
- Displaying data using Pandas data structures

### `Matplotlib_covid19.py`

Uses Matplotlib to visualize COVID-19 data:
- Reads data from `WHO-COVID-19-global-data.csv`
- Cleans and preprocesses data (handling missing values, converting date formats)
- Plots global COVID-19 trends including confirmed cases, recoveries, and deaths over time

## Installation

To run these scripts, ensure you have Python installed along with the following libraries:
1. NumPy
2. Pandas
3. Matplotlib
4. scikit-learn (for SimpleImputer in `Matplotlib_covid19.py`)

You can install these libraries using pip with the following command:
```bash
pip install numpy pandas matplotlib scikit-learn
```

Usage:
Each script demonstrates specific functionalities related to its respective library. You can run them individually to see the output and understand how to utilize these libraries for data manipulation, visualization, and analysis.
