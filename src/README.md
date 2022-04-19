## Requirements
To install requirements run
```sh
pip install -r requirements.txt

```

## Input
The `input.txt` file describes the net in the following format:
- First line lists all places with their token distribution in the format `<token count>.<place>` (i.e. `4.wait`).
- Second line lists all the transitions.
- From the third line onward lists all arcs in the format `<source> <target>` (i.e. `wait start`).

## Application
To run the GUI app, run
```sh
python app.py

```

To run the TUI app, run
```sh
python petri_net.py

```
