# CPGRAMS-ChatBot
**problem statement**: Develop an AI/ML-driven Chatbot which is   Ministry Specific to help the Citizens to resolve their common queries related to filing a Grievance in the CPGRAMS portal (https://pgportal.gov.in) and expedite smooth submission of grievances.

We have develop AI based ChatBot for CPGRAMS portal serves as a virtual assistant, facilitating easy communication and answering questions about filling out grievance forms for users. By utilizing machine learning methods and **natural language processing (NLP)**, our ChatBot improves user experience by expediting the grievance filing process and guaranteeing timely response. 

Advantage using AI integrate ChatBot:
* Efficiency
* Continueously Learning 
* Cost effectiveness 

## Requirement
**Hardware Requirement**  
* CPU: Intel Core i5 or equivalent AMD processor recommended for optimal performance.
* RAM: Minimum: 4 GB RAM and Recommended: 8 GB or more for better performance, especially for handling multiple concurrent user interactions. 
* Minimum: **100 GB of available storage space** for OS, development tools, and application files.
* Internet Connectivity  

**Software Requirement**
* OS: 
  * Windows (7 or later)
  * macOS (10.11 or later)
  * Linux distributions (Ubuntu)
* Programming Language and Libraries:  
Python  
* Libraries:Flask, torch, nltk, numpy.

## TECH STACK
* Flask FrameWork
* Pytorch 
* NLP Libraries
* Python 

## API Reference 

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

## Approach
 **Define the Scope and Requirements for project:**
* we have Identified the *specific queries and tasks* the chatbot should handle related to filing grievances in the CPGRAMS portal.
* Also we determined the key features and functionalities required for the chatbot.

**Data Collection**  
* We utilizesed a dataset provide by DARPG and which contains  corresponding queries and responses related to filing grievances.
* Annotate the dataset for intents, entities, and dialog flow.

**Preprocessing and Feature Engineering:**
* Preprocess the text data, including tokenization, lemmatization, and removing stopwords.
* Converting the tokenization words into binary values and store them in array

**Model Selection and Training:**
*  Utilizing Torch library to train the Annotate dataset.
*  save the model 

**User Interface (UI) Design:**
* user-friendly interface for the chatbot is designed  considering the needs of both citizens and government agencies/officers.

**Deployment and Monitoring:**
* Deploy the chatbot in CPGRAMS portal 
* Monitor the chatbot's performance in real-time and make improvements based on user feedback and usage data.

## Procedure
Download the Python in your system [Python](https://www.python.org/downloads/) and set up.

Required Libraries to install and thier command

```
pip install pytorch
pip install flask 
pip install numpy
pip install nltk
```
**To run**

Install from github
```
git clone https://github.com/Jeswin-J/CPGRAMS-ChatBot.git

```

Run the project open command prompt
```
python train.py
```
![image](https://i.imgur.com/k2w0vt6.png)
```
python app.py
```

## Implementation Cost
This approach of Implementation is cost-effective which almost cost **zero rupees** to integrated into CPGRAMS portal. Also, the bot can learn continuously from the user inputs. So no manpower cost required. 
## Team 

Jeswin Joesph [Linkdin](https://www.linkedin.com/in/jeswinjosephj/)  
Sanjay [Linkdin](https://www.linkedin.com/in/sanjayk1415/)  
Johith Raj [Linkdin](https://www.linkedin.com/in/johithraj/)  
Rajkumar  [Linkdin](https://www.linkedin.com/in/raj-kumar-9a6b91249?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
Jeswin Rymonnd [Linkdin](https://www.linkedin.com/in/jeswin-rhymond/)