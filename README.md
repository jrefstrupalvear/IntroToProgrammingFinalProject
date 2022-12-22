# Stock Predictor 

## Description
This program was created to scrape stock data and make a simple prediction based off it. I used selenium to navigate chrome and eventually scrpae data from yahoo finance. I also used numpy and matplotlib to plot the data. FOor the prediction I used linear regression with the scipy library. Typing in the stock symbol in the terminal, will get you four graphs (for opening,closing,high price, and low price). These graphs will start at 25 days ago and 0 will be today. They will also predict the direction the prices is heading for the next 25 days.

## Legal Disclaimer
By downloading this program you assume full resposibility of your decisions on the stockmarket even if they are influence by what you see here. I am not liable for your loses on the market. This is a tool developed for a class and should not be used as a method of making stock decisions. The hope was that it would give an idea of where a stock is going over the next 25 days, nothing more.

## Getting Started

### Dependencies


 Python 3.10, python, matplotlib, numpy, selenium,scipy
* works on all OS that can run python all the above libraries

### Installing

* Download and Run it in a code editor/viewer
    - Make sure libraries are installed
    - make sure python is installed


### Executing program

* How To Run
- run the program on whichever editor your are using
- wait for a prompt in the terminal to enter your stock symbol (ALL CAPS, must be symbol)
- wait as the program opens up chrome and scrapes for the data
- look at the graph with the simple linear regression prediction
- close tabs when done

- 
```
code blocks for commands
```

## Help

- make sure that when you enter you symbol it is only the symbol. Don't use spaces as they will take you to a different part of the website
- depending on your connection, it might take a while for selenium to navigate as it waits for certain elements to appear on screen
- if it is still not working add more time to the WebDriverWait instantiation found on line 65

## Authors


 Joshua Refstrup Alvear 
 
 Email: J.RefstrupAlvear25@bcp.org

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [w3Schools](https://www.w3schools.com/python/default.asp)
* [Selenium Documetation](https://selenium-python.readthedocs.io/)
* [Automate The Boring Stuff](https://automatetheboringstuff.com/)
* [Google Search Automation](https://www.tutorialspoint.com/google-search-automation-with-python-selenium)
* [Explicit Wait Tutorial](https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/)
* [Labeling Axes](https://www.edureka.co/community/102186/how-set-the-figure-title-and-axes-labels-font-size-matplotlib)
* Dad's help with XPATHS
* Mr. Cozort (taught the class and provided files as well as tutorials)
* Made in Bellarmine College Preparatory's Intro to Computer Programming Class


