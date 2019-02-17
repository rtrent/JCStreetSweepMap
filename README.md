# JCStreetSweepMap

This project is to catalog and map all parking rules related to street sweeping 
in Jersey City. My initial pass of this has focused on Downtown.

This data will not provide information regarding other kinds of parking rules.
For example, if a street has a sign stating "No parking at all times", this
map will not have that information.

Data may not be 100% accurate. Always consult posted signs when making a decision
about where to park. Please help report any errors.

## Street Sign Data Format
Information about when parking is / is not allowed is associated with a length of
curb. Each curb length typically starts and ends at an intersection with another
street. A street has two curb sections on either side.

**The data structure captures the following information for each curb:**
* street name
* street name suffix (st, rd, ave, etc)
* sign title (what the rule is about)
* start time (when no parking time period begins)
* end time (when no parking time period ends)
* sign days (which days this rule applies)
* neighborhood name (which neighborhood this street segment is in)
* other rules (a catch all if the format cannot properly describe all rules)

An example with Brunswick St in Van Vorst Park:
```javascript
      "properties": {
        "street_name": "Brunswick",
        "street_suffix": "St",
        "sign_title": "Street Sweeping",
        "start_time": 13,
        "end_time": 15,
        "sign_days": [
          "M",
          "Th"
        ],
        "neighborhood_name": "Van Vorst Park",
        "other_rules": ""
```
## Data Sources
Data used in the map was a combination of the following sources:
* Walking and personally recording physical street signs
* [Jersey City Ordinance](https://library.municode.com/nj/jersey_city/codes/code_of_ordinances?nodeId=CH332VETR_ARTIIIPASTST) related to parking
* Google Maps Street View (typically for double checking)
