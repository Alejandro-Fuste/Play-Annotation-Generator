# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_124`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 40 |
| Ball Tracks | 2 |
| CSV events parsed | 16 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 250: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 250: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [397–411], lower_priority='Action_DownBlock' annotated_start=400, effective_Action_DownBlock_start=412.
> - Action 'Action_None' range [444-451] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-557] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [397-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-577] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-478] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [491-493] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-629] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-504] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-458] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [464-466] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-480] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-486] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-399] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-520] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-522] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-586] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-596] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-431] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [443-450] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-464] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-473] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-457] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-289] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [442-506] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-460] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-474] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-491] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-628] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-470] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-487] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-629] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-477] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [479-482] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-486] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-492] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-599] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-625] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [489-493] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-514] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-508] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-550] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-572] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-579] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-541] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-573] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-625] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-586] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-590] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-602] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [615-617] for track '41' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.