# mekorama_plandisplay
This software can be used to visualize plans made for the Mekorama assignment in the WASP course. With some modifications it can be used for more levels but right now it is hard coded for level 26. 

## Installing
```
pip install matplotlib
git clone https://github.com/pjensfelt/mekorama_plandisplay.git
```

## Running
Assuming that you have create a plan and that this plan fie is called plan_sas.3`
```
cd mekorama_plandisplay
python visualize_mekorama_plan.py -f sas_plan.3 
```
