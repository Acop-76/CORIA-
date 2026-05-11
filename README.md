### Contributor
Name: Coppalle Alexis
Institution: CORIA INSA Rouen
Country: France

------------------ Calibration of the thermal degradation of pine wood

with experimental dataset  ‘Test case : UMET_Wood_TGA_N2_10K_R3’

Optimisation sofware : DAKOTA, Version: 18
Optimisation algorithm : NL2SOL
(Dennis J.E., Gay M., ACM Transactions on Mathematical Software (ACM), Algorithm 573: NL2SOL—An Adaptive Nonlinear Least-Squares, 1981)

kinetic mechanism of wood decomposition
- Dry wood
-Three reactions in parallel , corresponding of the three pseudo-components hemicellulose, cellulose and lignin.
-For each reaction (i=1 hemicellulose, i=2 cellulose, i=3 lignin)
	component i===> ni char + (1-ni) gaz
ni stoechiometric coefficient od reaction

-Proportions, in %weight in virgin wood,  for hemicellulose, cellulose and lignin
(Márquez‑Montesino, Reaction Kinetics, Mechanisms and Catalysis Reaction Kinetics, Mechanisms and Catalysis (2021) 132:1057–1074, https://doi.org/10.1007/s11144-021-01954-5)
P1=0.163
P2=0.544
P3=0.293

-With the nomenclature of eq. 1 of the document ‘Guidelines_for_Particpation_MaCFP-4.pdf’




i=3, j=1
ns,i,j =1 for i=1-3 (reaction order 1)
nt,i,j = 0 (no explicit temperature dependence)

===> Application of the NL2SOL algorithm
For each progress variable  ai  of the 3 decomposition reactions
		dai dt = Ai,1 (1- ai ) exp(- Ei / Rts)
and
		d(m/m0)cal/dt = S Pi (1- ni )  dai dt

with m the total mass of the solid, and m0 the initial value

The fitness function F is calculated by the following sommation over time (0-1500s)

		F=   S [(m/m0)cal - (m/m0)exp]2

### Results
E1=9,227E+04	A1= 3,195E+08	n1= 0,281
E2= 1,004E+05	A2= 8,389E+07	n2= 0,001
E3= 2,768E+04	A3= 7,765E+00	n3=0,164

------------------ material properties of pine wood

with experimental dataset ‘TIFP+UCT_Wood_Gasification_30kW_hor_parallel_R1’

Simulation of the degradation and pyrolysis under N2: PATOx
(J. Lachaud et al: A generic local thermal equilibrium model for porous reactive materials
submitted to high temperatures, International Journal of Heat and Mass Transfer 108 (2017) 1406–1417)







see attached picture: 1Dcalculation-geometrie.png











Optimisation sofware: DAKOTA, Version: 18
Optimisation algorithm: NL2SOL
(Dennis J.E., Gay M., ACM Transactions on Mathematical Software (ACM), Algorithm 573: NL2SOL—An Adaptive Nonlinear Least-Squares, 1981)

The fitness function F is calculated by the following sommation over time (0-1500s)

		F=   S [(m/m0)cal – (m/m0)exp]2

with m the total mass of the solid, and m0 the initial value

kinetic mechanism of wood decomposition
The one obtained by optimsation on ATG dataset.
- Dry wood
-Three reactions in parallel , corresponding of the three pseudo-components hemicellulose, cellulose and lignin.

Optimised parameters : assumed to be constant

heat capacity (K/kg/K): virgin-wood (cpv), char (cpc)
thermal conductivity (W/m/K) : virgin-wood (kv), char (kc)
emissivity : char emc 
absorptivity : char abc
convective coefficient at the top (w/m²) : hTop

known parameters  for wood: from litterature
emissivity : 0.75
absorptivity : 0.9
Rq : these values have a low influence on the 1D calculation results under 30kw/m2

known parameters  for isolant: from litterature
 840          -8.967E+05      0.05         0.05            0.05             0.9               0.9
heat capacity (K/kg/K): 840
thermal conductivity (W/m/K) : 0,05
emissivity: 0.9
absorptivity: 0.9
convective coefficient at the bottom  (w/m²): hbottom= 10kw/m2


