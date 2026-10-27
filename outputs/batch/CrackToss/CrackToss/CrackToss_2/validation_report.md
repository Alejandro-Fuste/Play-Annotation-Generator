# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_2`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 51 |
| Ball Tracks | 2 |
| CSV events parsed | 19 |
| Action Segments inferred | 137 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 538 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 538 as fallback play end.
> - Segment 'Action_BallCarry' for track '6' has invalid range: start=79, end=10. Clamping end to start.
> - Segment 'Action_PullBlock' for track '7' has invalid range: start=52, end=5. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '12' has invalid range: start=42, end=10. Clamping end to start.
> - Segment 'Action_Toss' for track '12' has invalid range: start=59, end=10. Clamping end to start.
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=42, end=10. Clamping end to start.
> - Action 'Action_None' range [42-448] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-350] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-362] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-370] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-310] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-486] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-338] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-353] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-503] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-338] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [340-380] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-383] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-479] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-10] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-352] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-538] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-310] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-454] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-425] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-273] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-308] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-320] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-407] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [411-413] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-287] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-173] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-528] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-324] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-80] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-111] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-123] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-304] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [388-473] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [476-515] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-135] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-212] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-322] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [324-395] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-508] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-371] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-398] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [401-426] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-434] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-331] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-500] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [320-350] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-357] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-368] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-386] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-337] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-396] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-443] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-374] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-442] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-392] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-457] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-414] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-418] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-419] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-430] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-455] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-490] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [415-419] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-453] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-420] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-422] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-445] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-449] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-452] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-452] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-455] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-463] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-481] for track '52' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [483-486] for track '52' has 1 frames without a visible bounding box.
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
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.