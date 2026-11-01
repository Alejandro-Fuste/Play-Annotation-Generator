# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_110`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_110/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 222: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=47.
> - Action 'Action_None' range [31-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [61-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [76-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [80-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [86-99] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [31-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [54-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-109] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '21' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.