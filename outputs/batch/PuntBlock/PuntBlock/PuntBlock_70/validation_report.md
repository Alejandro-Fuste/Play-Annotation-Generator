# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_70`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [58-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-161] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [58-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [94-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [101-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-42] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-43] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-75] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-155] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-15] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-18] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-121] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [125-132] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-13] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-143] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-61] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-105] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-13] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-173] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-7] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-139] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-109] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-164] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '34' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.