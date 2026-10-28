# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_93`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 186: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [32–48], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=49.
> - Action 'Action_None' range [146-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-65] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-190] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-94] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-89] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-146] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-238] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.