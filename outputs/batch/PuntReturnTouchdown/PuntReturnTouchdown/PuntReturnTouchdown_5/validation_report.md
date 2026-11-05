# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_5`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 195 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [54-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-175] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-189] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-531] for track '0' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [54-268] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-339] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-549] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-363] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-278] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-365] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-377] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-555] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-513] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-185] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-201] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-383] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [386-397] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-412] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-343] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-203] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-254] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-313] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-316] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [100-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-355] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-249] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-257] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-340] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-460] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-125] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-167] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-298] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-378] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-137] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-569] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-163] for track '23' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-254] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-438] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-259] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-280] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-294] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-424] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-271] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-413] for track '31' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [415-422] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-281] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-298] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-502] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-372] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-387] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [373-377] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-395] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-415] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-429] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-442] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-440] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-495] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-542] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-551] for track '45' has 1 frames without a visible bounding box.
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