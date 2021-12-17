# Abusive-translated-bangla-facebook-comment-detection
This is a complete end to end project of detecting abusive comment in facebook. Trained various machine learning algorithms with the data that in have collected fro various facebook post. Apply the hyperparameter tunning to each algorithm to find out best parameter combination. Then make it a web app by using the Streamlit library.

![image](https://github.com/Sudhakordas/Abusive-translated-bangla-facebook-comment-detection/blob/master/Images/Abbusive.JPG)

## Process and Workflow diagram 

![image-2](https://github.com/Sudhakordas/Abusive-translated-bangla-facebook-comment-detection/blob/master/Images/Method.PNG)

1. In the first step of this project i collected facebook comment from various facebook pages and groups.
2. Swcondly i translated thoswe comment into English using the Google Tranlator.
3. Then Preprocess the text data and Convert into vector using the tfidfvectoriozer.
4. Used various machine learning algorithm and hyparameter tunned each and every algorithm.
5. Finally converted it as a end to end project(web app running in the localhost) by using Streamlit.

## How to run this project in your system.
1. Down load or clone the repository
```python
git clone https://github.com/Sudhakordas/Abusive-translated-bangla-facebook-comment-detection.git
```
2. Create a new environment.
3. Activate that environment 
 ```python
conda activate environment_name
```
4. Install all the denpendencies.
```python
pip install  -r requirements.txt
```
5. Now run the project.
 ### To run the web app.
 Go to the directory where you have clone the repository.
 Type 
 ```python
  streamlit run Ald.py
  ```
## Future work
1.I am wanting to make a simillar types of project to detect cyberbullyong in Bangladeshi local language.

