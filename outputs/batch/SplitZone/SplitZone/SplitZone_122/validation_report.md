# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_122`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_122/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 246: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 117 frames exceeds threshold 90 frames [start=40, end=156].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 117 frames exceeds threshold 90 frames [start=40, end=156].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 117 frames exceeds threshold 90 frames [start=40, end=156].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [37–54], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=55.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [37–54], lower_priority='Action_BlockSecondLevel' annotated_start=49, effective_Action_BlockSecondLevel_start=55.
> - Action 'Action_BallCarry' range [71-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-155] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [37-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [42-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-214] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-249] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [55-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [108-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-30] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-242] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-186] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-187] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-262] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-265] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.