# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_17`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 129 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Segment 'Action_BallCarry' for track '17' has invalid range: start=451, end=440. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [410–428], lower_priority='Action_ZoneBlock' annotated_start=412, effective_Action_ZoneBlock_start=429.
> - Action 'Action_None' range [410-548] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-545] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-586] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-504] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-511] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-517] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-520] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-571] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-586] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-588] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-520] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-595] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-453] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-510] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [516-521] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-528] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-437] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-472] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-447] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-450] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-599] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [412-445] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [447-448] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [450-461] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [499-505] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [507-599] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-499] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [505-516] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-63] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-505] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-513] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-519] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-560] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-569] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-591] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [594-595] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-521] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-529] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-539] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-445] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-470] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [410-445] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-511] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [516-519] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-440] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [412-445] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [452-469] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [473-498] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-511] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-534] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-563] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-589] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [429-437] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [440-445] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [492-498] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 499, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [499-499] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-560] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-569] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-586] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-591] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-595] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-501] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-519] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-530] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-567] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-574] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-588] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [412-431] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [442-446] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [450-498] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-473] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-599] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-474] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-489] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-495] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [504-511] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-529] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [534-543] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-562] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-562] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-568] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-587] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-574] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.