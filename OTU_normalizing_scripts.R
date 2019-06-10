#### Libraries####
#DO THIS FIRST
install.packages("scales")
install.packages("tidyr")
install.packages("dplyr")
# You should only have to do this step the first time because after that, the R enviroment...should remember them
# Usually
library(scales)
library(tidyr)
library(dplyr)

# This installs bioconductor which is a hub for bioinformatics oriented R packages!
# If there are any issues with this step, let me know. 
# It's sometimes fussy because the versions of R and Bioconductor may not align
source('http://bioconductor.org/biocLite.R')
biocLite('phyloseq')
library(phyloseq)

#### Functions Needed ####
mergeTaxaNormOtuCounts <- function(physeq){
  physeq <- transform_sample_counts(physeq,function(x) x/sum(x))
  taxa_of_physeq <- tax_table(physeq)
  otu_of_physeq <- t(otu_table(physeq))
  data_tbl_taxa <- taxa_of_physeq@.Data
  data_tbl_taxa <- as.data.frame(data_tbl_taxa)
  data_tbl_taxa <- tibble::rownames_to_column(data_tbl_taxa)
  data_tbl_otu <- as.data.frame(otu_of_physeq)
  data_tbl_otu <- tibble::rownames_to_column(data_tbl_otu)
  data_tbl_taxa_otu <- dplyr::full_join(data_tbl_taxa, data_tbl_otu, by = "rowname")
  return(data_tbl_taxa_otu)
}



##### Normalizing Pipeline ####

### STEP 1 ####
# Read in the rds file
# make sure your working directory is pointing to the correct folder!
WashU.UNC.data <- readRDS("~/course documents/fall 2019/Terry's/r scripts/WashU_UNC_CD_NI_ileum_data.rds")

### STEP 1.5 ####
# Separate the dataset to UNC patients and WashU patients
WashU.data <- subset_samples(WashU.UNC.data, sample_data(WashU.UNC.data)$Cohort=="WashU")
WashU.data <- prune_taxa(taxa_sums(WashU.data)>0, WashU.data)
UNC.data <- subset_samples(WashU.UNC.data, sample_data(WashU.UNC.data)$Cohort=="UNC")
UNC.data <- prune_taxa(taxa_sums(UNC.data)>0, UNC.data)


#### STEP 2 ####
# Get phyloseq objects for each taxonomic level (i.e. phylum, class, order, family, genus, species)
# Warning...it may take a while for the lower levels (i.e. Genus, Family), get cookie or something while it runs
WashU.UNC.data.genus <- tax_glom(WashU.UNC.data,"Genus")
WashU.UNC.data.family <- tax_glom(WashU.UNC.data,"Family")
WashU.UNC.data.order <- tax_glom(WashU.UNC.data,"Order")
WashU.UNC.data.class <- tax_glom(WashU.UNC.data,"Class")
WashU.UNC.data.phylum <- tax_glom(WashU.UNC.data,"Phylum")

### NOTES ####
# The following steps are for species level
# Challenge: do the rest~~
# EMAIL IF YOU HAVE PROBLEMS/QUESTIONS!!

#### STEP 3 ####
# Merges otu and taxa tables into a single data frame
# Warning: the larger it is....the longer it takes... (get another cookie)
data.species.table <- mergeTaxaNormOtuCounts(WashU.UNC.data)

### STEP 4 ####
# Concatenate the levels into a single column called Taxa

data.species.table$Taxa <- paste(data.species.table$Phylum,data.species.table$Class, data.species.table$Order, data.species.table$Family, data.species.table$Genus, data.species.table$Species,sep= ".")

#### STEP 5 ####
# Drop unnecessary columns, i.e. rowname, Kingdom, etc
data.species.table.2 <- subset(data.species.table, select = -c(rowname, Kingdom,Phylum, Class,Order,Family, Genus,Species))

#### STEP 6 ####
# Move Taxa column to the front
data.species.table.3 <- data.species.table.2 %>% select(Taxa, everything())

#### STEP 7 ####
#Make Taxa column into the rownames
data.species.table.4 <- data.frame(data.species.table.3, row.names = 1)


#### STEP 8 ####
# Normalize the features (i.e. the OTUs)
patient.species.data.scaled <- apply(data.species.table.4, 1, rescale)

#### STEP 9 #### 
# Save your work!

write.csv(patient.species.data.scaled,"~/course documents/fall 2019/Terry's/normalized data/UNC_WashU_CD_NI_ileum_species_scaled.csv")

##### Now do the same for the genus, family, etc phyloseq objects #####
