# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_237`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_237/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 474: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [19–31], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=32.
> - Action 'Action_None' range [19-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-67] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [59-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-87] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [88-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' for track '18' starts at frame 48, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockSecondLevel' range [48-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-87] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-131] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '29' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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