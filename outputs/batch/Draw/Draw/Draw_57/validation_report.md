# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_57`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [41–51], lower_priority='Action_PassBlock' annotated_start=44, effective_Action_PassBlock_start=52.
> - Action 'Action_None' range [41-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-199] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-182] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [83-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-235] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-110] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.