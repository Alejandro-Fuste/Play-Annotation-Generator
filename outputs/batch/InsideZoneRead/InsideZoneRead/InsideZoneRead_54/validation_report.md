# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_54`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 110: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 110: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 115 frames exceeds threshold 90 frames [start=141, end=255].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '12' (Unknown) duration 93 frames exceeds threshold 90 frames [start=163, end=255].
> - Segment 'Action_BallCarry' for track '13' has invalid range: start=183, end=149. Clamping end to start.
> - Action 'Action_None' range [139-176] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-309] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-336] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-293] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-324] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-173] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-317] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-255] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-337] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-353] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-319] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-448] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [174-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-246] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-343] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-68] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-75] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-85] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-140] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-68] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-137] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [139-145] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-339] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-149] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-305] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-337] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-348] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-190] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-226] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-250] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-305] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-301] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-308] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-427] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-449] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-322] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-315] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-344] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-355] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-330] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-345] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-328] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-408] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-420] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-427] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-440] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-437] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-449] for track '31' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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