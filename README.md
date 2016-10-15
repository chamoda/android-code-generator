# android-code-generator

Automatically generate android activity code from xml layouts.

## Install

Python 2.7 Required

`pip install beautifulsoup4 lxml`  
`git clone https://github.com/chamoda/android-code-generator.git; cd android-code-generator`

## Run

`cat main_activity.xml | python generate.py`

You will get an output like

```java

// Private variables

private EditText etFromName;
private EditText etToName;
private EditText etToEmail;
private EditText etMessage;
private Button bSend;

// Initialize elements

etFromName = (EditText)findViewById(R.id.etFromName);
etToName = (EditText)findViewById(R.id.etToName);
etToEmail = (EditText)findViewById(R.id.etToEmail);
etMessage = (EditText)findViewById(R.id.etMessage);
bSend = (Button)findViewById(R.id.bSend);

```
