# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_167`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_167/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 334: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 97 frames exceeds threshold 90 frames [start=36, end=132].
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 97 frames exceeds threshold 90 frames [start=36, end=132].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 97 frames exceeds threshold 90 frames [start=36, end=132].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 97 frames exceeds threshold 90 frames [start=36, end=132].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (C) duration 97 frames exceeds threshold 90 frames [start=36, end=132].
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [33–45], lower_priority='Action_ZoneBlock' annotated_start=36, effective_Action_ZoneBlock_start=46.
> - Action 'Action_ZoneBlock' range [36-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [74-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-105] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-74] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-223] for track '18' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.