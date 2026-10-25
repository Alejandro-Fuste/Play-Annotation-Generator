# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_75`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [52–67], lower_priority='Action_RunBlock' annotated_start=59, effective_Action_RunBlock_start=68.
> - Action 'Action_None' range [185-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-75] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [59-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-179] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-229] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [59-236] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [59-177] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [179-186] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [190-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [195-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [59-70] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-208] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-223] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.