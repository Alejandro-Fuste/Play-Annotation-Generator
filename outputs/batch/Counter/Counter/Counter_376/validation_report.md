# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_376`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_376/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Segment 'Action_BallCarry' for track '5' has invalid range: start=446, end=172. Clamping end to start.
> - Segment 'Action_BallSnap' for track '10' has invalid range: start=400, end=88. Clamping end to start.
> - Segment 'Action_DownBlock' for track '10' has invalid range: start=403, end=88. Clamping end to start.
> - Action 'Action_DownBlock' range [403-429] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [431-432] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-539] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-599] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [403-452] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [457-469] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-428] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-434] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-497] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-266] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-284] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [423-434] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [438-441] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-248] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-255] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-406] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-452] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-514] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-399] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-445] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [403-430] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [442-474] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-531] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-540] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-561] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-576] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-437] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-580] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-414] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [403-414] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [416-419] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [421-427] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [430-445] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [448-487] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [493-528] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-297] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-303] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-423] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-354] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-376] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-397] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-486] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-499] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-493] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-429] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-501] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-494] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-513] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [517-569] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-499] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [501-571] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-543] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-572] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-576] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-519] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [522-586] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-548] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-558] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-554] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-562] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-599] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [545-553] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-556] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-587] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.