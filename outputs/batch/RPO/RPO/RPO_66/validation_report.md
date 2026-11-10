# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_66`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 36 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 122: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-27] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [29-67] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-71] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-192] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-168] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-206] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-206] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.