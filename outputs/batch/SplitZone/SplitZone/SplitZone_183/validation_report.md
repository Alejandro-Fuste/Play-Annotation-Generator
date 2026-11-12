# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_183`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_183/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 165 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 368: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [307–322], lower_priority='Action_ZoneBlock' annotated_start=310, effective_Action_ZoneBlock_start=323.
> - Action 'Action_None' range [307-569] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-543] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [548-556] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-559] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-563] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-424] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-334] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-362] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-388] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-478] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-569] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [339-405] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [408-479] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [481-489] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [491-493] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [499-502] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [513-514] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [526-528] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [531-537] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [539-552] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-397] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-458] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-464] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-474] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-491] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-524] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [331-399] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-456] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-461] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-475] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-488] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-494] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-500] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-558] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-440] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-358] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-388] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-432] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [339-425] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-451] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-569] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-562] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [310-331] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [335-361] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-430] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [436-458] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-464] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-484] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [307-318] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [323-333] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-482] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [484-485] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-498] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [501-506] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [510-539] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [542-563] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-466] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [468-473] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-478] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-506] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-519] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-535] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-403] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [310-399] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [310-315] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [318-332] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [334-356] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-434] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-446] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [455-504] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-569] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-390] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-438] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-425] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [428-438] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-475] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [481-501] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [503-519] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-465] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-453] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-533] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-559] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [562-568] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-465] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-475] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-482] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-494] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [477-496] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-518] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [526-546] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [548-558] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [561-569] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-488] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-514] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-544] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-549] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-554] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-557] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-486] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-492] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-499] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-508] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-534] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [536-537] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-569] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-543] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-568] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [512-516] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-524] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-530] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-538] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-547] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [556-569] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [542-544] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-563] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-569] for track '47' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.