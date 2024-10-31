# BioInfoPythonScripts

Welcome to BioInfoPythonScripts! This repository is tailored for experienced Python users and contains a personal collection of Python scripts for bioinformatics. Focused on sequencing analysis, data processing, and data visualization, these scripts utilize powerful libraries such as NumPy, pandas, and seaborn. Whether you're working on genome sequencing, RNA-seq data analysis, or complex data visualizations, you'll find useful tools and examples here to enhance your bioinformatics workflows. Dive into efficient, well-documented code designed to tackle real-world bioinformatics challenges.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Scripts](#scripts)
    1. [Data Processing](#data-processing)
    2. [Data Visualization](#data-visualization)
4. [Contributing](#contributing)

## Introduction

This repository provides a collection of Python scripts designed for bioinformatics tasks. The scripts are intended for users who have a solid understanding of Python and are looking to apply their skills to bioinformatics challenges.

## Prerequisites

Before using these scripts, ensure you have the following installed:

- Python 3.6 or higher
- NumPy
- pandas
- seaborn
- Biopython
- Matplotlib
- scikit-learn

You can install these dependencies using pip:

```bash
pip install numpy pandas seaborn biopython matplotlib scikit-learn
```

## Scripts

All the Data used in the scripts can be found here: [Data](https://github.com/dzhao2019/BioInfoPythonScripts/tree/main/Data)

### i.[Data Processing](https://github.com/dzhao2019/BioInfoPythonScripts/tree/main/Data_Processing)
[Example1_Exploring_Data_with_Pandas](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Processing/Example1_Exploring_Data_with_Pandas.py)

[Example2_Basic_Data_selection](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Processing/Example2_Basic_Data_selection.py)

[Example3_Handling_Missing_Data](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Processing/Example3_Handling_Missing_Data.py)

#### [DNA Sequence Data Processing](https://github.com/dzhao2019/BioInfoPythonScripts/tree/main/Data_Processing/DNA%20Sequence%20Data%20Processing)

[Remove_short_contigs_fasta_files_in_a_fold](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Processing/DNA%20Sequence%20Data%20Processing/Remove_short_contigs_fasta_files_in_a_fold.py)

[NCBI_genome_download](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Processing/DNA%20Sequence%20Data%20Processing/NCBI_genome_download.py)

[Extract_contigs_left2remains](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Processing/DNA%20Sequence%20Data%20Processing/Extract_contigs_left2remains.py)

### ii.[Data Visualization](https://github.com/dzhao2019/BioInfoPythonScripts/tree/main/Data_Visualization)

Example1 scatter_plot

![Example1_scatter_plot_Jan Feb Mar_style](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example1_scatter_plot_Jan%20Feb%20Mar_style.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example1_scatter_plot_four%20different%20plots.py)

Example2 Histplot

![Histplot_season_stock]( https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example2-2_Histplot_season_stock.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example2-2_Histplot%20-%20season.py)

Example3_bar_plot

![Example3_bar_plot]( https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example3_bar_plot%20Total%20Rainfall%20per%20Year%20(1960-1969).png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example3_bar_plot.py)

Example4_box_plot monthly vs violin plot

![violin plot](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example4_violin_plot%20monthly%20default%20color.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example4_box_plot%20monthly%20vs%20violin%20plot.py)

Example5_Heatmap

![Heatmap](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example5_Heatmap%20of%20Monthly%20Rainfall%20by%20Year.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example5_Heatmap%20of%20Monthly%20Rainfall%20by%20Year.py)

Example6_FacetGrid

![Example6_FacetGrid](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example6_FacetGrid%20of%20Monthly%20Rainfall%20by%20Decade.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example6_FacetGrid%20of%20Monthly%20Rainfall%20by%20Decade.py)

Example7_catplot box

![Example7_catplot box](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example7_catplot%20box.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example7_catplot%20box.py)

Example8_scatter_plot_customize

![Example8_scatter_plot_customize](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example8_scatter_plot_customize.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example8_scatter_plot_customize.py)

Example9_line plot, violin plot, box plot, and swarm plot

![Example9_line plot, violin plot, box plot, and swarm plot](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example9_line%20plot%2C%20%20violin%20plot%2C%20box%20plot%2C%20and%20swarm%20plot.png) [Script]()

Histograms comparing the rainfall in different time periods

![Heatmap](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Histograms%20comparing%20the%20rainfall%20in%20different%20time%20periods.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Example9_line%20plot%2C%20%20violin%20plot%2C%20box%20plot%2C%20and%20swarm%20plot.py)

violin_plot Summer & Winter in decades

![violin_plot](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/violin_plot%20Summer%20%26%20Winter%20in%20decades.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/violin_plot%20Summer%20%26%20Winter%20in%20decades.py)

Cluster Heatmap of Seasonal Rainfall

![Cluster Heatmap](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Cluster%20Heatmap%20of%20Seasonal%20Rainfall.png) [Script](https://github.com/dzhao2019/BioInfoPythonScripts/blob/main/Data_Visualization/Cluster%20Heatmap%20of%20Seasonal%20Rainfall.py)

## Contributing
Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!
