# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_88`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 178: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [86-539] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-72] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-353] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-384] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-370] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-456] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-482] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-290] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-368] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-405] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-416] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-340] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-360] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-382] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-507] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-43] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-268] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-373] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [385-387] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-423] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-533] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-55] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-539] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-74] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-475] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-486] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-109] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-172] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-332] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-358] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-279] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-530] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-293] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-341] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-296] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-419] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-265] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-245] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-461] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-469] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [472-494] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [501-504] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-512] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-424] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-461] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-534] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [418-426] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-435] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-423] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-428] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-437] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-464] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-442] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-437] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-448] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-455] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-437] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-437] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-482] for track '50' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [486-488] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-494] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [496-497] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-468] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [470-471] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-501] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-468] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-500] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-518] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-521] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-509] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-518] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-530] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-537] for track '57' has 1 frames without a visible bounding box.
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
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.