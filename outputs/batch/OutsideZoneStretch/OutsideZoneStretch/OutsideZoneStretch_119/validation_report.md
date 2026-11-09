# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_119`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 129 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action 'Action_PreSnap' range [0-445] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-292] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-425] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-291] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-454] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-391] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-396] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-479] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-447] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-444] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-335] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-358] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-370] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-445] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-289] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-307] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-317] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-252] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-444] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-193] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-394] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-426] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [145-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-434] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-278] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-457] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-422] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-343] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-436] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-428] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-263] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-270] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-301] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-324] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-332] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-359] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-374] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-383] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-392] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-397] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-404] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-409] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-419] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-432] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-462] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-426] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-272] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-286] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-311] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-287] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-343] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-409] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-452] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-287] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-292] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-303] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-367] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-378] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-440] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-286] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-417] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-424] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-324] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-441] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-415] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-455] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [451-464] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-479] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [471-475] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.