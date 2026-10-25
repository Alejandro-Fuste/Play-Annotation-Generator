# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_93`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 166: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [96–101], lower_priority='Action_RunBlock' annotated_start=101, effective_Action_RunBlock_start=102.
> - Action 'Action_None' range [96-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-222] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-214] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-236] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-269] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [223-232] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [234-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-245] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [102-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [122-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [147-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [202-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [216-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [221-222] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-237] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [185-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [188-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-259] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '32' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.