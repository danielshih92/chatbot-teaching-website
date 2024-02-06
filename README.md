
# chatbot-teaching-website
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/danielshih92/chatbot-teaching-website.git

```

--> Move into the directory where we have the project files : 
```bash
cd chatbot-teaching-website

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv env

```

--> Activate the virtual environment :
```bash
env\Scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Setting up Environment Variables :

Create a file named `.env` in the root directory of the project. Add the following variables to configure your environment:\n
You can get free openai APIKEY here: https://github.com/chatanywhere/GPT_API_free?tab=readme-ov-file
```bash
API_KEY="your_openai_api_key"
SECRET_KEY = "yout_secret_key"
```
### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src=">  
</td>
</table>
