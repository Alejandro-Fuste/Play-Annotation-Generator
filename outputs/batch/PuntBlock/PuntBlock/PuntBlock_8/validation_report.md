# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_8`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 18: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [15-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [67-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [77-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-93] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-193] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-131] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-190] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '31' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.