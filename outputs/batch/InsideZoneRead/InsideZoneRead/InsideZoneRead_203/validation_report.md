# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_203`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 406: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 406: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
> - Action 'Action_None' range [15-130] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-269] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-176] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-144] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-208] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [32-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [45-113] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [131-200] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [54-142] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [160-195] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-158] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-54] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-252] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-267] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-247] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-53] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-118] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-215] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-145] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-255] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-146] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-269] for track '29' has 3 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.