# JCStreetSweepMap

This is a project to catalog and map all parking rules related to street sweeping 
in Jersey City.

## Street Rule Map Website
The data is displayed in an online map at the url [jcstreetsweep.com](jcstreetsweep.com). It uses Leaflet and JQuery to generate a map with clickable curblines on every street. Once clicked, a popup is displayed with the associated rule presented to the user is a sentence-like structure.

## Disclaimers
* This project is not associated with the City of Jersey City. It is an independent project by a resident intended to make hard to find information more accessible.
* This data will not provide information regarding other kinds of parking rules.
For example, if a street has a sign stating "No parking at all times", this
map will not have that information.
* Data may not be 100% accurate. Always consult posted signs when making a decision
about where to park. Please help report any errors.
* This project is not associated with the City of Jersey City. It is an independent project by a resident intended to make hard to find information more accessible.

## Street Sign Data Format
Information about when parking is not allowed is associated with a length of curb. Each curb length typically starts and ends at an intersection with another street. Each street has two curb lengths on either side. This is an attempt to represent these curbs, and associated rules, digitally.

The data structure follows the [SharedStreets](sharedstreets.io) [CurbLR standard](github.com/sharedstreets/curblr) in GeoJSON.

An example with Abbett St:
```javascript
{
   "type":"Feature",
   "geometry":{
      "type":"LineString",
      "coordinates":[
         [
            -74.05006170272826,
            40.740876077958994
         ],
         [
            -74.04990077018736,
            40.74105897808468
         ]
      ]
   },
   "properties":{
      "location":{
         "sideOfStreet":"west",
         "marker":"sign",
         "streetName":"Abbett St"
      },
      "regulations":[
         {
            "rule":{
               "activity":"no parking",
               "reason":"street cleaning"
            },
            "timeSpans":[
               {
                  "daysOfWeek":[
                     "mo",
                     "th"
                  ],
                  "timesOfDay":[
                     {
                        "from":"13:00",
                        "to":"15:00"
                     }
                  ]
               }
            ],
            "priority":3
         }
      ]
   }
}
```
## Data Sources
Data used in the map was a combination of the following sources:
* Primary research through walking and recording street sign information
* The [Jersey City Code of Ordinances](https://library.municode.com/nj/jersey_city/codes/code_of_ordinances?nodeId=CH332VETR_ARTIIIPASTST), Article II Section 332-31 related to no parking rules for street cleaning purposes
* Google Maps Street View
