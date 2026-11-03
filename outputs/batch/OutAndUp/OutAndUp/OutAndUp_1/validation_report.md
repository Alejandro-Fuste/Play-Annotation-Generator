# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_1`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
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
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=35.
> - Action 'Action_None' range [21-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-169] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-51] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-61] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [103-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-41] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-89] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [182-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [191-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [198-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-73] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-88] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-207] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-94] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-61] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-143] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-182] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
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