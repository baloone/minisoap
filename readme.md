# Minisoap
## Install dependecies
First you need to have python 3 and pip installed on your computer.
You also will have to install ffmpeg on your computer. This can be done for instance on ubuntu just by running ```sudo apt install ffmpeg```.

Then you will have to install the requirements by typing ```pip install -r requirements.tst```

## Launching the interpreter
To launch the interpreter you need to run ```python minisoap.py``` 

Then it should display:

```

╔╦╗ ╦ ╔╗╔ ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║║║ ║ ║║║ ║ ╚═╗ ║ ║ ╠═╣ ╠═╝  0.1a
╩ ╩ ╩ ╝╚╝ ╩ ╚═╝ ╚═╝ ╩ ╩ ╩

>
```

## Running a minisoap file

```python minisoap.py example.minisoap```

## Documentation
### Get the list of available functions
```
> all_functions ()
INFO: all_functions: Prints all available functions
INFO: 
INFO: all_mics: Transform all microphones to streams
INFO: 
INFO: get: Get element from array
INFO:         
INFO:         @param i Index of element
INFO:         @param array The array
INFO: 
INFO: mix: Mixes between two streams
INFO:         
INFO:         @param stream The main stream
INFO:         @param bgstream The background stream (optional)
INFO:         @param scalar The multiplier (default value : .5)
INFO: 
etc.
```
### Get the descriptions of a particular function

```

> sine ?
INFO: 
INFO: Generate a sine wave
INFO: 
INFO: @param freq The frequency of the wave (optional)
INFO: @param amplitude The wave amplitude (optional)
INFO: @param duration The duration of the wave in seconds (optional)
INFO:

```
