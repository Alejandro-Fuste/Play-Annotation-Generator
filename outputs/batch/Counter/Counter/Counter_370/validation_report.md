# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_370`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_370/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 742: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [40–52], lower_priority='Action_PullBlock' annotated_start=43, effective_Action_PullBlock_start=53.
> - Action 'Action_None' range [40-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-110] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-172] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [40-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-157] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [43-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '9' starts at frame 77, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [77-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-149] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [40-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [63-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-106] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-80] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' for track '13' starts at frame 43, but the player has no visible bounding box on this frame.
> - Action 'Action_PullLeadBlock' range [43-69] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [76-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [80-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [90-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [45-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [103-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-157] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '26' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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