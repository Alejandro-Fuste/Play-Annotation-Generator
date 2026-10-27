# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_66`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 134: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 134: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [29-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [32-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [42-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-91] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-101] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-113] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-52] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-62] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [32-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [41-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-10] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-12] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-150] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [31-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-91] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-91] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-109] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-106] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.