# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_99`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 118 |
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
> - Action 'Action_PreSnap' range [0-100] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-166] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-83] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-140] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-126] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-127] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [59-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-74] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-73] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-78] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-145] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-157] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-28] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-39] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-121] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-180] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-139] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-148] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-170] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '33' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.