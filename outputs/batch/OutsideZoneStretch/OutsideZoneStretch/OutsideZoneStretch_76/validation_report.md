# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_76`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 147 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 154: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Segment 'Action_Handoff' for track '16' has invalid range: start=199, end=107. Clamping end to start.
> - Action 'Action_PreSnap' range [0-57] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-270] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-284] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-296] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-328] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-246] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-295] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-307] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-335] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-314] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [316-321] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-336] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-517] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [519-539] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-233] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-319] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-449] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-197] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-111] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-147] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-360] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-292] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-233] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-273] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-113] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-196] for track '13' has 9 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-241] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-283] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-311] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-315] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-319] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-229] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-424] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [481-490] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [492-537] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-288] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-283] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-443] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-264] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-273] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-279] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-321] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-292] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-298] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-251] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-307] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-271] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-285] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-425] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [429-433] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-437] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [439-539] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-331] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-355] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-367] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-375] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-437] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [447-449] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [453-506] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-338] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-331] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-422] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-539] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-313] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-307] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-539] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-372] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-464] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [470-472] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-469] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-482] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [493-496] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [498-539] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-507] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [513-525] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [536-539] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-382] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-474] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-477] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [481-515] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-539] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-404] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-467] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-404] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-426] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-473] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-482] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [488-493] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [434-482] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [488-490] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [436-452] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [468-487] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-482] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [498-500] for track '48' has 1 frames without a visible bounding box.
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