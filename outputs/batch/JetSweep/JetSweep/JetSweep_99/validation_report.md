# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_99`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 200: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [55–68], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=69.
> - Action 'Action_None' range [55-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-161] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [85-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-155] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-43] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [55-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-209] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-153] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-190] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '29' has 1 frames without a visible bounding box.
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