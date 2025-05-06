# Petrol Price Forecasting

This project is a time series analysis and prediction application for petrol prices. It uses machine learning models to analyze historical data and predict future trends. The application is built with Streamlit for an interactive user interface.

## Project Structure

- **`app.py`**: The main Streamlit application file.
- **`requirements.txt`**: Contains the dependencies required to run the project.
- **`data/`**: Includes the training and test datasets:
  - `train_data.csv`: Historical data for training the model.
  - `test_data.csv`: Data for testing and making predictions.
- **`models/`**: Contains the saved machine learning model:
  - `petrol_price_model.h5`: Pre-trained model for petrol price prediction.
- **`notebooks/`**: Jupyter Notebook for exploratory data analysis and model development:
  - `Petrol Price Forecasting.ipynb`

## Features

1. **Training Data Analysis**:
   - Displays summary statistics of the uploaded training data.
   - Visualizes the time series data with interactive plots.

2. **Prediction**:
   - Allows users to upload test data for predictions.
   - Displays predicted values and visualizes them alongside the test data.

3. **Interactive Interface**:
   - Built with Streamlit for easy data upload and visualization.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/petrol-price-forecasting.git
   cd petrol-price-forecasting
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Upload the training data (`train_data.csv`) to analyze it.
3. Upload the test data (`test_data.csv`) to make predictions.

## Data

- **Training Data**: Historical petrol price data for model training.
- **Test Data**: Data for evaluating the model's predictions.

## Model

The project uses a pre-trained model (`petrol_price_model.h5`) for predictions. The model was trained using the data in the `train_data.csv` file.

## Jupyter Notebook

The `notebooks/Petrol Price Forecasting.ipynb` file contains the exploratory data analysis and model training code.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.