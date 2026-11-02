# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_178`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_178/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 358: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [47–59], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=60.
> - Action 'Action_None' range [47-196] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-106] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [47-153] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-185] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-200] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 93, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [93-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 93, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [93-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_Toss' range [66-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-111] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-24] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-75] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-46] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [49-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-197] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [63-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-108] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-127] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-134] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-186] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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