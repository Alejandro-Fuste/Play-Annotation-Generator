# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_137`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_137/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 276: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 94 frames exceeds threshold 90 frames [start=104, end=197].
> - Validation warning: Action 'Action_LeadBlock' for track '14' (QB) duration 94 frames exceeds threshold 90 frames [start=104, end=197].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [102–113], lower_priority='Action_ZoneBlock' annotated_start=104, effective_Action_ZoneBlock_start=114.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 94 frames exceeds threshold 90 frames [start=104, end=197].
> - Action 'Action_None' range [102-231] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-249] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-188] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-168] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [104-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-139] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-231] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-224] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-269] for track '29' has 1 frames without a visible bounding box.
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