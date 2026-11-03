# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_45`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [11–26], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=27.
> - Action 'Action_None' range [11-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [93-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-185] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-197] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [194-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-130] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [134-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-53] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-137] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '35' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.