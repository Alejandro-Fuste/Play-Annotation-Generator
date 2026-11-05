# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_55`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 168 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_CatchPunt' for track '39' has invalid range: start=346, end=233. Clamping end to start.
> - Action 'Action_None' range [49-192] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-373] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [376-383] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-417] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [421-479] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [49-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-298] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-302] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-309] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-253] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-262] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-292] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-222] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-268] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-383] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-397] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-312] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-220] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-245] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-451] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-479] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-293] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-311] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-217] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-374] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-383] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-428] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-479] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-264] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-254] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-382] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-402] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-409] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-417] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-439] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-448] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-465] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-268] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-479] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-445] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-394] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-468] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-270] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-479] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-296] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-312] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-358] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-439] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-445] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-309] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-346] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-294] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-376] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-413] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-479] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-308] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-468] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-318] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-313] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-373] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-390] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-400] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-407] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-434] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [436-441] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-479] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-356] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-363] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-376] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-441] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-353] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-373] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-382] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-392] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-396] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-419] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [421-439] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-445] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-403] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [406-438] for track '42' has 3 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.