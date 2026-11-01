# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_217`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_217/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 434: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_BallCarry' for track '10' has invalid range: start=104, end=96. Clamping end to start.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [55–68], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=69.
> - Action 'Action_None' range [55-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-95] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-145] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-110] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-290] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [75-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-171] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [101-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-291] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-126] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-212] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-148] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-194] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-281] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-294] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-298] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-276] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-307] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-284] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-294] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '43' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.