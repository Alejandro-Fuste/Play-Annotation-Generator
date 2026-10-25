# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_69`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [37–51], lower_priority='Action_RunBlock' annotated_start=45, effective_Action_RunBlock_start=52.
> - Action 'Action_None' range [187-206] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-114] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-160] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-197] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-156] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-198] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-129] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [52-197] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [208-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-124] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [139-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [80-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [103-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [107-194] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [196-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-72] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-175] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-191] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '37' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.