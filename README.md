# Arrest Blotter Map
This is the repository of a crime visualization. It is being made by scraping arrest blotters and caching the information. After being cleaned, the addresses are geocoded. Ideally the locations will be displayed on a map. This is a work in progress.

![alt tag](https://raw.github.com/ryan-p-larson/arrests/master/examples/arrests.gif)

#### Dependencies
This viz requires the following to be able to clone and hit make for a one step install:

* Make (to compile)
* Curl (to download the shapefile zip)
* ogr2ogr (.shp -> geojson)
* TopoJSON (geojson -> json)
* Python (I used 2.7, but it can be done with 3.4)
* D3.js
