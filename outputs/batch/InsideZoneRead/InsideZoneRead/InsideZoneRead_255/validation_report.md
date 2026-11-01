# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_255`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_255/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 510: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [18–33], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=34.
> - Action 'Action_None' range [18-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-83] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [66-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [83-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [102-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-63] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-130] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-95] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-39] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-123] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '27' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.