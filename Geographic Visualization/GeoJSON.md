# GeoJSON

GeoJSON is a geospatial data interchange format. This is a very commonly used format.
It defines several types of JSON objects and the manner in which they are combined to represent data about geographic features, their properties, and their spatial extents. GeoJSON uses a geographic coordinate reference system, World Geodetic System 1984, and units of decimal degrees.

## Link to Specification
https://tools.ietf.org/html/rfc7946

## Example JSON
In this we have an object of type FeatureCollection and it contains an array of features. In each feature there can be many properties which might be relevant to the data you might be working with, but from a geoJSON perspective it is not important.
The Geometry object with its coordinates on [long, lat, alt] is what mostly we work with.
Note: In most google maps api it is generally {lat, long} which is in different order and can sometimes create issues.

```JSON
{
  "type":"FeatureCollection",
  "features":[
    {
      "type":"Feature",
      "properties": {
        "mag": 5.4,
        "place": "48km SSE of Pondaguitan, Philippines",
        "time":1348176066,"tz":480,
        "url":"http://earthquake.usgs.gov/earthquakes/eventpage/usc000csx3",
        "felt":2,"cdi":3.4,"mmi":null,"alert":null,"status":"REVIEWED",
        "tsunami":null,"sig":"449","net":"us","code":"c000csx3",
        "ids":",usc000csx3,",
        "sources":",us,",
        "types":""
      },
      "geometry": {
        "type":"Point",
        "coordinates":[126.3832,5.9775,111.16]
      },
      "id":"usc000csx3"
    }
  ]
}

```
