# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_170`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_170/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 124 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 340: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 340: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 96 frames exceeds threshold 90 frames [start=410, end=505].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [408–422], lower_priority='Action_ZoneBlock' annotated_start=410, effective_Action_ZoneBlock_start=423.
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 96 frames exceeds threshold 90 frames [start=410, end=505].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 96 frames exceeds threshold 90 frames [start=410, end=505].
> - Action 'Action_None' range [408-629] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-610] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-487] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-513] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-517] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-526] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-449] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-464] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [469-470] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-487] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-504] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-563] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [598-599] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [602-618] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-594] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [408-607] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [610-613] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [616-618] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-629] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-611] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-492] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-508] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [410-431] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-459] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-501] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-616] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-622] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-436] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [423-430] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-581] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-584] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-590] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-562] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-407] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-549] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [553-559] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-588] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [590-629] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [410-505] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-613] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-280] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-520] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-500] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-22] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-481] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [410-464] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-10] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-328] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-340] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-388] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-396] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-407] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-416] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [424-430] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-441] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-462] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-482] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-537] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-543] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-606] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-446] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-451] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-478] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-489] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-551] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [553-603] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [612-613] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-604] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-511] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-537] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-526] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-604] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-614] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-575] for track '34' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.