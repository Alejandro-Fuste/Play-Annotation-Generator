# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_41`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 180 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 568 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 568 as fallback play end.
> - Segment 'Action_BreakInside' for track '4' has invalid range: start=389, end=387. Clamping end to start.
> - Segment 'Action_PassBlock' for track '9' has invalid range: start=377, end=140. Clamping end to start.
> - Segment 'Action_PassBlock' for track '15' has invalid range: start=377, end=376. Clamping end to start.
> - Segment 'Action_PassBlock' for track '18' has invalid range: start=377, end=108. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '20' has invalid range: start=374, end=215. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '20' has invalid range: start=452, end=215. Clamping end to start.
> - Action 'Action_None' range [374-399] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-408] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [414-430] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-421] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [426-434] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [436-439] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-457] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-473] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-488] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-503] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-506] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-544] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-410] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-433] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-445] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [511-512] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-424] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-387] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-428] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-404] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-474] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-493] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-505] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-508] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-514] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-536] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [540-541] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-568] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-270] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-284] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-304] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-318] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-404] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-430] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-213] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-238] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-259] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-382] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ClearToEdge' range [404-405] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-255] for track '15' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-369] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [374-376] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-182] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-204] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-256] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-293] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-346] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-351] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-373] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-379] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-404] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-421] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-433] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-438] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-43] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-215] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-290] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-373] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-384] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-500] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [514-532] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-373] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-417] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-373] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-404] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-422] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-373] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-377] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-432] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-369] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-498] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-365] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-369] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '27' starts at frame 374, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [374-377] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-398] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-363] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-385] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-402] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [407-410] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-421] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [423-424] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-369] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-405] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-414] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-435] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-386] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-399] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-403] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-404] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-440] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-410] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-434] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-453] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-461] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-476] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-505] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-463] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-474] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-568] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-476] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-475] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-553] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-524] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-526] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-529] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-561] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [527-529] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-552] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-568] for track '48' has 2 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.