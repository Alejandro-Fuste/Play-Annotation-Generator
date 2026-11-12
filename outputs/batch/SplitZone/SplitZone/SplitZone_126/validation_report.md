# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_126`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 254: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 118 frames exceeds threshold 90 frames [start=34, end=151].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 120 frames exceeds threshold 90 frames [start=34, end=153].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [31–47], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=48.
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 120 frames exceeds threshold 90 frames [start=34, end=153].
> - Action 'Action_None' range [31-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [57-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-145] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-62] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-82] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '21' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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