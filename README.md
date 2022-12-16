# Stock Predictor 

## Description
Uses selenium to scrape stock data from yahoo finance and simple machine learning to make an easy prediction. Goals: Scrape Data from a Website and Present it in a tangible Way

## Getting Started

### Dependencies


 Python 3.10, python, matplotlib, numpy, selenium
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
 J.RefstrupAlvear25@bcp.org

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
* [PyGame](https://www.pygame.org/docs/)
* [Automate The Boring Stuff](https://automatetheboringstuff.com/)
