**Introduction and Background**

I think this section should talk about what HGT is and why it is important in
Nature. HGT is a strong driving force in bacterial evolution whose fossils are
embedded in the genome. You can see my NSF proposal (paragraph 1) for an
example of what I would include in the introduction. Below are some points I
think you should put in the background.

 *Three mechanisms of gene transfer* 

- Natural transformation - direct uptake of foreign DNA. This requires the DNA
  to be stable in the environment. The cell must be in the “competence state”
  where they express a myriad of genes that allow for DNA uptake to occur. The
  incredibly hydrophillic DNA must pass through the incredibly hydrophobic cell
  membrane. In some organisms (such as *Bacillus subtilis*) the cellular
  machinery has been studied extensively. In other organisms, the competence
  state is far more enigmatic and is worthy of study.


-  Conjugation - “bacterial sex”. This requires the presence of a
   “fertility element”, usually a plasmid that encodes the genes to
   build a pilus and also serves as the marker for where gene transfer
   begins. This requires other bacteria to be very nearby. This has been
   pretty well studied. More work is being done on the biochemistry of
   the assembly.

-  Transduction - the topic of your research. This section should be the
   longest part of your background. Transduction is a long-range
   mechanism of HGT. As long as the virus carrying the genetic material
   is around, it can pass it to other bacteria (so long as they have not
   developed resistance to the phage). Upon infecting the cell,
   bacteriophages have two fates – they can either reproduce and kill
   the cell immediately (the lytic state) or they can integrate their
   genome into the host and sit there for many generations or even into
   perpetuity (lysogenic state). When in the lytic state, the
   bacteriophage hijacks the cell’s machinery and makes many more copies
   of itself. It builds it’s capsid and packs it full of DNA. In some
   cases (the frequency is dependent on the species of phage) bits and
   pieces of the host genome can be packaged into the phage head. Once
   released into the environment, the phage can diffuse about and infect
   another cell. This DNA no longer encodes any of the genes needed to
   duplicate the phage so the bacterium may incorporate the DNA into
   it’s genome (or form a plasmid). Transduction is believed to be an
   incredibly strong driving force in the generation of mosaic genomes
   (need a reference for this – I’ll look around). What happens at the
   single cell resolution has not really been studied. There have been
   studies on the injection of DNA into the cell, but the frequency at
   which genes are transfered between bacteria is not studied in depth.

**Objectives**

I think there are three really nice objectives for the research. They
are outlined below.

1. Measure the frequency at which bacterial genes are transfered via
   transduction. We can measure this as a fraction of total phage
   infection (i.e. how many cells get DNA from other bacteria / how many
   cells die from infection total). This has not been studied at
   single-cell resolution. Our current estimates have been done at the
   bulk scale (10^9 bacteria) and only typically trace one trait. This
   is very likely an underestimate at cells could be infected by
   multiple phages – one carrying bacterial genes and the other carrying
   it’s own genome. To do this experiment, we need to use a phage that
   will **always** enter the lytic state. This way, we know that if a
   bacterium is infected it will die no matter what.

2. Measure differences in gene transfer based on gene type. Which are
   more frequently transfered - “core genes” (e.g. RNAP, 16s rRNA) or
   “accessory genes” (e.g. antibiotic resistance, metabolic genes). This
   can be done as combination of bulk measurements and single cell
   studies. This will require putting our reporter system into several
   different locations on the genome and measuring the frequency at
   which we find it.

3. How does selective pressure affect transduction? Is there a higher
   frequency of successful transfer in “stressful states”? One could ask
   if the presence of antibiotic in the medium would increase the impact
   of a successful HGT event. Again, this can be done at the single-cell
   and bulk level.

**Approach** 

In this section, you should describe the experimental
methods we will be using. We will be using single-molecule/single-cell
microscopy techniques to observe the transfer of specific DNA regions
into other cells through the action of transduction. We currently have a
system in which a protein has been fluorescently tagged (YGFP is the
fluorophore, ParB is the protein) that binds specifically and
cooperatively to a DNA sequence (parS - only 100bp long or something.
I’ll double check this number). Upon binding of ParB to the *parS* site,
ParB quickly oligomerizes resulting in a high concentration of protein
in a relatively small volume. Under the microscope, these appear as
bright “puncta” where as the cell is uniformly fluorescent when the DNA
sequence is not present.

For the phage experiments, we will need to integrate this *parS* site in
to many different places on the chromosome. Recombineering in *E. coli*
has been incredibly well engineered and this is a (relatively) trivial
task (I am currently trying to integrate it into two “accessory” loci).
The real utility of this system is that it serves as an “instantaneous
reporter”. Unlike watching for the expression of some reporter from a
transfered region (which would rely on the maturation time of the
reporter), our system can tell us immediately when *parS*-DNA is present
or not because the ParB protein is being continually expressed. The
other nice part about this system is that it does not require a huge
amount of DNA. The *parS* sequence is very small (again I’ll check the
exact length) meaning that the genetic region we are observing is
relatively unperturbed. Studies have been done previously (see Joe
Pogliano lab at UCSD) to monitor plasmids by having an array of ~256
*lacO* or *tetO* binding sites to which reporters attach. This results
in about 12kb of excess DNA. In our case, we are really only modifying
the genomic environment by ~100bp.

The bulk assays will be done using traditional biological methods. This
can be done by plating onto selective plates and counting colonies as a
function of the total number of surviving cells.

Image processing and data collection will be written in Python (Rob will
probably suggest MATLAB but I like python).

With the data we collect, we’ll be able to build a quantiative
statistical model describing the frequency at which DNA is passed around
in the environment through transduction.

**Work Plan**

If I understand this section correctly, this should be a schedule of the
experiments.

This is a super, super tentative schedule. This will be easier to flesh
out when we have the rest of the proposal written (I think).

Weeks 1 - 2, Familiarization with microscopy/ generation of phage stocks
/general microbiology techniques, Integrations of parS sequences into
accessory loci

Weeks 2 - 4, Concurrent bulk and single-cell experiments. Infection of
bacteria with phage carrying bacterial genome, Continuing integrations.

Weeks 4 - 10, I’ll keep thinking about a schedule.

**References** 

Probably a good idea to include 4 - 5 references.
