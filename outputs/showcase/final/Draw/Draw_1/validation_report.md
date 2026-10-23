# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_1`
- **Input XML**: `output_showcase_final/Draw/Draw_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_PassBlock' annotated_start=70, effective_Action_PassBlock_start=81.
> - Action 'Action_None' range [68-172] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-102] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-245] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-245] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-269] for track '13' has 6 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [118-148] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-214] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-269] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-117] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-221] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-244] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-208] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-244] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-128] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-246] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-261] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.