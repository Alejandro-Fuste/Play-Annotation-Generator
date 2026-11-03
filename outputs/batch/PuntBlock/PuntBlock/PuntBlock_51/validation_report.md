# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_51`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 112 |
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
> - Segment 'Action_SecureRecovery' for track '2' has invalid range: start=174, end=78. Clamping end to start.
> - Action 'Action_None' range [1-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-105] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-66] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [62-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-71] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-78] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-39] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-23] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [1-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-66] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-61] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-63] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-149] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-70] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-74] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-74] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-135] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-105] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-125] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-124] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-132] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-148] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-178] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-125] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-176] for track '36' has 2 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.