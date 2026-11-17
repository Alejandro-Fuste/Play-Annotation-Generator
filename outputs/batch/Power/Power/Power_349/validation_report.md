# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_349`
- **Input XML**: `outputs/batch/Power/Power/Power_349/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 161 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Segment 'Action_DownBlock' for track '14' has invalid range: start=303, end=302. Clamping end to start.
> - Segment 'Action_DownBlock' for track '20' has invalid range: start=303, end=297. Clamping end to start.
> - Action 'Action_PreSnap' range [20-415] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-513] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [521-527] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-417] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-337] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-358] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-539] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-361] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-379] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-418] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-429] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-371] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-394] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-401] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-480] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-484] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [486-489] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [497-526] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [528-535] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [537-539] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-421] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-449] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [451-468] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [470-474] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-478] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-361] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-364] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-377] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-420] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-539] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-394] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-404] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-447] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-288] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-301] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-288] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-301] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-38] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-458] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [467-481] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-302] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-356] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-369] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-391] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-395] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-46] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-61] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-282] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-302] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-393] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-401] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-444] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [446-450] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-282] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-157] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-289] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-301] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-64] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-288] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-297] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-286] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-302] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [320-327] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [330-343] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [347-356] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-337] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-341] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-356] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-372] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-331] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-370] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-375] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-386] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-401] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-384] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-396] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-400] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-418] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-470] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-497] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-428] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-517] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [523-526] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [533-535] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-514] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [519-526] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [533-535] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-418] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-457] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [459-467] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [469-478] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-488] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-400] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-418] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [422-455] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [459-460] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-478] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-524] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-400] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-415] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [417-418] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-418] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-539] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-418] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-473] for track '35' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [481-490] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [427-448] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [451-513] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [438-444] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [447-456] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [459-473] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-484] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [465-468] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [486-499] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [511-512] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [535-539] for track '43' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.