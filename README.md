# CPGRAMS-ChatBot
**problem statement**: Develop an AI/ML-driven Chatbot which is   Ministry Specific to help the Citizens to resolve their common queries related to filing a Grievance in the CPGRAMS portal (https://pgportal.gov.in) and expedite smooth submission of grievances.

We have develop AI based ChatBot for CPGRAMS portal which provides interface for user to resolve their queries related to filling grievances form.The major outcomes are **Faster Resolution of Grievances**,**Data Insights and Analytics**,**Reduction in Manual Workload**. 

Advantage using AI integrate ChatBot:
* Efficiency
* Continueously Learning 
* Cost effective

## Requirement
**Hardware Requirement**  
* CPU: Multi-core
* RAM: Atleast 6 GB 
* Internet Connectivity  

**Software Requirement**
* OS: Window(8/10/11),IOS,Linux
* Python
* Machine Learning Libraries (pytorch,NLP)

## TECH STACK
* Flask FrameWork
* Pytorch 
* NLP Libraries
* Python 

## API Reference by sanjsy

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
```
python app.py
```
![image]("https://github.com/Jeswin-J/CPGRAMS-ChatBot/blob/sanjay/static/images/Train.png")

## Implementation Cost
This approach of Implementation is cost effective which almost cost **zero rupees** to integrated into CPGRAMS portal.
## Team 

Jeswin Joesph  
Sanjay   
Johith Raj   
Rajkumar   
Jeswin Rymonnd