Milestone 3: Anomaly Detection and Visualization

### Objective 
The objective of this milestone is to detect, label, and visualize anomalous health patterns from fitness device data. By analyzing deviations between observed and predicted values, abnormal heart rate and sleep behaviors are identified to support early detection of unusual fitness activity.

### Steps Followed

1. Residual Analysis
   - Applied Facebook Prophet to model expected trends in heart rate data.
   - Computed residuals by comparing actual values with predicted values.

2. Threshold-Based Detection
   - Identified anomalies where the absolute residual exceeded two times the standard deviation.
   - Flagged extreme deviations from normal behavior.

3. Cluster-Based Detection
   - Applied clustering techniques to detect outlier behavioral patterns.
   - Identified anomalous clusters representing unusual fitness activity.

4. Visualization
   - Created time-series visualizations with anomalies highlighted.
   - Generated separate visualizations for heart rate and sleep pattern anomalies.

### Tools Used
- Python  
- Pandas  
- NumPy  
- Facebook Prophet  
- Scikit-learn  
- Matplotlib  
- Streamlit  
- Google Colab  


### Key Insights and Visualizations
- Residual-based analysis effectively detected abnormal heart rate variations.
- Threshold-based and cluster-based approaches together improved anomaly detection reliability.
- Sleep anomalies were observed during sudden changes in sleep duration.
- Visualizations clearly highlighted anomalous segments in the fitness time-series data.

### Visualization and Deployment
All anomaly detection results and visualizations generated in Milestone 3 are presented through an interactive Streamlit application deployed on **Hugging Face Spaces**.

Live Application Link: 
https://huggingface.co/spaces/VinothaManikannan/Milestone3 

### The application provides:
- Heart rate time-series visualization with detected anomalies highlighted  
- Sleep pattern visualization showing abnormal segments  
- Residual-based anomaly detection using Prophet predictions  
- Threshold-based and cluster-based anomaly labeling  
- Visual interpretation of abnormal fitness behavior patterns
