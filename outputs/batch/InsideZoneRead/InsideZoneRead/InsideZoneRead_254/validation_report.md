# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_254`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_254/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 508: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 508: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=24.
> - Action 'Action_None' range [10-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-48] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [53-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-156] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [10-195] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [10-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-74] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-37] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-26] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-207] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.