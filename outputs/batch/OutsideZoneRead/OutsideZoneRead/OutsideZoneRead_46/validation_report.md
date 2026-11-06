# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_46`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 57 |
| Player Tracks | 57 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 231 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 94: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 94: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 94: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Overlapping action conflict at frame 82 for track '12': 'Action_PressEdge' vs 'Action_ReadEdgeDefender'. Overriding with 'Action_ReadEdgeDefender'.
> - Action 'Action_PreSnap' range [0-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-290] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-479] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-200] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-279] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-283] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-306] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-479] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-118] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-281] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-474] for track '5' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-443] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [453-468] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-190] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-244] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-251] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-278] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-419] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-472] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-251] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-369] for track '11' has 8 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-409] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-413] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-419] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-427] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [429-452] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [458-479] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-107] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 126, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [126-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-288] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-306] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-322] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-413] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-421] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-424] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-433] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-449] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-460] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-245] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-288] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-368] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-476] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-128] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-433] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-450] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-103] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-118] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 126, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [126-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-479] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-251] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-268] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-60] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-85] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-479] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-353] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-368] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-394] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-399] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-241] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-337] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-356] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-479] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-288] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-323] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-335] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-341] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-472] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-218] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-288] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-305] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-321] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-236] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-246] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-284] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-300] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-306] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-320] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-331] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-466] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-276] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-306] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-321] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-339] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-343] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-355] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-358] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-388] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-479] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-279] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-290] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-306] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-325] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-331] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-361] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-390] for track '43' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-409] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-441] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [443-479] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-306] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-313] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-321] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-369] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-375] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-385] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-388] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-391] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-307] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-324] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-333] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-349] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-427] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-402] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-428] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-428] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-457] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [459-460] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [467-468] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [475-477] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [450-452] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [464-465] for track '56' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.