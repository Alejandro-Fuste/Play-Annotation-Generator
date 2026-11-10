# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_204`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_204/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '14' has invalid range: start=59, end=53. Clamping end to start.
> - Action 'Action_None' range [58-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-87] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-129] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-198] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-202] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-38] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-10] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-20] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-147] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-167] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '38' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.