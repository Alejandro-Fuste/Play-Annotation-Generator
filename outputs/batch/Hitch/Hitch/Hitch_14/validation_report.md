# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_14`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [1–16], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=17.
> - Action 'Action_None' range [1-127] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-191] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-136] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-28] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-45] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-48] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-125] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-107] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-37] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-47] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-152] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '33' has 1 frames without a visible bounding box.
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