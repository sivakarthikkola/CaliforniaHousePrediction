# California House Price Prediction

## Overview
This project predicts house prices in California using machine learning techniques. A user-friendly web application built with Flask allows users to input property details and receive price predictions.

## Features
- **Accurate Predictions**: Utilizes a Random Forest Regressor for reliable house price estimates.
- **Interactive Web Interface**: Easy-to-use form for entering property details.
- **Docker Support**: Simplifies deployment and ensures consistency across environments.
- **Continuous Integration**: Automated testing and deployment with GitHub Actions.

## Software and Tools Requirements

1. [GitHub Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

## Getting Started

### Create a New Environment

```bash
conda create -p venv python==3.7 -y
```
### Installation Steps

Clone the Repository:

```bash
git clone https://github.com/yourusername/california-house-price-prediction.git
cd california-house-price-prediction
```

Install Dependencies:
```bash
pip install -r requirements.txt
```
### Download the Dataset: Place the California housing dataset in the /data directory.

Train the Model:
```bash
python src/train_model.py
```

Run the Application:
```bash
python src/app.py
```

### Usage.

Enter property details in the form.
Click "Predict Price" to see the estimated house price.
Contributing
We welcome contributions! Feel free to open issues or submit pull requests to improve this project.

### License.

This project is licensed under the Apache2.0 License.
### Acknowledgments

California Housing Dataset
Special thanks to all contributors and open-source communities!

### Contact
```
For questions or feedback, please reach out to sivakarthikkola3mail@gmail.com
```
