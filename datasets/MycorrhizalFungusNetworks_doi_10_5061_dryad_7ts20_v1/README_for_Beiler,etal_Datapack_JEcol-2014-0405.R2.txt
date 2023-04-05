
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Manuscript title: 'Topology of tree-mycorrhizal fungus interaction networks in xeric and mesic Douglas-fir forests'


MS Authors: Beiler, Kevin; Simard, Suzanne; Durall, Daniel


MS Reference Number: JEcol-2014-0405.R2


ReadMe file created 05/FEB/2015


Contact: Kevin.Beiler@gmail.com


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

This ReadMe is a general guide to files comprising the data package associated with MS number JEcol-2014-0405.R2. 


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Contents of data package:

1. 01_SampleData 

2. 02_Genotypes

3. 03_PopulationData


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

File Name: 01_SampleData

Contents: Sample locations of Rhizopogon vesiculosus and R. vinicolor tuberculate ectomyocrrhizas which were successfully identified to fungal and tree genotypes. Ectomycorrhizas were collected from six 10 x 10 m plots characterized by either xeric or mesic soil moisture regimes. See manuscript for further information. 


'01_SampleData' column headings:
Column 1	;	Plot	;	10 x 10 m plot boundary within which ectomycorrrhiza root samples collected
Column 2	;	Site	;	Soil moisture regime (relative to dry, cool Pseudotsuga menziesii var. glauca forests)
Column 3	;	SmpleID	;	Sample ID (VES = Rhizopogon vesiculosus, VIN = R. vinicolor)
Column 4	;	GenetID	;	Genet ID (VES = Rhizopogon vesiculosus, VIN = R. vinicolor)
Column 5	;	TreeID	;	Tree genotype (Plot#-Tree#; -U = root genotype not matched to reference tree bole)
Column 6	;	X_UTM	;	Sample location X coordinate; UTM based on WGS 1984, Zone 10
Column 7	;	Y_UTM	;	Sample location Y coordinate; UTM based on WGS 1984, Zone 10


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

File Name: 02_Genotypes

Contents: Microsatellite data for Rhizopogon spp. fungal and Pseudotsuga menziesii var. glauca tree genotypes

'02_Genotypes' column headings:

Column4;	[L1A2] second allele at locus 1
Column5;	[L2A1] first allele at locus 2
Column6;	[L2A2] second allele at locus 2
Column7...		
Column#;	[L#A1] first allele at locus #
Column#;	[L#A2] second allele at locus #

>'#' = Number

>For R. vesiculosus, locus1 = Rv15, locus2 = Rv46, locus3 = Rve2.10, locus4 = Rve2.14, locus5 = Rve1.21, locus6 = Rve1.34, locus7 = Rve2.44, locus8 = Rve2.77, locus9 = Rve3.21.

>For R. vinicolor, locus1 = Rv15, locus2 = Rv46, locus3 = Rve2.10, locus4 = Rve2.14, locus5 = Rve1.21, locus6 = Rve1.34, locus7 = Rve2.44, locus8 = Rve2.77, locus9 = Rve3.21, locus10 = Rv53. Locus3 and locus5 were excluded from population genetic analysis.

>For P. menziesii, locus1 = PmOSU_1C3, locus 2 = PmOSU_1F9, locus 3 = PmOSU_2D4. 


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

File Name: 03_PopulationData

Contents: Rhizopogon vesiculosus and R. vinicolor fungal and Pseudotsuga menziesii var. glauca tree genotypes encountered within the six 10 x 10 m study plots, for calculation of population genetic parameters using GenAlEx, GENEPOP, etc. 

In order listed:
1. Title line identifies species
2. List of microsatellite DNA loci targeted
3. List of unique genotypes grouped by plot/population ('Pop') 

Genotype list column headings:
Column1;	[ID] genotype ID (species-plot-count format; for example VES-04-01 = R. vesiculosus genotype #1 in plot 4) 
Column2;	[Pop] for a priori population assignment according to independent study plots
Column3;	[Genotype] genotypes delineated by numbers assigned to unique alleles (2 digits) for each locus


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>








