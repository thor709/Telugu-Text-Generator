# Telugu_text_generator

Link: https://share.streamlit.io/golden-panther/telugu_text_generator/main/telugu_text_gen.py

## Usage
1. Open website
2. Select/input seed text
3. Adjust "amount of text" value
4. Click on "Submit"
5. The generated text will be displayed with a success message.

Note: There are two methods of giving input. Choose any one.
  1. Custom input - Here, the user needs to provide a seed/prompt text (telugu).
  2. Select one of the readily available sample seed texts.

## Below are some screenshots of the website.

### Custom Input
![alt text](https://github.com/golden-panther/Telugu_text_generator/blob/main/CustomInputPic.png)

### Readily available sample seed texts
![alt text](https://github.com/golden-panther/Telugu_text_generator/blob/main/SampleSeedPic.jpg)

### Generated text and menu
![alt text](https://github.com/golden-panther/Telugu_text_generator/blob/main/MenuPic.jpg)

### Success message
![alt text](https://github.com/golden-panther/Telugu_text_generator/blob/main/SuccessPic.jpg)

# >> Details

I integrated two APIs to achieve telugu language text generator from english text generator.
  1. Googletrans (a python module which enables usage of free Google translate API)
  2. DeepAI's text generation API (it is based on GPT-2)

I used streamlit to host this project online.

This is how the code works.....
  1. Take telugu text as input and store it in "telugu_query"
  2. Translate it to english and strore it in "english_query"
  3. Input this english_query to generate text using DeepAI's API and store it in "english_text"
  4. Translate this "english_text" into "telugu_text"
  5. Display the output

# >> How to run this app
To use our project - go to this link: https://share.streamlit.io/golden-panther/telugu_text_generator/main/telugu_text_gen.py

(or)

To run this app

```
pip install -r requirements.txt
streamlit run https://raw.githubusercontent.com/golden-panther/Telugu_text_generator/main/telugu_text_gen.py
```

(or)

To run our telugu text generator on your machine by cloning this repository,
* Type the following in your terminal or cmd:
```
pip install -r requirements.txt
streamlit run telugu_text_gen.py
```
* The web app opens up in a local host. Then you can use it for generating telugu text. That's it!

## You can get some telugu seed texts from here: 
https://te.wikipedia.org/wiki/
