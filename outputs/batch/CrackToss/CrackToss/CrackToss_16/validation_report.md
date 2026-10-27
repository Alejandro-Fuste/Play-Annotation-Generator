# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_16`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (LT) duration 104 frames exceeds threshold 90 frames [start=47, end=150].
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=52, end=47. Clamping end to start.
> - Action 'Action_PreSnap' range [0-76] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [47-73] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-83] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [85-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [47-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [78-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-159] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-51] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-95] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-96] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-63] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-106] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [43-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-140] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-180] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-108] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-135] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-130] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-145] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-168] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '32' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.