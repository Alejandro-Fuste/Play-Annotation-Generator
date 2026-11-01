# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_246`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_246/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 492: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 0 for track '11': 'Action_BallSnap' vs 'Action_ZoneBlock'. Overriding with 'Action_ZoneBlock'.
> - Action 'Action_None' range [0-39] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-66] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [45-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-35] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-80] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-35] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [0-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [0-39] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [0-13] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-17] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-22] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-148] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-2] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-52] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '21' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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