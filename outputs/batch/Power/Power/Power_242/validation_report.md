# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_242`
- **Input XML**: `outputs/batch/Power/Power/Power_242/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 486: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 486: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action 'Action_PreSnap' range [4-413] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [417-464] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [474-500] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [505-528] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-420] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-472] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-499] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [501-599] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-418] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-458] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [462-496] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [428-439] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-478] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-241] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-251] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-471] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-415] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-493] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [388-404] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-472] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-515] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [531-533] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-536] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-561] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-567] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [388-414] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-471] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [477-487] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-511] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-591] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-474] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-100] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-284] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-318] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-322] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-410] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-432] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [453-455] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [462-471] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-488] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [490-491] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [505-523] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-296] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-310] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-388] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [388-400] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-462] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-532] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-393] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-403] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-413] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-419] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [422-472] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [481-483] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [485-505] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [507-550] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [557-559] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-466] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [470-552] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [557-559] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [561-591] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-443] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-425] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [453-475] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-531] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [536-559] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [500-501] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [504-543] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [508-561] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [510-519] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [510-565] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [574-595] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [518-566] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [555-572] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [577-578] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [575-599] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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