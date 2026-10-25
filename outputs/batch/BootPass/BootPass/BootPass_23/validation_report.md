# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_23`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 45: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 46: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [40–52], lower_priority='Action_RunBlock' annotated_start=47, effective_Action_RunBlock_start=53.
> - Action 'Action_None' range [40-241] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-260] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-135] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-135] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-113] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [40-180] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-118] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [53-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-235] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-178] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-249] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-269] for track '30' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.