Single Molecule Investigation of Phage-Mediated Gene Transfer in *E. coli*
==========================================================================

Understanding the flow of genetic information through populations has
long been the focal point of biological inquiry. Vertical gene transfer,
the transmission of genetic determinants from parent to offspring, has
served as the “standard model” of evolution. For quite some time, it was
assumed that all life evolved in this manner, including prokaryotes.
However, in 1928 Frederick Griffith showed that pathogenicity could be
transferred *horizontally* between populations of bacteria, suggesting
that vertical inheritance was not the complete story. This work was
expanded upon by Oswald Avery and Colin MacLeod who showed that DNA was
the chemical identity of Griffiths’ “transforming material”. With the
advent of reliable genome sequencing, it has become incredibly apparent
that genes have been transferred between species, phyla, and even
domains over the course of evolutionary history. It has been estimated
that in the course of proteobacterial evolution, 75% of all protein
families have experienced 1.9 horizontal gene transfer (HGT) events^1^.
Vertical gene transfer and its implications with respect to evolution
has been studied extensively and is well understood. Over the past
several decades, horizontal gene transfer in prokaryotes has received a
considerable amount of study, yet there is still much that remains
enigmatic. Many interesting and basic questions surrounding HGT can be
answered by observing the events at the appropriate resolution. While
population scale studies are informative, being able to accurately
describe the movement of DNA through HGT at the cellular level will not
only further our understanding of the origin and passage of genetic
information, but of bacterial evolution as a whole.

**The mechanisms of HGT**

Bacteria live in a fertile soup of foreign genetic information. Over the
past 3.5 billion years of evolution, bacteria have developed three main
mechanisms of HGT – transformation, conjugation, and transduction.
Transformation occurs when a cell picks up exogenous DNA from its
environment and maintains it in a heritable form. This process is rife
with challenges as the incredibly hydrophilic DNA needs to cross the
hydrophobic barrier of the cell wall, evade the restriction systems of
the host bacterium, and either integrate into the chromosome or
circularize and persist as a plasmid. Such precise procedure often
requires an impressive amount of inter- (and in some cases intra-)
cellular communication. Many cells have a well-defined state of gene
expression, called the “competence state”, in where the cellular
machinery is built to facilitate genetic transfer. The gene expression
patterns of the competence state varies widely from organism to
organism; some genomes show evidence of horizontal gene transfer yet
lack characteristics specific to known competence states in other
organisms.

Another method of horizontal gene transfer is bacterial conjugation, in
which a donor cell transfers a plasmid or transposon to a recipient cell
through a tube-like bridge or direct contact between the cells^2,3^.
These special plasmids, often called fertility elements, can be
integrated into the host genome. Depending on where they are integrated,
material other than that of the fertility element can be transfered to
nearby cells. The plasmids often have mechanisms that safeguard against
transferring genetic information that may conflict with a similar
element in the recipient. Conjugation is often beneficial to the
recipient; for example, plasmids that code for antibiotic resistance can
be transferred through bacterial conjugation. Other transferred plasmids
can be regarded as parasitic elements that have evolved to spread
through conjugation4. This type of horizontal transfer has been shown to
occur at a high frequency in biofilms. However, the role that
conjugation has on the physiology, development, and evolution of
biofilms is unknown.

In both natural transformation and conjugation, the cell must be close
to the source of the donated genetic information, be it the environment
or some other cell. Transduction is the only known method of long-range
gene transfer, and is the topic of my research. Transduction is the
process in which genetic material is transferred from one bacterium to
another through a virus proxy, called a bacteriophage. Once the virus
infects the cell the virus can enter either of two fates - the lysogenic
state or the lytic state. In the lysogenic state, the bacterium
integrates the foreign genetic material into its own genome, where it
can sit for generations while the cell continues to live and reproduce
normally. In the lytic state, the viral DNA is not integrated into the
cell’s genome, but continues to replicate until the cells bursts and
releases the phage into the environment, where it can infect other
bacteria. Occasionally, viruses sometimes pack segments of the host
bacteria’s genome instead of viral DNA in its capsid by accident. In
this situation, the virus cannot enter the lytic or lysogenic state.
Instead, the virus can only donate segments of the host’s genome to the
recipient. Transduction is believed to be a significant factor in the
development of mosaic genomes, making it a process of interest in the
field of genetics. While there have been studies on the injection of DNA
into a cell, transduction at a single cell resolution has yet to be
studied in depth. Furthermore, the frequency at which genes are
transferred between bacteria has not yet been determined.

