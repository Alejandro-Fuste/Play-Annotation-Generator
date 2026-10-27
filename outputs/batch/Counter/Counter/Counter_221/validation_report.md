# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_221`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_221/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 150 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [213–227], lower_priority='Action_DownBlock' annotated_start=215, effective_Action_DownBlock_start=228.
> - Action 'Action_None' range [213-256] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-322] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-393] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-362] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-417] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-501] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-517] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [522-529] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-537] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-427] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-539] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [215-298] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-355] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [294-355] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-367] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-382] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-388] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-392] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-408] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-508] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-530] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [215-258] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [264-266] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [215-262] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [268-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-338] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-414] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [213-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-324] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [330-369] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-338] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-361] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-370] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-380] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-399] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [406-436] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-445] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-454] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [462-465] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-487] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-503] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-510] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-522] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-528] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [537-538] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-368] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-377] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-388] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-399] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-409] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [414-419] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-439] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-396] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-539] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-408] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-496] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-432] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-436] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-454] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-463] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-477] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-485] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [493-494] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-498] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-505] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-521] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [523-526] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-539] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-436] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-458] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-464] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-458] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-474] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-482] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-493] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-507] for track '41' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [510-511] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-516] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-485] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-495] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [509-511] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-538] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-484] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-518] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-536] for track '44' has 2 frames without a visible bounding box.
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