# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_97`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_KickBall' range [43-50] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-91] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-88] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-101] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-115] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-117] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-132] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-42] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-93] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-116] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-157] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-118] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-116] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-115] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-128] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-169] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '31' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.