Vertical gene transfer, the transmission of genetic determinants from
one generation to the next both through sexual and asexual reproduction,
has long been the focal point in the field of genetics. Our
understanding of gene transfer, especially in eukaryotes, is mostly
built on this model. As a result, it was assumed that prokaryotic gene
transfer is fundamentally vertical as well. However, prokaryotes exhibit
other specialized processes for gene transfer, for example natural
transformation, conjugation, and transduction – these processes are
termed lateral gene transfer, or horizontal gene transfer. In general,
lateral gene transfer refers to the transfer of genes from one organism
to another organism which is not an offspring of the first organism.
Vertical gene transfer, and its implications with respect to evolution
is well understood. In contrast, the mechanisms of lateral gene transfer
have been not been studied as extensively. Lateral gene transfer plays a
major role in the evolution of antibiotic-resistant bacteria, making the
study of lateral gene transfer pertinent to health-care discussions
today.

Natural transformation occurs when a cell picks up exogenous DNA from
its environment and integrates the DNA with its own genome. The chemical
structure of DNA makes it extremely hydrophilic, while the chemical
structure of cell membrane makes it extremely hydrophobic. As a result,
the cell must be in a specific state, called the “competence state”, in
order to be able to experience transformation. Another method of lateral
gene transfer is bacterial conjugation, in which a plasmid is
transferred from one cell to another through a tube-like bridge or
direct contact between the cells. In both natural transformation and
conjugation, the cell must be close to the source of the donated genetic
information, be it the environment or some other cell. Transduction is
the only known method of long-range gene transfer, and is the topic of
my research. Transduction is the process in which genetic material is
transferred from one bacterium to another through a virus proxy, called
a bacteriophage. Once the virus infects the cell, transduction can then
enter one of two states, the lysogenic state or the lytic state. In the
lysogenic state, the bacterium integrates the foreign genetic material
into its own genome, where it can sit for generations while the cell
continues to live and reproduce normally. In the lytic state, the viral
DNA is not integrated into the cell’s genome, but continues to replicate
until the cells bursts and releases the phage into the environment,
where it can infect other bacterium. Transduction is believed to be a
significant factor in the development of mosaic genomes, making it a
process of interest in the field of genetics. While there have been
studies on the injection of DNA into a cell, transduction at a single
cell resolution has yet to be studied in depth. Furthermore, the
frequency at which genes are transferred between bacteria has not yet
been determined.

My project seeks to study transduction on a single-cell level in depth.
Firstly, I would like to measure the frequency at which bacterial genes
are transferred by the process of transduction. Then, I would like to
determine if there differences in gene transfer frequency depending gene
type – core genes or accessory genes. Once the frequency of transduction
is determined, I would like to identify how different conditions affect
transduction. Specifically, how does selective pressure affect
transduction? Do stressful states lead to a higher frequency of
successful transfer? Does the presence of an antibiotic in the
environment affect the transduction in any way?

The frequency that transduction occurs has been estimated at a bulk
scale. However, it has yet to be studied at single-cell resolution. In
order to study transduction at this scale, we will need to use a phage
that will always enter the lytic state so that we may determine if a
bacterium has been infected – the bacterium will surely burst and die if
that phage is in the lytic state. The differences in gene transfer as a
function of gene type can be measured both in bulk and at single-cell
resolution. To perform this measurement, we will need to insert a
reporter system at several sites on the genome and measuring the
frequency that it is found. Studying the impact of different
environments can both be done at the single-cell and bulk level.

I plan on using conventional single-molecule/single cell microscopy
techniques to observe the transfer of specific DNA regions into other
cells through the action of transduction. The lab where I plan on
working currently has a system in which a protein, *parB*, has been
fluorescently tagged with YGFP that binds specifically and cooperatively
to a parS, a DNA sequence. Upon binding of *parB* to the *parS* site,
*parB* quickly oligomerizes resulting in a high concentration of protein
in a relatively small volume. Under the microscope, these appear as
bright concentrated spots of fluorescence, in contrast to the uniform
fluorescence that is exhibited when the DNA sequence is not present.

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
done previously to monitor plasmids by having an array of ~256 *lacO* or
*tetO* binding sites to which reporters attach. This results in about
12kb of excess DNA. In our case, we are really only modifying the
genomic environment by ~100bp.

The bulk assays will be done using traditional biological methods. This
can be done by plating onto selective plates and counting colonies as a
function of the total number of surviving cells.

    Image processing and data collection will be written in Python.

After we finish collecting data, we will be able to build a quantitative
statistical model describing the frequency at which genetic information
is transferred through transduction.

I plan on using the first two weeks to familiarize myself with
microscopy, generation of phage stocks, and general microbiology
techniques. I will also integrate *parS* sequences into accessory loci.
In the next two weeks, I will conduct both bulk experiments and
single-cell experiments, in which I will infect bacteria with phage
carrying bacterial genome and continue to integrate *parS* sequences
into accessory loci.
