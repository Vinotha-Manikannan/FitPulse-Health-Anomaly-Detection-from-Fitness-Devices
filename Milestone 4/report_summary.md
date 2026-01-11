FitPulse Health Anomaly Detection – Milestone 4 Report

--Objective

1.The objective of this milestone is to develop an interactive Health Anomaly Detection Dashboard using Streamlit in Google Colaboratory. The dashboard enables users to:

2.Upload fitness data (CSV/JSON) from wearable devices.

3.Detect anomalies in health metrics such as Heart Rate, Steps, and Sleep Duration.

4.Visualize trends and abnormal patterns interactively.

5.Generate summary statistics and downloadable reports for further analysis.

--Dashboard Workflow

1.File Upload
- Users upload a CSV or JSON file containing fitness data with timestamped records.

2.Data Preprocessing

- Column names are standardized.

- Timestamps are auto-parsed and sorted.

- Invalid timestamps are removed.

3.Anomaly Detection

- IsolationForest algorithm is applied to each numeric metric (Heart Rate, Steps, Sleep Duration).

- Metrics are scaled using StandardScaler to improve anomaly detection accuracy.

- A fixed contamination rate of 5% ensures meaningful anomaly identification.

4.Interactive Controls

- Users can select the metric to visualize.

- Date range filtering allows users to focus on specific periods.

5.Visualization and Insights

- Line plots display metric trends with anomalies highlighted.

-Anomaly tables list all detected abnormal records.

- Summary statistics table shows mean, median, anomaly count, and anomaly percentage for all numeric metrics.

6.Report Generation

- Users can download a CSV report containing the filtered data and anomaly labels for offline analysis.

--Tools & Libraries Used

1.Python Libraries:

Streamlit – for building the interactive dashboard.

pandas – for data preprocessing and manipulation.

numpy – for numerical operations.

plotly.express – for interactive plotting.

scikit-learn – for anomaly detection (IsolationForest) and scaling (StandardScaler).

pyngrok – to expose the Streamlit app via a public URL in Google Colab.

2.Execution Environment:

Google Colaboratory (.ipynb)

--Key Insights from the Dashboard

Heart Rate:

Average and median heart rates are displayed.

Abnormal spikes or drops are highlighted as anomalies.

Steps:

Detect unusually high or low activity levels compared to typical daily steps.

Anomalies could indicate missed data, unusual activity, or device errors.

Sleep Duration:

Detect abnormal sleep patterns or deviations from typical duration.

Helps in identifying possible health or lifestyle issues.

Overall Summary:

The summary table provides a quick overview of anomalies across all metrics.

The anomaly percentage helps in understanding the prevalence of abnormal events in the dataset.
