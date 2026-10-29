# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_33`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 658 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 658 as fallback play end.
> - Action 'Action_PreSnap' range [0-545] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-527] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [537-540] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [553-556] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-547] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-553] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [556-612] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-551] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [553-554] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [558-559] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [563-564] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-593] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-628] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [633-636] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [644-648] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-513] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [516-658] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-553] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [558-658] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-600] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [609-614] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-642] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-658] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-658] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-579] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [596-600] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-560] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-301] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-308] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-314] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-520] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-312] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-339] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-658] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [534-535] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [551-658] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [543-558] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [549-554] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [554-558] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [560-658] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [562-609] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [613-614] for track '28' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.