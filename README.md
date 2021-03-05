# PHYLIP-matrix-visualizer

This small program creates a network visualiser from a PHYLIP distance matrix (see: <http://bioinformatics.org.au/tools/AFnetwork> for an example network visualisation). This is done by generating a html page that contains the nesseccary information from the matrix file to create the network visualiser.

To run the program, all you need to do is provide the path to the phylip matrix as well as the output path for the new html page. A title for the html page may also be optinally provided. An example usage of the `create_vis.py` script is shown below.

```bash
python3.7 create_vis.py --phylip_path ./data/sample.txt --output_path ./test.html
```

The scripts usage is summaried in the output of running `create_vis.py` with the help flag switched on. To view the network visualiser, simply open the generated html file in a web browser of choice.

NOTE: The generated html file must be run in the same directory as the `support_files` included in this repository.
