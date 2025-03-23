## E-Matrix

E-Matrix is a Python-based chatbot that integrates the Matrix chat protocol with the Ollama Large Language Models.

***Features***
 * Allows the chatbot to participate in conversations in Matrix chat rooms. 
 * Saves conversation history for each chat room locally. (Not sus but, you are in control of someone else's data which gives you ultimate power.)
 * Customize bot personality via the `SYSTEM_CONTENT` environment variable.
 
***Installation*** 
 * Clone the Repository
   ```
   https://github.com/0xdotgz/E-Matrix
   ```
 * Install requirements from requirements.txt
   ```
   pip install -r requirements.txt
   ```
  * Configure all values in `.env` file
  * Launch the Bot
    ```
    python e-matrix.py
    ```

  ***Docker***

  1. Configure all values in `.env` file or pass the env variables to docker with `-e` tag.
  
  2. Build the Docker image:
  
     ```
     docker build -t ematrix .
     ```
  
  3. Run the Docker image
  
     ```
     docker run ematrix 
     ```
