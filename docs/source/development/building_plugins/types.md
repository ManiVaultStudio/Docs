# Plugin types
In order to extend the functionality of the ManiVault system, it is possible to write your own plug-ins and add them to the system.

Below are six types of plugins which are currently supported in **ManiVault**. For each plugin type, we have created [example plugins](https://github.com/ManiVaultStudio/ExamplePlugins) which can serve as a starting point for creating your own plugin:

## View
This plugin type is specifically targeted at visualization of some data. Examples of such plugins would be:
* A scatter plot
* An image viewer
* A 3D volume viewer
* A chart or histogram

Our example plugins repository contains an example [view plugin](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master/ExampleView).

## Analysis
This type is used for controlled computations. These plugins have no direct visual output (although their output can be visualized with a View Plugin), but are purely concerned with transformation of input data or generation of new data. Examples of such plugins would be:
* Generating a t-SNE embedding from input data
* Computing clusters of data
* Generating random points
* Subsampling input data

Our example plugins repository contains an example [analysis plugin](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master/ExampleAnalysis).

## Data
This type provides a raw data store and a view on this data. It defines a type derived from [RawData]() which contains the actual data. In addition it defines a type derived from [Set]() which provides an indexed subset of the data and is what gets passed to all interested plugins.

Examples of data plugins would be:
* Point data
* Image data
* Volume data

Our example plugins repository contains an example [data plugin](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master/ExampleData).

__Be aware that in most cases it will not be necessary to write a Data Plugin. Many types of data can be stored as Point Data which is available by default in the library.__

## Loader
This IO plugin type is used for loading data into the system. It automatically gets added to the menu options and once triggered will launch the logic defined in the plugin for loading the appropriate data. Typical implementations launch a file explorer window to select the file the user wants to load, then processes it to be in the desired format and passes the data to the core system where it is stored in the central data manager.

Examples of loader plugins would be:
* A CSV loader
* An image loader
* A binary file loader

Our example plugins repository contains an example [loader plugin](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master/ExampleLoader).

## Writer
This IO plugin type  is used for writing data from the system to disk. It automatically gets added to the menu options and once triggered will launch the logic defined in the plugin for writing the data. Typical implementations launch a file explorer window to decide under which file name and where the data will be saved, then prepares the data into the desired output format and saves it to disk.

Examples of writer plugins would be:
* A CSV writer
* An image writer
* A binary file writer

Our example plugins repository contains an example [writer plugin](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master/ExampleWriter).

## Transformation
A **transformation** plugin is used for transforming data, either by chaging the data in-place, or by generating a new dataset.

Examples of transformation plugins would be:
* An arc-sin image transform
* Data transposition

Our example plugins repository contains an example [transformation plugin](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master/ExampleTransformation).

## Setting up the plugin
The easiest way to set up your new plugin is to build on one of the example projects listed above. Each of these projects contains a main plugin class, which extends from one of the base plugin classes (ViewPlugin, AnalysisPlugin, etc.). In addition, a plugin factory is defined which is reponsible for initializing the plugin itself.
