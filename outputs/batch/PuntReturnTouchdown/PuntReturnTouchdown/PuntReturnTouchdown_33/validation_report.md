# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_33`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 191 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [66-243] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-285] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-130] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-175] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-197] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-244] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-283] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [287-291] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-134] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-173] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-188] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-244] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-275] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-291] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-310] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-337] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-354] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-239] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-134] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [66-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [111-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-154] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-217] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-162] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-236] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-355] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-222] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-267] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-321] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-221] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [224-237] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-359] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [190-237] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-263] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-293] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-302] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-340] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-359] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-213] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-220] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-282] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-340] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-359] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-265] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-292] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-304] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-310] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-341] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-359] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-308] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-305] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-311] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-322] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-335] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-359] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-303] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-337] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-341] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-345] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-359] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-321] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-336] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-359] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-342] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-332] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-337] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [347-355] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [329-333] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-348] for track '52' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.