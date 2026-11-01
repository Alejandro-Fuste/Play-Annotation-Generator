# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_280`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_280/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 560: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '7' has invalid range: start=60, end=53. Clamping end to start.
> - Segment 'Action_BallSnap' for track '16' has invalid range: start=32, end=29. Clamping end to start.
> - Action 'Action_None' range [15-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-34] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-33] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-46] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [40-53] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-47] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-93] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-29] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-111] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [30-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '26' has 3 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.