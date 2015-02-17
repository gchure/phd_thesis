**Single Molecule Investigation of Phage-Mediated Gene Transfer in *E.
coli***

Understanding the transfer of heritable information from parent to
offspring has long been the focal point of biological research. Vertical
gene transfer, the transmission of genetic determinants from parent to
offspring has served as the “standard model” of evolution. Our
understanding of gene transfer, especially in eukaryotes, is mostly
built on this model. For quite some time, it was assumed that all life
evolved in this manner, including prokaryotes. However, in 1928
Frederick Griffith showed that pathogenicity could be transferred
horizontally between populations of bacteria, suggesting that vertical
inheritance was not the complete story. This work was expanded upon by
Oswald Avery and Colin MacLeod who showed that DNA was the chemical
identity of Griffiths’ “transforming material”. With the advent of
reliable genome sequencing, it has become incredibly apparent that genes
have been transferred between species, phyla, and even domains over the
course of evolutionary history. I has been estimated that in the course
of proteobacterial evolution, 75% of all protein families have
experienced 1.9 horizontal gene transfer events[^1]. Vertical gene
transfer, and its implications with respect to evolution has been
studied extensively and is well understood. Over the past several
decades, horizontal gene transfer in prokaryotes has received a
considerable amount of study, yet there is still much that remains
enigmatic. Many interesting and basic questions surrounding HGT can be
answered by observing the events at the appropriate resolution. While
population scale studies are informative, being able to accurately
describe the movement of DNA through HGT at the cellular level will not
only further our understanding of the origin and passage of genetic
information, but of bacterial evolution as a whole.

Natural transformation occurs when a cell picks up exogenous DNA from
its environment and integrates the DNA with its own genome. This process
is rife with challenges as the incredibly hydrophilic DNA needs to cross
the remarkably hydrophobic barrier of the cell wall, evade the
restriction systems of the host bacterium, and either integrate into the
chromosome or circularize and persist as a plasmid. As a result, the
cell must be in a specific state, called the “competence state”, in
order to be able to experience transformation. Due to the challenges
presented during transformation, an incredible amount of cellular
communication is required to allow for transformation. The “competence
state” varies widely from organism to organism; some genomes show
evidence of horizontal gene transfer yet lack characteristics specific
to known competence states in other organism.

Another method of horizontal gene transfer is bacterial conjugation, in
which a donor cell transfers a plasmid or transposon to a recipient cell
through a tube-like bridge or direct contact between the cells[^2][^3].
The plasmids often have mechanisms that safeguard against transferring
genetic information that may conflict with a similar element in the
recipient. Conjugation is often beneficial to the recipient; for
example, plasmids that code for antibiotic resistance can be transferred
through bacterial conjugation. Other transferred plasmids can be
regarded as parasitic elements that have evolved to spread through
conjugation[^4].

In both natural transformation and conjugation, the cell must be close
to the source of the donated genetic information, be it the environment
or some other cell. Transduction is the only known method of long-range
gene transfer, and is the topic of my research. Transduction is the
process in which genetic material is transferred from one bacterium to
another through a virus proxy, called a bacteriophage. Once the virus
infects the cell, transduction can then enter one of two states, the
lysogenic state or the lytic state. In the lysogenic state, the
bacterium integrates the foreign genetic material into its own genome,
where it can sit for generations while the cell continues to live and
reproduce normally. In the lytic state, the viral DNA is not integrated
into the cell’s genome, but continues to replicate until the cells
bursts and releases the phage into the environment, where it can infect
other bacteria. Occasionally, viruses sometimes pack segments of the
host bacteria’s genome instead of viral DNA in its capsid by accident.
In this situation, the virus cannot enter the lytic or lysogenic state.
Instead, the virus can only donate segments of the host’s genome to the
recipient. Transduction is believed to be a significant factor in the
development of mosaic genomes, making it a process of interest in the
field of genetics. While there have been studies on the injection of DNA
into a cell, transduction at a single cell resolution has yet to be
studied in depth. Furthermore, the frequency at which genes are
transferred between bacteria has not yet been determined.

.

My project seeks to study transduction on a single-cell level by
watching the transfer of fluorescently labeled segments of DNA from
virus to cell, and integration of the DNA into the host genome. The
frequency of gene transfer through transduction has only been estimated
at a bulk scale, and is almost certainly an underestimate of the actual
frequency. Transduction has yet to be studied at single-cell resolution.
In order to study transduction at this scale, we will need to use a
phage that will always enter the lytic state so that we may determine if
a bacterium has been infected – the bacterium will surely burst and die
if that phage is in the lytic state. Furthermore, I would like to study
to dynamics of recombination into the host genome. Being able to
visualize recombination at the single-molecule level would provide
valuable insight on the frequency of successful integration as it would
allow us to understand the process of integration and the obstacles that
must be overcome to allow for successful integration. Below, I outline
an experimental procedure that will allow us to track the free DNA and
determine when it has been integrated into the bacterial genome.

