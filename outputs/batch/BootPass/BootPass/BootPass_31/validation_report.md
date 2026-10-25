# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_31`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [16–40], lower_priority='Action_RunBlock' annotated_start=27, effective_Action_RunBlock_start=41.
> - Action 'Action_None' range [16-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [27-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-182] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-39] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [27-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [27-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-103] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [16-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [57-62] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [64-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [27-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-110] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-20] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-105] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-120] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-103] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-108] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-177] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '35' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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