# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_258`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_258/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [0–13], lower_priority='Action_ZoneBlock' annotated_start=3, effective_Action_ZoneBlock_start=14.
> - Action 'Action_None' range [0-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [49-97] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [3-19] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-41] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-226] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [3-40] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-62] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 71, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [71-97] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [0-345] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-252] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-302] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-320] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-201] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-259] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [221-356] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-270] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-300] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-317] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-258] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-297] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-315] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-305] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-318] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '34' has 1 frames without a visible bounding box.
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