
Team 5: Censos Hackathon

## Project Name: AdjusterAI

A collection of artificial intelligence applications that are designed to simplify and improve the process of submitting claims for automotive damage.



## Architectural Diagram
![image](https://github.com/ajdidonato7/censos-hackathon/assets/50722159/c9519f75-6680-498a-b5ed-8d02d4b7ef6f)


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



SwiftUI Template App
A todo list application built with the Realm Swift SDK and Atlas Device Sync.

You can follow along with the SwiftUI Tutorial to see how to build, modify, and run this template app.

This project uses Swift Package Manager (SPM) to load dependencies.

Configuration
For this template app to work, you must ensure that App/atlasConfig.plist exists and contains the following properties:

appId: your Atlas App Services App ID.
baseUrl: the App Services backend URL. This should be https://services.cloud.mongodb.com in most cases.
Using the Atlas App Services UI
The easiest way to use this template app is to log on to Atlas App Services and click the Create App From Template button. Choose Real Time Sync, and then follow the prompts. While the backend app is being created, you can download this SwiftUI template app pre-configured for your new app.

Cloning from GitHub
If you have cloned this repository from the GitHub mongodb/template-app-swiftui-todo repository, you must create a separate App Services App with Device Sync enabled to use this client. You can find information about how to do this in the Atlas App Services documentation page: Template Apps -> Create a Template App

Once you have created the App Services App, replace any value in this client's appId field with your App Services App ID. For help finding this ID, refer to: Find Your Project or App Id

Download the Client as a Zip File
If you have downloaded this client as a .zip file from the Atlas App Services UI, it does not contain the App Services App ID. You must replace any value in this client's appId field in App/atlasConfig.plist with your App Services App ID. For help finding this ID, refer to: Find Your Project or App Id

If you did not replace the App ID, you may see an Error: unsupported URL message.

Run the app
Open App.xcodeproj in Xcode.
Wait for SPM to download dependencies.
Press "Run".





