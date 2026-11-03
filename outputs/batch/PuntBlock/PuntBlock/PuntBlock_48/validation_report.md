# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_48`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 70 |
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
> - Action 'Action_PuntBall' range [51-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [64-68] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [76-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [122-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [128-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-138] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-180] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [60-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-115] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-58] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-82] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-180] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.