# Bank Customer Churn Prediction

## Project Overview
A machine learning project that predicts customer churn in a banking dataset. The goal is identifying customers at risk of leaving the bank and to support proactive retention strategies.

<!-- TO-DO: Add URL for dataset  -->
The data used for this is: [bank customer dataset](URL).

### Business Problem
Customer churn reduces long-term revenue and customer lifetime value. Without predictive analytics, banks often react after customers have already churned, making retention efforts costly and ineffective. 

### Business Questions
1. Which customers are most likely to churn?
2. Which customer characteristics are associated with churn?
3. Can we accurately predict churn using machine learning?
4. Which model performs best for churn prediction?
5. How can the bank use these predictions to reduce churn?

#### Value Proposition
This project provides a machine learning model that predicts which customers are likely to leave, allowing the bank to intervene early. 
**Business value created**
- Reduced customer churn through early identification of at-risk customers
- Increased customer lifetime value
- More efficient marketing and retention campaigns
- Improved overall customer experience


<!-- TO-DO: check with dataset -->
### Dataset
The dataset contains information about bank customers including demographics, account characteristics, and financial behaviour.
- has exited
- age
- tenure
- balance
- number of products
- has credit card
- credit score
- geography
- gender
- estimated salary

Exited
1 = customer churned
0 = customer retained

<!-- TO-DO: if needed adjust to actual project work flow -->
### Project Workflow
1. Business understanding
2. Exploratory data analysis
3. Data preparation
4. Model training
5. Model evaluation
6. Business interpretation


<!-- TO-DO: Adjust with actual findings of EDA -->
### Exploratory Data Analysis (EDA)
Key insights from the data exploration:

- Customers with higher balances showed a higher probability of churn.
- Older customers were more likely to leave the bank.
- Customers with fewer products were more likely to churn.
- Geography showed differences in churn behavior.

These insights helped guide feature selection and model development.

<!-- TO-DO: adjust with actual model approach / models used -->
### Modeling Approach / Models Used
- Logistic Regression
- Random Forest
- Gradient Boosting

<!-- TO-DO: adjust with actual evaluation metrics used -->
### Evaluation Metrics
- ROC-AUC
- Precision
- Recall 
- F1-score


<!-- TO-DO: adjust with actual numbers -->
## Key Results

| Model                | ROC-AUC | Precision | Recall | F1 Score |
|----------------------|--------|-----------|--------|----------|
| Logistic Regression  | 0.79   | 0.68      | 0.60   | 0.64     |
| Random Forest        | 0.85   | 0.73      | 0.70   | 0.71     |
| Gradient Boosting    | 0.87   | 0.76      | 0.74   | 0.75     |

<!-- TO-DO: adjust with actual best performing model-->
**Best Performing Model:** Gradient Boosting

Gradient Boosting achieved the highest ROC-AUC and F1 score, indicating the best overall performance in identifying churned customers while maintaining balanced precision and recall.


<!-- TO-DO: adjust with actual insights after analysis-->
### Business Insights

The analysis revealed several key drivers of customer churn:

- Customers with fewer banking products were more likely to churn.
- Older customers showed higher churn rates.
- Customers with higher balances had increased churn probability.
- Churn behaviour differed across geographic regions.

These findings suggest that customer engagement and product usage are important factors in customer retention.

### Business Impact
The model allows the bank to:
- Identify customers at high risk of churn
- Target retention campaigns more effectively
- Reduce customer churn
- Increase customer lifetime value


<!-- TO-DO: adjust with actual findings, at least one data-driven argument -->
### Business Recommendations

Based on the model predictions, the bank can implement several strategies:

- Target high-risk customers with retention campaigns
- Offer loyalty benefits to customers with high balances
- Increase engagement with customers who have few products
- Provide personalized offers based on churn risk scores
- Encourage customers to adopt additional banking products, as customers with fewer products showed higher churn probability.


## Project Structure
```
bank-churn-project/
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   └── churn_analysis.ipynb
│
├── src
│   ├── train.py
│   └── predict.py
│
├── models
├── requirements.txt
└── README.md
```

<!-- TO-DO: check which ones match / adjust, add ,remove otherwise -->
### Future Improvements

- Hyperparameter tuning to further improve model performance
- Testing additional models such as XGBoost or LightGBM
- Feature engineering to capture more complex customer behaviour
- Model deployment as an API for real-time churn prediction
---



## Set up your Environment

### **`macOS`** type the following commands : 

- For installing the virtual environment you can either use the [Makefile](Makefile) and run `make setup` or install it manually with the following commands:

     ```BASH
    make setup
    ```
    After that active your environment by following commands:
    ```BASH
    source .venv/bin/activate
    ```
Or ....
- Install the virtual environment and the required packages by following commands:

  > NOTE: for macOS with **silicon** chips (other than intel)
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements_silicon.txt
    ```
  > NOTE: for macOS with **intel** chips
  ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-bash` CLI :
  
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:
    ```Bash
    python.exe -m pip install --upgrade pip
    ```


   
## Usage

In order to train the model and store test data in the data folder and the model in models run:

**`Note`**: Make sure your environment is activated.

```bash
python example_files/train.py  
```

In order to test that predict works on a test set you created run:


<!-- TO-DO: renaming to eg models/churn_model.sav -->
```bash
python example_files/predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```

## Limitations

Development libraries are part of the production environment, normally these would be separate as the production code should be as slim as possible.

<!-- TO-DO: Adjust  -->

- The dataset is relatively small and may not fully represent real banking customers.
- Some potentially important variables such as customer satisfaction or transaction behaviour are not available.
- Model performance may vary when applied to different banking populations.


---

## Handling Merge Conflicts in Jupyter Notebooks

When working in teams, `.ipynb` files can cause messy merge conflicts because they’re JSON-based.  
We use **nbdime** to make this easy.

### Setup (run once)
```bash
nbdime config-git --enable
```

### When a conflict happens
```bash
nbdime mergetool
```

A web interface will open showing both notebook versions side by side.
Choose what to keep, save and close tool, then:
```bash
git add your_notebook.ipynb
git commit -m "Resolved notebook conflict"
```
That’s it — clean merges for notebooks!