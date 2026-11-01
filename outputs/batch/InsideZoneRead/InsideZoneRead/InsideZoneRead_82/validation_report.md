# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_82`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 166: Duplicate assignment for track ID '25' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Overlapping action conflict at frame 364 for track '9': 'Action_BallSnap' vs 'Action_ZoneBlock'. Overriding with 'Action_ZoneBlock'.
> - Action 'Action_ZoneBlock' range [364-422] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-392] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [397-458] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [391-396] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-334] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [364-422] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-424] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-225] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-273] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [364-449] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-52] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-70] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-158] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-440] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-449] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-396] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-430] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-357] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-375] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-399] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-429] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-429] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-466] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [477-509] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-428] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-459] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-446] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-471] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-446] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-467] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-485] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [421-424] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-491] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-474] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-483] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [492-505] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [454-498] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-485] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-497] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-493] for track '33' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.