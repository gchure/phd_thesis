---
title: 'Towards A Single-Cell View of Horizontal Gene Transfer'
author: 
	-name: Griffin Chure
abstract: |
	Bacterial populations live in a fertile cocktail of foreign genetic
	material. Whether by viral infection, conjugative transfer, or direct
	uptake of DNA through transformation, bacteria frequently share their
	genetic information with their neighbors (including those of different
	species) strongly influencing bacterial evolution. Prior work on
	horizontal gene transfer has primarily been performed in bulk requiring
	the growth of saturated and well-mixed bacterial cultures. Such
	conditions, however, are far removed from natural environments where
	cells often grow in non-homogeneous multi-species biofilms. Precision
	measurements of horizontal gene transfer in single cells will allow us
	to paint a more detailed picture of the evolutionary implications in
	natural envi- ronments and thus provide a better understanding of the
	evolutionary implications of horizontal gene transfer. In this
	research, I will characterize and quantify the frequency and dynamics
	of horizontal gene transfer during transformation and transduction at
	single-cell resolution to understand how mobile genetic information
	affects the formation and evolution of microbial communities. I have
	employed a genetically encoded system in Escherichia coli and Bacillus
	subtilis that allows for the observation of DNA molecules with sequence
	specificity as they are transferred between individual cells. The
	physiologically non-perturbative nature of the visualization system
	allows for in vivo studies of the dynamics of conjugation,
	transformation, and transduction. In addition, this research will
	advance our understanding of how recombination of foreign genetic
	material into the chromosome can influence genomic architecture.

---


#Introduction 

blah blah blah

#Experimental Progress

A careful and quantitative measure of the uptake and expression from external
DNA. 

##Description of Set-Up
Forced competence, incubation, etc. 

##Pitfalls and concerns
Free DNA is replenished through cell death. 

Not all loci are alike. 

Washes may not be complete. 

Maturation and incubation timeee may be a concern. 

##The Ideal ParB System 
State of the cloning. Reasons why it may not be worth going forward. (Running
out of loci, expresssion, time, certainty of false positive/negatives)

Similar thing can be done with DNA FISH.

#Data Analysis
Single cell measurements of rare events needs many, many trials. This means
that I need many images

##Image Processing Pipeline

1. Segmentation. 
2. Filtering. 
3. Property extraction. 
4. Classification. 
5. Frequency computation

##Who is a transformant?

Not as obvious as one would thnik just from looking at an image. 

Show histograms. 


Show bleed through is not an issue. 


Extracted image moments. 


Show correlation between CFP and YFP. Show the ratio. 


Depending on thresholding, results can be an order of magnitude different. 


##For example of analysis. 
Assume that is boolean. do the analysis. 


Do the full derivation of bayes and binomial distribution

Show plots of the posterior. 

Do the derivation of the error. 


Show the plots with error bars.



#Does it matter in Evolution?


$$
P(\mathrm{HGT} \vert \mathrm{[DNA]}, \mathrm{stress}) \sim P(\mathrm{comp.}
\vert \mathrm{stress}) \cdot P(\mathrm{uptake} \vert \mathrm{[DNA]},
\mathrm{comp.})
$$


Why does HGT occur?

1. Nutrition
2. DNA Repair
3. A source of new genetic information. 


##Is HGT a valid strategy for overcoming selective pressures?

Pose the question in both the antibiotic context and the nutritional stress
context. 


Show the differential equations explaining each case. 

Plot the predictions. 



Do the simulations and include the code snippets. 


##Experimental test. 
Plate reader and growth assays. With *B. sub*, I know what the uptake
probabilities will be at a given concentration of DNA. I can also very easily
figure out the tuneability of competence. This is a contrived situation to a
degree, but it relevant in some contexts (hospitals, persistent infections,
etc).



 


