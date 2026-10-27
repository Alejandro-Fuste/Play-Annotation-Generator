# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_15`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '14' (LT) duration 100 frames exceeds threshold 90 frames [start=20, end=119].
> - Action 'Action_None' range [17-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [51-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-131] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [20-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [47-49] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [54-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [20-37] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-90] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-56] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-85] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 17, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [17-22] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [20-93] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [104-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [113-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [24-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [30-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-117] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.