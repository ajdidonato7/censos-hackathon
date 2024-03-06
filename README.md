
Team 5: Censos Hackathon

## Project Name: AdjusterAI

A collection of artificial intelligence applications that are designed to simplify and improve the process of submitting claims for automotive damage.



## Architectural Diagram
![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/c9519f75-6680-498a-b5ed-8d02d4b7ef6f)

**Video presentation : **   https://drive.google.com/file/d/1MHmtgiYn5KQ_m5KeW_pf5FsbwvE6JGtT/view?usp=sharing

###Installation Instructions : 

#### Step 1: Installing requirements

Optional: Creating Python venv\
```python -m venv env```\
```chmod +x env/bin/activate```\
```source env/bin/activate```

Install necessary packages\
```pip install streamlit```\
```pip install boto3```\
```pip install python-dotenv```\
```pip install pymongo```

#### Step 2 : Creating Vector Index search

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/10b7eb1a-01a4-460a-af65-469726d65db9)

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/be0043fc-6735-4a68-9e05-50dea50bfa84)

**Index Name** : **claim_image_search**

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/dd01f658-9215-4b82-9f2b-85d3d0d5ba7e)

#### Step 3: Launching the streamlit web app
```streamlit run StreamlitApp.py```

#### Step 4: Testing out the web app

-Upload a photo to see how the adjuster finds similar items from the dataset and suggests a severity level with claim estimate

-Type some text to see how the adjuster finds similar items based on your description and suggests a severity leve with claim estimate

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/f3bf8b84-07e3-44dd-b07f-ac9708e34c2a)



![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/d84563ae-0614-4cd9-8034-dea12a02eae7)


<img width="373" alt="image" src="https://github.com/ajdidonato7/censos-hackathon/assets/50722159/40823879-057f-4076-8f2c-8fe16689c22e">




