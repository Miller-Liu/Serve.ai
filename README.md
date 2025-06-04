# Serve.ai: An AI Tennis Serve Coach
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

Ever wish that there was a better way to compare your tennis serve with the pros? Serve.ai offers tennis players an easy way to do just that, by intelligently adjusting the speed of two tennis serve videos so that both are synchronized. That way, you can see every stage of your serve and compare it to a professionals.

## Features

- **Intelligent Tennis Serve Synchronization**: Using [MediaPipe](https://chuoling.github.io/mediapipe/) and [Scikit-Learn](https://scikit-learn.org/stable/), Serve.ai is able to intelligently synchronize two videos of tennis serves. 
- **Supervised and Unsupervised Learning**: By implementing both supervised and unsupervised methods of comparing the videos, users can analyze the difference in performance between the two.
- **Modern and Intuitive UI**: Using Flask, HTML and CSS, users are able to interact with the application on a modern and intuitive interface.

## System Requirements

Before getting started, ensure you have the following installed on your system:

- **Pip**: Package management system
- **Pyenv**: Python version management


## Getting Started
### 1. Clone the repository
```bash
git clone <repository-url> <your-repo-name>
cd <your-repo-name>
```
### 2. Set up the virtual environment 
First, set the local Python version to 3.9.13.
```bash
pyenv local 3.9.13
```
To double check that the local version is 3.9.13, run
```bash
pyenv local # should be 3.9.13
```
Create the virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run `main.py`
```bash
python main.py
```
Alternatively, simply run `main.py` in an editor of your choice.

## How it works
After the app starts running, you will be prompted to input two videos of tennis serves. After you input the two videos, the program will use various AI methods to identify similar moments between the two videos, then edit the videos accordingly to synchronize them. The initial videos you inputted are stored in `Static/uploads`, the synchronized videos are are stored in `Static/videos`, and the AI-labeled similar moments between the two videos are stored in `Static/Images`.