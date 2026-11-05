# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_64`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 61 |
| Player Tracks | 61 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 146 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 130: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [34-65] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-234] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-453] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-464] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-581] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-355] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-394] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [399-401] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-446] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-470] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-363] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-370] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-107] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [34-364] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-112] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-140] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-359] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-367] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-173] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-268] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-352] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-401] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-407] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-561] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-565] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-410] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-313] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-599] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-228] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-193] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-316] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-343] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-361] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [363-395] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [397-421] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-270] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-307] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-364] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-467] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-332] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-464] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-363] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-373] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-453] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-383] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-384] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-445] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-562] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-569] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-576] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-491] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-521] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-539] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-589] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-435] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-458] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [434-437] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [462-463] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-516] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-512] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [511-515] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [517-529] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [515-525] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-533] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [520-528] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-529] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [534-539] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-548] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-557] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-564] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-561] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-565] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [568-589] for track '56' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [591-599] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-571] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-579] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-593] for track '60' has 3 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.