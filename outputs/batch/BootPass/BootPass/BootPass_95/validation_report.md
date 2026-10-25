# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_95`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 128 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [8–24], lower_priority='Action_RunBlock' annotated_start=16, effective_Action_RunBlock_start=25.
> - Action 'Action_None' range [8-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-36] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-38] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-231] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-265] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-100] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [81-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [16-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [69-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [16-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [83-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [93-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [100-269] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [16-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [39-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [66-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [70-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [154-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [8-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [18-24] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [25-75] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-105] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [107-112] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [115-149] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [16-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-115] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [117-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-92] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-103] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-173] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-223] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-245] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-247] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '38' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.