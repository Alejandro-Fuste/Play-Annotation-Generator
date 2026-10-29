# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_51`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 76 |
| Player Tracks | 76 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 216 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-233] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-306] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-311] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-352] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [200-229] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-66] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-213] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-246] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-274] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-330] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-68] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-21] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-40] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-78] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-64] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-51] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-67] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-7] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-53] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-28] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-51] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-16] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-52] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-67] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-79] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-329] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-341] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-110] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-130] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-143] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-113] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-117] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-181] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-351] for track '32' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-152] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-170] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-186] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-199] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-261] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-271] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-300] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-221] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-359] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-178] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-329] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-335] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-359] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-251] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-261] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-206] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-224] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-241] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-259] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-278] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-285] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-323] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-340] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-355] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-359] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-226] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-240] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-279] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-291] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-298] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-307] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-259] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-270] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-301] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-331] for track '51' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-349] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-295] for track '52' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-251] for track '53' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-278] for track '53' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-288] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-359] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-239] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-258] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-236] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-252] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-273] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-288] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-296] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-312] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-322] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-330] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-359] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-277] for track '57' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-258] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-269] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-279] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-319] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-359] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-277] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-289] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-296] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-314] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-320] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-338] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-343] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-349] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-355] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-291] for track '66' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-297] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-328] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-352] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-279] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-295] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-311] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-342] for track '71' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-329] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-331] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-336] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-359] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-344] for track '75' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Player track '71' has undefined position. Will map to Position_Unknown.
> - Player track '71' has undefined team_side. Will map to Team_Unknown.
> - Player track '72' has undefined position. Will map to Position_Unknown.
> - Player track '72' has undefined team_side. Will map to Team_Unknown.
> - Player track '73' has undefined position. Will map to Position_Unknown.
> - Player track '73' has undefined team_side. Will map to Team_Unknown.
> - Player track '74' has undefined position. Will map to Position_Unknown.
> - Player track '74' has undefined team_side. Will map to Team_Unknown.
> - Player track '75' has undefined position. Will map to Position_Unknown.
> - Player track '75' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.