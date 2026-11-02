# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_130`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_130/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 261: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
> - Validation warning: Action 'Action_LeadBlock' for track '4' (RB) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
> - Segment 'Action_ZoneBlock' for track '6' has invalid range: start=18, end=15. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
> - Action 'Action_None' range [16-50] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-115] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [18-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-192] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [16-21] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [25-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-112] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [45-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-127] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.