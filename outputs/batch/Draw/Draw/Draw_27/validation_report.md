# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_27`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
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
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [11–25], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=26.
> - Action 'Action_None' range [11-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-208] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-219] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [11-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-46] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-223] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [11-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [170-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '34' has 1 frames without a visible bounding box.
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