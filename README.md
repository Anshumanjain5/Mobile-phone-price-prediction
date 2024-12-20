# 📱 **Phone Price Prediction**

## **Introduction**
This project focuses on predicting smartphone prices based on their specifications using machine learning. By analyzing features like RAM, wifi, touch screen, battery capacity, and others, we aim to estimate the price range of phones effectively. This can be useful for manufacturers, retailers, and consumers in making data-driven decisions.

---

## **Project Objectives**
- Develop a machine learning model to predict phone price ranges (e.g., budget, mid-range, premium).
- Explore and compare different machine learning algorithms for optimal performance.
- Provide insights into the impact of various features on phone prices.

---

## **Dataset**
- The dataset includes specifications of smartphones and their corresponding prices.
- Key columns and their descriptions:

### **1. `battery_power`**
- Total battery capacity (in mAh).
- Example: `842` (Phone 1), `1021` (Phone 2).

### **2. `blue`**
- Bluetooth support (`0` = No, `1` = Yes).
- Example: `0` (Phone 1: No Bluetooth), `1` (Phone 2: Supports Bluetooth).

### **3. `clock_speed`**
- Processor clock speed (in GHz).
- Example: `2.2` GHz (Phone 1), `0.5` GHz (Phone 2).

### **4. `dual_sim`**
- Dual SIM support (`0` = No, `1` = Yes).
- Example: `0` (Phone 1: Single SIM), `1` (Phone 2: Dual SIM).

### **5. `fc` (Front Camera)**
- Front camera resolution (in megapixels).
- Example: `1` MP (Phone 1), `0` MP (Phone 2: No front camera).

### **6. `four_g`**
- 4G support (`0` = No, `1` = Yes).
- Example: `0` (Phone 1: No 4G), `1` (Phone 2: Supports 4G).

### **7. `int_memory`**
- Internal storage capacity (in GB).
- Example: `7` GB (Phone 1), `53` GB (Phone 2).

### **8. `m_dep` (Mobile Depth)**
- Phone thickness (in cm).
- Example: `0.6` cm (Phone 1: Slimmer), `0.7` cm (Phone 2).

### **9. `mobile_wt`**
- Phone weight (in grams).
- Example: `188` g (Phone 1), `136` g (Phone 2: Lighter).

### **10. `n_cores`**
- Number of cores in the processor.
- Example: `2` (Phone 1), `3` (Phone 2: Better multitasking).

### **11. `pc` (Primary Camera)**
- Rear camera resolution (in megapixels).
- Example: `2` MP (Phone 1), `6` MP (Phone 2).

### **12. `px_height`**
- Screen resolution height (in pixels).
- Example: `20` (Phone 1: Low resolution), `905` (Phone 2: High resolution).

### **13. `px_width`**
- Screen resolution width (in pixels).
- Example: `756` (Phone 1), `1988` (Phone 2: Sharper display).

### **14. `ram`**
- RAM capacity (in MB).
- Example: `2549` MB (Phone 1), `2631` MB (Phone 2).

### **15. `sc_h` (Screen Height)**
- Height of the screen (in cm).
- Example: `9` cm (Phone 1), `17` cm (Phone 2: Taller screen).

### **16. `sc_w` (Screen Width)**
- Width of the screen (in cm).
- Example: `7` cm (Phone 1), `3` cm (Phone 2).

### **17. `talk_time`**
- Maximum talk time on a full battery (in hours).
- Example: `19` hours (Phone 1), `7` hours (Phone 2).

### **18. `three_g`**
- 3G support (`0` = No, `1` = Yes).
- Example: `0` (Phone 1: No 3G), `1` (Phone 2: Supports 3G).

### **19. `touch_screen`**
- Touchscreen support (`0` = No, `1` = Yes).
- Example: `0` (Phone 1: No touchscreen), `1` (Phone 2).

### **20. `wifi`**
- Wi-Fi support (`0` = No, `1` = Yes).
- Example: `1` (Both phones support Wi-Fi).

### **21. `price_range`**
- Phone price category:
  - `0` = Low cost
  - `1` = Medium cost
  - `2` = High cost
  - `3` = Premium cost.
- Example: `1` (Phone 1: Medium cost), `2` (Phone 2: High cost).

**Source**: [mobile price classification](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)

---

## **Technologies Used**
- **Languages**: Python
- **Libraries**:
  - **Data Processing**: Pandas, NumPy
  - **Modeling**: Scikit-learn, XGBoost, CatBoost
- **Tools**: Python script

---

## **Model Development**
1. **Feature Engineering**:
   - Handling missing values, scaling, and encoding categorical features.
2. **Model Training**:
   - Algorithms used:
     - Decision Trees
     - Random Forests
     - Gradient Boosting
     - Support Vector Machines
     - Linear Regression
     - Logistic Regression
3. **Model Evaluation**:
   - Comparison of algorithms based on metrics.

---

## **Results**
- Achieved a classification accuracy of **98%** (adjust based on your results).
- Feature importance analysis revealed that **RAM** and **Processor Speed** were the most significant predictors of price.

---

## **How to Use**
1. Clone this repository:
   ```bash
   git clone https://github.com/Anshumanjain5/Mobile-phone-price-prediction.git
   ```
2. Switch working directory to Mobile-phone-price-prediction
   ```bash
   cd Mobile-phone-price-prediction
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project:
   ```bash
   python app.py
   ```
5. Input specifications to get price predictions.

---

## **Future Enhancements**
- Incorporating more features like brand popularity or market trends.
- Using deep learning models for more complex relationships.
- Deploying the model as a web app for real-time predictions.

---

## **Contributing**
Contributions are welcome! Please fork this repository and submit a pull request with your ideas or improvements.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Contact**
For any questions or feedback, please reach out to:
- **Name**: Anshuman Jain
- **Email**: anshumanjain8886@gmail.com
- **GitHub**: Anshumanjain5
