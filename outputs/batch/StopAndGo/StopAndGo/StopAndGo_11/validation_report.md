# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_11`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [25–41], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=42.
> - Action 'Action_RunGoRoute' range [112-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-230] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-177] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-73] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-111] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-196] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [221-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-51] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-69] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-180] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [184-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-188] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-63] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-71] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-189] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [191-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [195-199] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-194] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [67-141] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-98] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-118] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-200] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-187] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-205] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '35' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.