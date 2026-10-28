# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_14`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 30: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [38–52], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=53.
> - Action 'Action_None' range [38-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-230] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-119] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-141] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-225] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [38-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [140-163] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-212] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-54] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [59-87] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-189] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-239] for track '20' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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