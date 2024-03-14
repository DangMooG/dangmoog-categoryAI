# Fasttext-category-classification #


## Run on Local Server ##

### 1. Setup ###
    # Project clone
    git clone https://github.com/DangMooG/dangmoog-categoryAI.git
    
    # Go to directory
    cd dangmoog-categoryAI/fasttext
    
    # Install requirements
    pip install -r requirements.txt

### 2. Move trained model to your directory

  - You can download pre-trained model here
    <https://drive.google.com/drive/folders/1u-iqZDcNawoFSeAXzELw0KME-9m6y2zJ?usp=drive_link>

  - Move 'fasttext_v1.0.0.bin' to your directory 'dangmoog-categoryAI/fasttext/trained_model'

### 3. Execute main.py ###

    python main.py

### 4. Test on local server ###

    # Go to test directory
    cd dangmoog-categoryAI/examples
    
    # Execute test
    python api_call.py 

  or Excecute nobebook cells on 'request_test.ipynb' 


## Run on docker container ## 

### 1. Pull Image in docker-hub ### 

### 2. 
  
