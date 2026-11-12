# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_45`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 156 frames exceeds threshold 90 frames [start=111, end=266].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 156 frames exceeds threshold 90 frames [start=111, end=266].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 156 frames exceeds threshold 90 frames [start=111, end=266].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [108–120], lower_priority='Action_ZoneBlock' annotated_start=111, effective_Action_ZoneBlock_start=121.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '20' (RG) duration 136 frames exceeds threshold 90 frames [start=131, end=266].
> - Action 'Action_None' range [108-253] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [115-214] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-215] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-296] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-200] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [202-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '28' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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