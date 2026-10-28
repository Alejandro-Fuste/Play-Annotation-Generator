# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_28`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [103–117], lower_priority='Action_PassBlock' annotated_start=106, effective_Action_PassBlock_start=118.
> - Action 'Action_PassBlock' range [106-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-257] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-271] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-42] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-270] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [145-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-311] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-162] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-241] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '22' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.