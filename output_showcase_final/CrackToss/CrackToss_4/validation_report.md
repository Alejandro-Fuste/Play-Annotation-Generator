# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_4`
- **Input XML**: `output_showcase_final/CrackToss/CrackToss_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 10: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 10: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Segment 'Action_SnapReceive' for track '19' has invalid range: start=110, end=23. Clamping end to start.
> - Segment 'Action_Toss' for track '19' has invalid range: start=119, end=23. Clamping end to start.
> - Action 'Action_None' range [110-212] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-211] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [147-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-249] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [168-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 113, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [113-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-20] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-230] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-268] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-265] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.