# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_70`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BootAway' for track '8' has invalid range: start=98, end=91. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '8' has invalid range: start=156, end=91. Clamping end to start.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [58–72], lower_priority='Action_RunBlock' annotated_start=68, effective_Action_RunBlock_start=73.
> - Action 'Action_RunBlock' range [68-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [68-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [83-172] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [175-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [68-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [82-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-154] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-198] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [68-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [94-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-4] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-11] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-172] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-225] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-239] for track '20' has 1 frames without a visible bounding box.
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
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.