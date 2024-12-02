# Synthetic Data Generator

![Project Cover](/assets/sdg_main.png)

A powerful, flexible, and user-friendly tool for generating synthetic datasets for testing, analysis, or machine learning applications. With a clean and interactive interface built using **Streamlit**, users can define and generate data columns with various types, distributions, and constraints.

---

## 🎯 **Features**
- **Dynamic Table Creation**: Create and manage multiple tables seamlessly.
- **Column Generation**:
  - **Number Columns**: Generate numeric data with customizable ranges and steps.
  - **Date Columns**: Generate date ranges with adjustable frequencies.
  - **Text Columns**: Generate text data with support for custom distributions (count or ratio).
- **Customizable UI**:
  - Dark-themed sidebar with a clean and intuitive layout.
  - Expandable options for advanced column configurations.
- **Real-Time Updates**: Automatically refreshes as you add or modify data.
- **Export Functionality**:  Export tables in CSV  format.
  
---

## 🚀 **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/its-saran/synthetic_data_generator.git
   cd synthetic-data-generator
   ```
   
2. Set up a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
     ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run app.py
    ```

## 🛠️ **Usage**
1. **Launch the App**:
    - After running the app, it will open in your browser.
    - You can also access it at: [http://localhost:8501](http://localhost:8501).

2. **Create Tables**:
    - Use the **Create Table** section in the sidebar to create a new table.

3. **Add Columns**:
    - Select a table and use the provided controls to add columns with types like:
        - **Number**
        - **Date**
        - **Text**
    - Configure column properties such as:
        - Range
        - Frequency
        - Text distribution

4. **Visualize and Edit**:
    - View your generated data in real-time in the main app area.

5. **Upcoming Features**:
    - Export tables as CSV or Excel files.
    - Advanced data analysis and transformation tools.

## 📦 **Dependencies**

This project uses the following libraries and tools:

- **[Streamlit](https://streamlit.io/)**: Core framework for building the interactive web app.
- **[pandas](https://pandas.pydata.org/)**: For data manipulation and table operations.
- **[numpy](https://numpy.org/)**: For numerical computations and advanced data generation.
- **[streamlit-option-menu](https://pypi.org/project/streamlit-option-menu/)**: For creating dynamic sidebar navigation menus.
- **[streamlit-extras](https://pypi.org/project/streamlit-extras/)**: Enhancements for custom UI components.
