# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_99`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 129 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-223] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-371] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 226, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [226-226] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-240] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-259] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-245] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-323] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-419] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-419] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-253] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [178-231] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-306] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-395] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-309] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-257] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-281] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-375] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [188-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [224-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-58] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-76] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [183-204] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-245] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-378] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-419] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-254] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-257] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-302] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-345] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-357] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-369] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-395] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-351] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-365] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-323] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-333] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-363] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-323] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-395] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-403] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-331] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-377] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-419] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-341] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-354] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-419] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-365] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-371] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-375] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-375] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-388] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-373] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-395] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-383] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-419] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-383] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-398] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-413] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-419] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-408] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-414] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-417] for track '53' has 1 frames without a visible bounding box.
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
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.