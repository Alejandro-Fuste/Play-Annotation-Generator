# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_87`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 174: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [26–39], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=40.
> - Action 'Action_None' range [26-66] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-64] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-65] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-88] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-213] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-189] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '22' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.