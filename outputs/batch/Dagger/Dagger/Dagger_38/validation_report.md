# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_38`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 165 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 538 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 40: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 538 as fallback play end.
> - Segment 'Action_SnapReceive' for track '14' has invalid range: start=329, end=7. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '14' has invalid range: start=418, end=7. Clamping end to start.
> - Segment 'Action_PassBlock' for track '15' has invalid range: start=332, end=150. Clamping end to start.
> - Action 'Action_None' range [329-389] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-455] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [458-472] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-538] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-421] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [424-428] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-439] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-444] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-375] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-479] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-491] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [493-494] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-499] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-467] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [471-521] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-537] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-377] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BreakInside' range [354-475] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-49] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-87] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-93] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-339] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ClearToEdge' range [354-406] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-447] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-467] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [470-471] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-70] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-328] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-403] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-47] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-56] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' for track '16' starts at frame 329, but the player has no visible bounding box on this frame.
> - Action 'Action_BallSnap' range [329-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-145] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-161] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-367] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [369-426] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-451] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-259] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-271] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-279] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-395] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-403] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-410] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-355] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-410] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-349] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-365] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-403] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-355] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-375] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [377-387] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-398] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-451] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-455] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-355] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-401] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [352-367] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-403] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [450-451] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-434] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-538] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-387] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-387] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-406] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-447] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-455] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-471] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [450-455] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-464] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-498] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-455] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-462] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-455] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-460] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-479] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-520] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-455] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-458] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-489] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-534] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [481-501] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-504] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-513] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-517] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-491] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-486] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [488-508] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [483-484] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-489] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-495] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-511] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [489-501] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-495] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-519] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [532-533] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-503] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-503] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-496] for track '50' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.