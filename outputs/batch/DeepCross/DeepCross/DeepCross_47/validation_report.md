# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_47`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [19–33], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=34.
> - Action 'Action_None' range [19-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-227] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-267] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-208] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-52] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-121] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [155-171] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-53] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-164] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [168-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [186-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-120] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-132] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-200] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '32' has 1 frames without a visible bounding box.
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