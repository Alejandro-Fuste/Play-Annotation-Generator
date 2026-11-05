# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_94`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 166 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 189: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_LongSnap' range [78-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-153] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-358] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [365-367] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-298] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-341] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-349] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [359-415] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-266] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-307] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-392] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-421] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-285] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-326] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-139] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-307] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-332] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-378] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-304] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-294] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-134] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-104] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-327] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-367] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-517] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [519-521] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 552, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [552-552] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-306] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [308-355] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-276] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-341] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-301] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-367] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-381] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_CatchPunt' range [234-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [261-318] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [324-331] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [335-340] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [360-400] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-261] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-384] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-289] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [347-409] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-229] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-258] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-341] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-375] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-258] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-401] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-327] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-365] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-282] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-343] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-330] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-350] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-367] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-388] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-362] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-423] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-566] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-389] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [380-382] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-394] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-407] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-505] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-512] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-515] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-519] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-524] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-531] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-553] for track '46' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.