# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_323`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_323/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [4-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [7-37] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-29] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-47] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-60] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.