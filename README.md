# mekorama_plandisplay
This software can be used to visualize plans made for the Mekorama assignment in the WASP course. With some modifications it can be used for more levels but right now it is hard coded for level 26. 

## Installing
```
git clone https://github.com/pjensfelt/mekorama_plandisplay.git
```

### Requirements
The tool requires matplotlib
```
pip install matplotlib
```


## Running
Assuming that you have create a plan and pasted that this plan into a file called `plan.txt`
```
cd mekorama_plandisplay
python visualize_mekorama_plan.py -f bad_plan.txt
```
