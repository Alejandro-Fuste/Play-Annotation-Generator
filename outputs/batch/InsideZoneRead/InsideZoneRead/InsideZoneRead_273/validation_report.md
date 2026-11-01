# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_273`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_273/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 546: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [8–23], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=24.
> - Action 'Action_None' range [8-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-65] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [54-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-98] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-91] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-33] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-48] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-79] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-128] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-157] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-170] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '35' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.