# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_54`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action 'Action_None' range [9-472] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-574] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [577-578] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-455] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-583] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-440] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-516] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-516] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-328] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-415] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-481] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [483-490] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-522] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-530] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-629] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-542] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-394] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-588] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-282] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-452] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-467] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [470-471] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-484] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [503-619] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-625] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-325] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-334] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-264] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-305] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-402] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [420-477] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [479-480] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [509-519] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [521-530] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [542-619] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [9-576] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-588] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [597-598] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-418] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-319] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-629] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-393] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-629] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-498] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-550] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-328] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [332-334] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-334] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-417] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [422-442] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-478] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-497] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-618] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-368] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-477] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-543] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-400] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-415] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-421] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-411] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-416] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-462] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [464-480] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [485-500] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [504-511] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-515] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-528] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-532] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-421] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-506] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-514] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [519-521] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-526] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-544] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-548] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-556] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-559] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-591] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-452] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-450] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-458] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-506] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [509-514] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-629] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-541] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-629] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-629] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [539-556] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-599] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-629] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [548-556] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-555] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-608] for track '47' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [611-615] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [617-620] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-595] for track '48' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.