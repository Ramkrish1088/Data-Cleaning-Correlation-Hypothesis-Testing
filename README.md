**Data-Cleaning-Correlation-Hypothesis-Testing**
--------------------------------------------------

**📌 Project Overview**
-------------------------

This project focuses on preparing and analyzing the Heart Attack Prediction Dataset. 

The main objectives are:

    Cleaning the dataset to ensure accuracy and consistency.
    
    Identifying correlations between health parameters and heart attack risk.
    
    Conducting hypothesis testing, including t-tests, chi-square tests, and ANOVA, to check for statistically significant relationships.
    
    This process supports better decision-making and prepares the dataset for further predictive modeling.

**🧹 Step 1: Data Cleaning**
-------------------------------

Data cleaning is the foundation of reliable analysis. In this project, the following steps are carried out:

**Handling Missing Values:** Detect and address gaps in the dataset. This can be done by removing records with excessive missing values or filling them using statistical measures such as mean, median, or mode.

**Correcting Data Types:** Ensure each column has the correct data type (e.g., numerical, categorical) to avoid errors in analysis.

**Removing Duplicates:** Eliminate duplicate records to prevent bias in results.

**Standardizing Data:** Normalize or standardize numerical values where necessary for better comparability.

**📊 Step 2: Correlation Analysis**
---------------------------------------

Correlation analysis helps to identify how variables are related to each other. For example, it can show whether cholesterol, age, or blood pressure levels are strongly associated with the risk of a heart attack.

**Correlation Matrix:** A summary that shows the strength of relationships between variables.

**Heatmap Visualization:** A graphical representation of correlations, making it easier to identify which factors are most influential.

This step is crucial for feature selection, as highly correlated variables with the target can provide meaningful insights.

**🧪 Step 3: Hypothesis Testing**
------------------------------------

Hypothesis testing is used to verify whether observed patterns in the data are statistically significant. It involves:

Defining Hypotheses:

**Null Hypothesis (H0):** There is no relationship or no difference between groups.

**Alternative Hypothesis (H1):** There is a significant relationship or difference.

Types of Tests Used:

**t-Test:** Compares the means of two groups (e.g., cholesterol levels between patients with and without heart attacks).

**Chi-Square Test:** Checks for associations between categorical variables (e.g., gender and heart attack occurrence).

**ANOVA (Analysis of Variance):** Compares the means across more than two groups. For example, comparing average cholesterol levels across multiple age groups to see if the differences are statistically significant.

A **p-value** is calculated in each test:

If p < 0.05, the null hypothesis is rejected, suggesting a significant difference or association.

If p ≥ 0.05, the null hypothesis cannot be rejected, suggesting no significant difference or association.

**✅ Summary**
------------------

Data Cleaning ensures the dataset is accurate, consistent, and free from errors.

Correlation Analysis highlights the strength of relationships between health parameters and heart attack risk.

Hypothesis Testing (t-test, chi-square test, and ANOVA) validates whether observed differences or associations are meaningful or simply due to chance.

By completing these steps, the dataset becomes ready for deeper statistical analysis and predictive modeling, ultimately supporting better insights into heart attack risks.