**Tracking transduction at single-molecule resolution**

My project seeks to observe and quantify transduction at the single-cell
level by watching the transfer of fluorescently labeled segments of DNA
from virus to cell, and the subsequent degradation or integration of the
DNA into the host genome. The frequency of gene transfer through
transduction has only been measured at a bulk scale (often selecting for
a specific phenotype), and is almost certainly an underestimate of the
frequency it occurs at the single-cell level. Recent advancement in
molecular biology, optical microscopy methods, and image processing
algorithms allow for a detailed study of the molecular nature of
evolution at single molecule resolution.

Griffin Chure and Rob Brewster, a graduate student and postdoctoral
researcher in the Phillips group respectively, have developed a
genetically encoded system to observe the dynamics of individual DNA
molecules in living bacterial cells. Specific low copy-number plasmids
use protein partitioning systems to ensure faithful inheritance of the
population into the daughter cells. While these systems come in many
flavors, all rely on sequence-specific recognition of DNA through
protein binding. One system, the ParABS partitioning system, uses
cooperative binding of the ParB protein to a relatively short (\~100bp)
*parS* DNA sequence. Upon binding to the sequence, ParB changes
conformation, recruiting approximately 100 other ParB proteins to the
DNA. This results in a high concentration of ParB protein in a small
volume surrounding the *parS* site. The Phillips lab has exploited this
system to observe individual DNA molecules by fusing a YGFP fluorophore
to the ParB protein and has inserted this fusion into the *gspI* locus
of the chromosome. In the absence of *parS* sequence, the YGFP-ParB
proteins are uniformly distributed through the cell. However, upon
addition of a *parS* site, on a plasmid or introduced through phage
infection, the YGFP-ParB proteins quickly cluster at the *parS* site
producing a bright puncta within the cell allowing observation of the
spatial distribution and movement of the DNA within the cell. Because
YGFP-ParB is being constitutively expressed, this system functions as an
instantaneous reporter and does not rely on the transcription,
translation, and maturation of conventional fluorescent reporter
systems.

Using this system, I plan to observe transduction at single-cell
resolution to quantify the frequency of bacterial gene transfer through
transduction. In order to study transduction at this scale, I will use a
phage that will always enter the lytic state so that we may determine if
the bacteria has been infected- the bacteria will surely burst and die
if the phage is in the lytic state indicating viral infection.
Furthermore, the presence of bright puncta will indicate successful
~~integration~~ transduction **(Not necessarily. The puncta will
indicate that the DNA inside the cell. The difference in rate of
diffusion will tell if it has been integrated or not)** whereas uniform
fluorescence throughout the cell will indicate that the *parS* has not
been successfully transduced into the acceptor cytosol. By measuring the
difference in the rate of diffusion of the puncta, I will be able to
differentiate between transduced fragments that are integrated into the
acceptor chromosome and those that are linear and diffusing in the cell.
Thus, the ParBS visualization system will allow us to determine if each
individual cell has undergone successful transduction. As a result, we
will be able to determine the frequency of transduction on a single-cell
level.

This paragraph is good, but you don’t really explain how you will watch
the frequency of gene transfer. Here, you should give a brief
description. “I will integrate the *parS* system into conventional
gene-replacement loci and watch for the transfer of this region into
YGFP-ParB expresing cells as is described in Figure 1.”

~~Once the rate of gene transfer through transduction has been
quantified, I would like to study the rate and dynamics of homologous
recombination of the transduced fragment.~~ ~~Being able to visualize
recombination at the single-molecule level would provide valuable
insight on the frequency of successful integration as it would allow us
to understand the process of integration and the obstacles that must be
overcome to allow for successful integration. This can be through the
system developed by Griffin Chure and Rob Brewster,~~ ~~in which the
cooperative binding of the ParB protein to a *parS* DNA sequence results
in bright puncta~~ ~~at the location of the~~ parS ~~site. This system
will allow us to track the spatial distribution and movement of the DNA
within the cell, thus giving us a method to visualize and understand the
integration of transduced DNA. ~~

**(The above paragraph doesn’t really add anything new. It feels that
you are simply repeating what we said two paragraphs ago when we
described the visualization system. I think you are trying to explain
that we will be able to observe fragments as they enter the cell,
diffuse around, and recombine with the genome by measuring the diffusion
of the spot in the cell. I kind of addressed this with my comment in red
above. I would try to rewrite this paragraph to make it more clear that
this is a separate goal of the proposal. As it is written, it feels like
a brief summary of the goal of the proposal)**

