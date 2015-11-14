# Arrest Blotter Map

This map displays arrest information geographically. It uses public information from the Johnson County blotter. Each row is an arrest record with attributes: Name, Home Address, Arrest Address, Date of Birth, Date of Arrest, Incident #, and Charges. Python is used to scrape, geocode (Google API), and format the data. Mapzen graciously allows downloads of their mapping files. D3.js provides the framework to visualize the arrests as nodes on an interactive map. The names and home addresses are absent from the visualization. If I'm missing anything, or have gotten something mixed up please open up an issue and I'll take a look!

**View live here:** [Interactive version](https://myweb.uiowa.edu/rlrson/portfolio/arrests/arrests.html)

##### Example animation of the dataset
![alt tag](https://raw.github.com/ryan-p-larson/arrests/master/examples/arrests.gif)

#### Dependencies
This viz requires the following to be able to clone and hit make for a one step install:
* Make (to compile)
* Curl (to download the shapefile zip)
* ogr2ogr (.shp -> geojson)
* TopoJSON (geojson -> json)
* Python (I used 2.7, but it can be done with 3.4)
* D3.js

#### Installation
1. Make a folder where you can clone the repo.
2. Clone the repo
3. `cd arrests`
4. `make`

That's it. The makefiles will take care of the rest for you, provided you have internet. Python will try to fire up the index.html at localhost:8888, check it out!
