# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_78`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 158: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [284–301], lower_priority='Action_ZoneBlock' annotated_start=287, effective_Action_ZoneBlock_start=302.
> - Action 'Action_PreSnap' range [15-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-383] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-479] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [287-371] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-348] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-373] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-405] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-415] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [292-371] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-326] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-408] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [327-474] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-314] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-345] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [347-350] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-479] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-323] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-391] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-416] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-413] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [415-464] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-295] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-412] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-223] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-405] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-438] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-479] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-408] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-352] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-357] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-415] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-457] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-471] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [421-479] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-464] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-473] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-451] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-468] for track '28' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.