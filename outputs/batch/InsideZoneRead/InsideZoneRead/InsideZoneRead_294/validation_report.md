# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_294`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_294/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 588: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [22–35], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=36.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
> - Action 'Action_None' range [22-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-48] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-76] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-130] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [179-204] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-54] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [22-140] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-43] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-169] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-185] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '31' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.