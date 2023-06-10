The ```SMaSH``` (Scalable Marker gene Signal Hunter) framework is a general, scalable codebase for calculating marker genes from single-cell RNA-sequencing data for a variety of different cell annotations as provided by the user, using supervised machine learning approaches.  These annotations can be truly general: they can be broad cell types/clusters, detailed sub-types of different broad clusters, cell organ of origin, whether the cell inhabits tumour tissue, surrounding microenvironment, or healthy tissue, and more besides. ```SMaSH``` implements marker gene extraction using four different models (Random Forest, Balanced Random Forest, XGBoost, and a deep neural network) and two different information gain metrics (Gini impurity for the ensemble learners, and Shapley value for the neural network). For some details on the ```SMaSH``` implementation please consult our pre-print: https://www.biorxiv.org/content/10.1101/2021.04.08.438978v1, or visit our GitLab repository: https://gitlab.com/cvejic-group/smash. ```SMaSH``` is integrated with the ```ScanPy``` framework, working directly from the ```AnnData``` object of RNA-sequencing counts and a vector of user-defined annotations for each cell according to the marker gene extraction problem. 


We're always happy to hear of any suggestions, issues, bug reports, and possible ideas for collaboration.

- Simone Riva <simo.riva15@gmail.com>, <sgr34@cam.ac.uk>, <sr31@sanger.ac.uk> (University of Cambridge, and Wellcome Sanger Institute) 

- Mike Nelson <nelson@ebi.ac.uk> (University of Cambridge, and EMBL-EBI)
