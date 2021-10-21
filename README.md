<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">

[![Run unit tests](https://github.com/ian-mcfarlane/pk-modelling/actions/workflows/python-unit-tests.yml/badge.svg)](https://github.com/ian-mcfarlane/pk-modelling/actions/workflows/python-unit-tests.yml)
[![OS Tests](https://github.com/ian-mcfarlane/pk-modelling/actions/workflows/OS-tests.yml/badge.svg)](https://github.com/ian-mcfarlane/pk-modelling/actions/workflows/OS-tests.yml)

# Pharmacokinetic Model for Intravenous and Subcutaneous Dosing
This Python library models the diffusion of a drug through the body, using simple 2- and 3-compartment pharmacokinetic models. This project does not feature interactions with pharmacodynamic models.

These models can be used to ensure there are sufficient concentrations of the drug administered according to its toxic threshold and the desired efficacy of the drug regimen.
## 2-Compartment Model (Intravenous Dosing)
The 2-compartment model describes _intravenous bolus_ dosing into a body with one "central" compartment and one "peripheral" compartment.

The central compartment is where the drug is directly administered according to the _Dose_ function, and excreted according to rate _CL_.

The drug diffuses between the central and peripheral compartments according to the rate Q<sub>p1</sub> and their relative volumes and drug concentrations.

The corresponding system of ordinary differential equations for this model is:

![equation](https://latex.codecogs.com/svg.latex?\frac{dq_c}{dt}&space;=&space;\text{Dose}(t)&space;-&space;\frac{q_c}{V_c}&space;CL&space;-&space;Q_{p1}&space;\left&space;(&space;\frac{q_c}{V_c}&space;-&space;\frac{q_{p1}}{V_{p1}}&space;\right&space;),)

![equation](https://latex.codecogs.com/svg.latex?\frac{dq_{p1}}{dt}&space;=&space;Q_{p1}&space;\left&space;(&space;\frac{q_c}{V_c}&space;-&space;\frac{q_{p1}}{V_{p1}}&space;\right&space;).)

Where:
* q<sub>c</sub> is the quantity of the drug in the central compartment
* q<sub>p1</sub> is the quantity of the drug in the peripheral compartment
* Dose(t) is the dose function
* V<sub>c</sub> is the volume of the central compartment
* V<sub>p1</sub> is the volume of the peripheral compartment
* CL is the clearance rate from the central compartment
* Q<sub>p1</sub> is the transition rate between central compartment and the peripheral compartment.


## 3-Compartment Model (Subcutaneous Dosing)
The 3-compartment model describes _subcutaneous_ dosing into a body with one "central" compartment and one "peripheral" compartment. The subcutaneous dosing is represented by a third compartment into which the dose is administered, from which the drug diffuses into the central compartment according to rate q<sub>0</sub>

The drug diffuses between central and peripheral compartments as in the 2-compartment model.

The corresponding system of ordinary differential equations for this model is:

![equation](https://latex.codecogs.com/svg.latex?\frac{dq_0}{dt}&space;=&space;\text{Dose}(t)&space;-&space;k_a&space;q_0,)

![equation](https://latex.codecogs.com/svg.latex?\frac{dq_c}{dt}&space;=&space;k_a&space;q_0&space;-&space;\frac{q_c}{V_c}&space;CL&space;-&space;Q_{p1}&space;\left&space;(&space;\frac{q_c}{V_c}&space;-&space;\frac{q_{p1}}{V_{p1}}&space;\right&space;),)

![equation](https://latex.codecogs.com/svg.latex?\frac{dq_{p1}}{dt}&space;=&space;Q_{p1}&space;\left&space;(&space;\frac{q_c}{V_c}&space;-&space;\frac{q_{p1}}{V_{p1}}&space;\right&space;),)

Where:
* q<sub>0</sub> is the concentration of drug in the initial dosing subcutaneous compartment
* k<sub>a</sub> is the rate of diffusion from the subcutaneous compartment to the central compartment
* All other parameters as in the 2-compartment model.

# Inputs
All parameters above are to be specified by the user in a .csv file to be read by the model. This file takes the format:

label,comps,Q_p1,V_c,V_p1,CL,X,dose_on,dose_off,k_a,graph_preview.

Each new line of the input .csv file represents a new set of parameters to be run through the model and will each produce a solution.

Each parameter is explained below:
* label = a string labelling the set of parameters to distinguish from all other sets being run
* comps = the number of compartments in the model, with 2 representing intravenous dosing and 3 representing subcutaneous dosing
* Q_p1 = the diffusion rate (mL/h) between the central and peripheral compartment
* V_c = the volume (mL) of the central compartment
* V_p1 = the volume (mL) of the peripheral compartment
* CL = the clearance rate (mL/h) from the central compartment
* X = the amount (ng) of drug to be administered at all relevant time points (see section Dosing Functions for guidance on designing a dosing function)
* dose_on = the number of time periods (1000ths of 1 hour) for which the dose is to be administered at a time (see section Dosing Functions for guidance on designing a dosing function)
* dose_off (optional) = the number of time periods (1000ths of 1 hour) for which the dose is not to be administered at a time
* k_a (optional) = the diffusion rate from the subcutaneous dosing compartment to the central compartment in the 3-compartment model
* graph_preview (optional) = True or False, indicating whether to show a preview of the dosing graph when creating parameter sets.

# Outputs
The model outputs a graph representing the change in drug quantity for each compartment for each set of parameters input.

# Appendix: Dosing functions
The dosing regimen is specified by three parameters in the model inputs:

* X - the amount of drug in ng administered
* dose_on - the length of time period for which doses are administered
* dose_off - the length of time between each dosing period

## Example 1
If dose_on = 0 then the dose function represents an instantaneous dose at time 0 and no more of the drug will be administered. In this case dose_off does not need to be specified, and its value will not affect the dose function.

For example, if:
* X = 1, and
* dose_on = 0

the dose function is as below:

![dose_func_ex_1](https://user-images.githubusercontent.com/92573875/138295265-3b09fd00-9449-4bde-a89b-2c4818f6fdc4.png)

## Example 2
If dose_on > 0 and dose_off = 0 then the dose function represents the drug administered continuously for the whole time period.

For example, if:
* X = 1,
* dose_on = 1, and
* dose_off = 0,

the dose function is as below:

![dose_func_ex_2](https://user-images.githubusercontent.com/92573875/138295334-ef1647af-71d2-475b-be27-367cae08faf6.png)
## Example 3
If dose_on > 0 and dose_off > 0 then the dose function switches between the drug being administered continuously (for as many time periods as dose_on specifies) and the drug not being administered (for as many time periods as dose_off specifies).

For example, if:
* X = 1,
* dose_on = 20, and
* dose_off = 30,

the dose function is as below:

![dose_func_ex_3](https://user-images.githubusercontent.com/92573875/138295483-69d58f80-8fce-4aaf-a26a-2e6d1ab5f769.png)