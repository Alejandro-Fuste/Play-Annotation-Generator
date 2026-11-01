# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_171`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 127 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Segment 'Action_BallCarry' for track '0' has invalid range: start=446, end=240. Clamping end to start.
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=400, end=297. Clamping end to start.
> - Action 'Action_PreSnap' range [0-240] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [402-411] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [413-430] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [435-444] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-573] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-588] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [402-420] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 479, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [479-479] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-599] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-433] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-461] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-255] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [402-444] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-189] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-377] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-410] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-492] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-495] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-454] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [458-468] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-599] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [402-434] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-305] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-319] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-405] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-514] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-436] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-443] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-469] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-540] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-581] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-223] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-297] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-424] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-466] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-483] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-396] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-445] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-500] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-455] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-470] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-548] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-433] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-568] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-436] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-446] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-470] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-452] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-460] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-571] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-498] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-529] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-533] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-456] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-485] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-461] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-479] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-489] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-537] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [540-542] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-599] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-585] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-596] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-494] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-518] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [521-522] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-573] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [581-582] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-559] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-520] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-576] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [524-534] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-599] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-568] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-581] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-581] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [589-590] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-599] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [597-599] for track '42' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.