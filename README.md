
Team 5: Censos Hackathon

## Project Name: AdjusterAI

A collection of artificial intelligence applications that are designed to simplify and improve the process of submitting claims for automotive damage.


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

#### Step 2: Launching the streamlit web app
```streamlit run StreamlitApp.py```

#### Step 3: Testing out the web app

-Upload a photo to see how the adjuster finds similar items from the dataset and suggests a severity level with claim estimate

-Type some text to see how the adjuster finds similar items based on your description and suggests a severity leve with claim estimate

##### Step 4 : Creating Vector Index search

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/10b7eb1a-01a4-460a-af65-469726d65db9)

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/be0043fc-6735-4a68-9e05-50dea50bfa84)

**Index Name** : **claim_image_search**

![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/dd01f658-9215-4b82-9f2b-85d3d0d5ba7e)




# Architectural Diagram
![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/c9519f75-6680-498a-b5ed-8d02d4b7ef6f)

