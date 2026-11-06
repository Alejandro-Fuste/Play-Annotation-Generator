# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_109`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [9–26], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=27.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [9–26], lower_priority='Action_BlockSecondLevel' annotated_start=20, effective_Action_BlockSecondLevel_start=27.
> - Action 'Action_None' range [9-189] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-105] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-161] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-190] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-15] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-61] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-160] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-202] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [9-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [22-24] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-60] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-146] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-13] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 12, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [12-12] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-201] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-80] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-106] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.