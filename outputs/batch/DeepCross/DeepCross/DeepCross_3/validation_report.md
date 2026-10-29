# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_3`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 59 |
| Player Tracks | 59 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 187 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 6: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_ThrowPass' for track '15' has invalid range: start=175, end=138. Clamping end to start.
> - Action 'Action_None' range [21-108] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-313] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-41] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-66] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-124] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-208] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-293] for track '2' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [295-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [34-83] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [95-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-64] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-74] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-66] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-328] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-224] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-241] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-251] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-325] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-359] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-56] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-80] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-97] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-133] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [21-177] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-209] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-243] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-66] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-255] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-349] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-66] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-93] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-108] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-66] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-136] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-93] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-108] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-136] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [138-197] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [199-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [211-220] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [224-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-107] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-134] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-214] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-133] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-172] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [21-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-167] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-247] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-265] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-287] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [249-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-249] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-198] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-220] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-197] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-185] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-331] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-253] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-253] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-322] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-351] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-276] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-280] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [283-292] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-306] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-325] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-301] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-323] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-322] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-343] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-339] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [342-345] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-312] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-359] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-353] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-359] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '58' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.