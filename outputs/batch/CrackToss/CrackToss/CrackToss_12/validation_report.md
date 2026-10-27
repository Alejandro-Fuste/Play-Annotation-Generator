# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_12`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 25: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 26: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 26: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [48-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [51-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [73-87] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [51-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-70] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-88] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-117] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-100] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-208] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-111] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-171] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-203] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-105] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-207] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.