# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_13`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [8–20], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=21.
> - Action 'Action_None' range [8-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [20-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [94-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-202] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-39] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-169] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-201] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-136] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-63] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-87] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-157] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-107] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-26] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-169] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [179-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-46] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-62] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-74] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-169] for track '19' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-27] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-31] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-49] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-82] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-164] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-94] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-158] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '37' has 1 frames without a visible bounding box.
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