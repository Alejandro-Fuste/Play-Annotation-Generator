# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_310`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_310/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 622: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [52–65], lower_priority='Action_DownBlock' annotated_start=55, effective_Action_DownBlock_start=66.
> - Action 'Action_PreSnap' range [0-40] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [55-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-186] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-195] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-134] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [55-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-126] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-154] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-190] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '27' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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