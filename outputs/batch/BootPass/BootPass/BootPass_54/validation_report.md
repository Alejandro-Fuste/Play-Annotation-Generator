# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_54`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [40–57], lower_priority='Action_RunBlock' annotated_start=47, effective_Action_RunBlock_start=58.
> - Action 'Action_None' range [40-149] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [129-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-191] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [58-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [68-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-204] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-215] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '27' has 1 frames without a visible bounding box.
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