Once I have determined the frequency of gene transfer through
transduction, I would like to determine if there is a difference in the
transfer of different gene types – core genes or accessory genes. The
differences in gene transfer as a function of gene type can be measured
both in bulk and at single-cell resolution. To perform this measurement,
we will need to insert a reporter system at several sites on the genome
and measuring the frequency that it is found.

Finally, I would like to study how different conditions affect
transduction. For example, the effect of selective pressure, stressful
states, and the presence of an antibiotic on the frequency of successful
transduction. Antibiotics, specifically, have the potential to give us
key insight into the evolution of bacterial colonies. By infecting a
bacteria with phage raised against an antibiotic resistant bug and
placing them in stressful concentrations of antibiotic, we can gain
insight into how some bacterial colonies come into evolutionary
advantages like antibiotic resistance. Studying the impact of different
environments can both be done at the single-cell and bulk level.

![](media/image1.png)

Figure 1 **A** The virus accidentally packs segments of the host’s
genome into its capsid and transfers it to another bacterial cell, where
it is recombined into the recipients genome. **B** Concentrate spots of
fluorescence upon binding of parB to the parS site

I plan on using single-molecule/single cell microscopy techniques to
observe the transfer of specific DNA regions into other cells through
the action of transduction. The lab where I plan on working currently
has a system in which a protein, *parB*, has been fluorescently tagged
with YGFP that binds specifically and cooperatively to *parS*, a DNA
sequence. Upon binding of *parB* to the *parS* site, *parB* quickly
oligomerizes resulting in a high concentration of protein in a
relatively small volume. Under the microscope, these appear as bright
concentrated spots of fluorescence, in contrast to the uniform
fluorescence that is exhibited when the DNA sequence is not present.
Figure 1 depicts the process of gene transfer through transduction and
how we will visualize recombination of DNA into the recipient.

For the phage experiments, we will need to integrate this *parS* site to
many different places on the chromosome. Recombineering in *E. coli* has
been incredibly well engineered and similar methods should be able to be
applied to the integration of this *parS* site. This system will be able
to serve as an instantaneous reporter. Typically, we would only be able
to determine the expression of our reporter gene after the maturation
time of the reporter. However, because the *parB* protein is continually
expressed, we can instantaneously determine whether *parS*-DNA is
present. The *parS* sequence is very small meaning that the genetic
region we are observing is relatively unperturbed. Studies have been
done previously to monitor plasmids by having an array of \~256 *lacO*
or *tetO* binding sites to which reporters attach. This results in about
12kb of excess DNA. In our case, we are really only modifying the
genomic environment by \~100bp.

The bulk assays will be done using traditional biological methods. This
can be done by plating onto selective plates and counting colonies as a
function of the total number of surviving cells.

> Image processing and data collection will be written in Python.

After we finish collecting data, we will be able to build a quantitative
statistical model describing the frequency at which genetic information
is transferred through transduction.

![](media/image2.png)

Figure 2- 10 week schedule with objectives each week

Figure 2 details a 10 week plan of research and objectives for each
week. The unique construction of this research allows for multiple
objectives to be studied at once. For the first week and a half of my
research, I will become familiarized with the microscopy equipment in
the lab along with the specifics of molecular biology and raising of
bacteriophage stocks. The DNA visualization system described in the
methods has already been constructed allowing for the beginning of
experiments immediately. For the entirety of the research, I will clone
the *parS* DNA sequence into various regions of the *E. coli* host
genome. Due to the close relationship of my objectives, I am able to
conduct measurements for several of them at the same time.

At the end of 10 weeks, I hope to understand horizontal gene transfer
through transduction on a single-molecule level. By building a
quantitative statistical model describing the frequency at which genetic
information is transferred through transduction, we will be able to gain
key insight into evolution of the genome. In the realm of healthcare,
antibiotic resistant bacteria is becoming an increasingly prevalent
concern. As a result, understanding the evolution of these bacteria has
important implications with regards to human health.

[^1]: T. Kloesges, O. Popa, W. Martin, T. Dagan, Mol. Biol. Evol. 28(2),
    1057 (2011).

[^2]: Ryan KJ, Ray CG (editors) (2004). *Sherris Medical
    Microbiology* (4th ed.). McGraw Hill. pp. 60–4

[^3]:  Russi et al. (2008). "Molecular Machinery for DNA Translocation
    in Bacterial Conjugation". *Plasmids: Current Research and Future
    Trends*. Caister Academic Press.

[^4]: Holmes RK, Jobling MG (1996). *Genetics: Exchange of Genetic
    Information.* in:*Baron's Medical Microbiology* (Baron S *et al.*,
    eds.) (4th ed.). Univ of Texas Medical Branch.