By specifically integrating the *parS* sequence into various regions of
the chromosome, I will be able to measure and compare the differences in
transduction frequency of different loci to determine if the frequency
of transduction of “accessory genes” (such as antibiotic resistance
elements) is the same as “core genes” (such as 16s rRNA). The
differences in gene transfer as a function of gene type can be measured
in bulk by inserting a reporter system at several sites on the genome
and measuring the frequency that it is found. This measurement can also
be performed at single-cell resolution using the same methods outlined
above.

**Very good and straight to the point. Add a sentence or two explaining
why this is worth investigating. A transfer of a 16s rRNA gene could
potentially be catastrophic if it’s an interspecies transfer whereas the
shuttling of accessory genes may be less of a burden for the cell. Which
would influence the evolution of the bacterium more? This kind of leads
into your next objective I think. **

![](media/image1.png)

Finally, I would like to study how different conditions affect the
evolutionary implications of transduction. ~~For example, the effect of
selective pressure, stressful states, and the presence of an antibiotic
on the frequency of successful transduction.~~ The selective pressures
of the environment (such as a limiting concentration of a carbon source
or presence of an antibiotic) would certainly favor the transfer of
genetic material that confers and advantage to the acceptor cell.
Antibiotics, specifically, have the potential to give us key insight
into the evolution of bacterial colonies. By infecting a bacteria with
phage raised against an antibiotic resistant ~~bug~~ host and placing
them in stressful concentrations (yet non-fatal concentrations) of
antibiotic, we can gain insight into how some bacterial colonies come
into evolutionary advantages like antibiotic resistance. This experiment
can be carried out in bulk scale by conducting a bulk assay as well as
with single-cell resolution. The procedure for this objective is very
similar to the procedure for the other objectives- an antibiotic
resistance cassette will be integrated along with the *parS sequence*
into different loci. Then we can observe the integration of the genome
sequences on a single-cell scale, as well as place entire colonies of
bacteria in an antibiotic to determine on a bulk scale how many have the
gene for antibiotic resistance.

After I finish collecting data, I will be able to build a quantitative
statistical model describing the frequency at which genetic information
is transferred through transduction.

**It is important to mention that you will do all of these experiments
in bulk as well as in single molecule, not just the final objective.
This will let us quantify how much of a difference is there between what
we see when looking at single cells versus entire cultures of bacteria.
I suspect they will be quite different. **

![](media/image2.png)Figure 2 details a ten-week plan of research and
objectives for each week. The unique construction of this research
allows for multiple objectives to be studied at once. For the first week
and a half of my research, I will become familiarized with the
microscopy equipment in the lab along with the specifics of molecular
biology and raising of bacteriophage stocks. The DNA visualization
system described in the methods has already been constructed allowing
for the beginning of experiments immediately. For the entirety of the
research, I will clone the *parS* DNA sequence into various regions of
the *E. coli* host genome. Due to the close relationship of my
objectives, I am able to conduct measurements for several of them at the
same time.

All of evolution is driven by molecular behavior within the cell. While
there has been much advancement in understanding the mechanisms of
horizontal gene transfer, much remains to be understood regarding the
role it plays in evolution. This research will advance our understanding
of the frequency at which genes are transfered at the single cell level
and the role it may play in the development and evolution of bacterial
colonies. The materials, equipment, and members of the Phillips lab put
me in the unique position to tackle this problem using the tools of
modern molecular biology and the quantitative analysis methods of
physics. By building a quantitative statistical model describing the
frequency at which genetic information is transferred through
transduction, we will be able to gain key insight into the evolution and
assembly of the bacterial genome.

1 T. Kloesges, O. Popa, W. Martin, T. Dagan, Mol. Biol. Evol. 28(2),
1057 (2011).

2 Ryan KJ, Ray CG (editors) (2004). *Sherris Medical Microbiology* (4th
ed.). McGraw Hill. pp. 60–4

3 Russi et al. (2008). “Molecular Machinery for DNA Translocation in
Bacterial Conjugation”. *Plasmids: Current Research and Future Trends*.
Caister Academic Press.

4 Holmes RK, Jobling MG (1996). *Genetics: Exchange of Genetic
Information.* in:*Baron’s Medical Microbiology* (Baron S *et al.*,
eds.) (4th ed.). Univ of Texas Medical Branch.
