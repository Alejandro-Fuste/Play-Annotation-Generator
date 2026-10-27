# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_234`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 179 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 470: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 470: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '15' (Unknown) duration 126 frames exceeds threshold 90 frames [start=401, end=526].
> - Action 'Action_None' range [400-487] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-514] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-425] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [454-479] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-512] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-546] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [432-448] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-488] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-435] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-459] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-464] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-482] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-503] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-518] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-529] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-534] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-559] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-487] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-551] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [553-587] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [590-591] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-599] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-504] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-537] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [401-410] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [475-476] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [401-421] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [424-425] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-448] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-468] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [403-444] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-482] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-407] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-421] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-454] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-318] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [401-413] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [440-507] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-567] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-42] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-224] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-366] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [401-405] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [410-411] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-49] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-77] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-135] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-161] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-244] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-270] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-279] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-283] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-304] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-326] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-425] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-280] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-305] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-317] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-338] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [400-414] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-436] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-447] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-272] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-281] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-300] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-318] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-403] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-399] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [400-403] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-543] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-427] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-435] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-519] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-529] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-597] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-431] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-468] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-485] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-517] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-494] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-517] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [520-533] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-543] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-489] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-528] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-562] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-566] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-581] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [521-595] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [527-540] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-548] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-559] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [561-562] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-572] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-599] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-548] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-596] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-547] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-567] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-577] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-572] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-591] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-559] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-561] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-572] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-586] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [588-591] for track '44' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.