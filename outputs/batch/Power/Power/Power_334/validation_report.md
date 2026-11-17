# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_334`
- **Input XML**: `outputs/batch/Power/Power/Power_334/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 668: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [5-20] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-44] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-174] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-80] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-144] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [61-77] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-37] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-104] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-142] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '23' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.