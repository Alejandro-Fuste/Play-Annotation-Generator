# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_48`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 64 |
| Player Tracks | 64 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 214 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 98: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [20-70] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-79] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-101] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-162] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-265] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [266-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-147] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-163] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-224] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-358] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-214] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-231] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-284] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-320] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-352] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-79] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-98] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-81] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [104-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-329] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-343] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-60] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-91] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-151] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-219] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-299] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [302-350] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-81] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-258] for track '16' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [20-55] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-46] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [20-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-341] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-84] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-121] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-320] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [326-352] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-170] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-200] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-240] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-264] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-266] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-281] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-338] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-282] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-186] for track '31' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [189-309] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-339] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-232] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [233-249] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [252-253] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-294] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [299-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-267] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-301] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-359] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-213] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-327] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-349] for track '44' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [223-350] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-255] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-353] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-280] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-343] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-290] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-309] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-305] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-323] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-339] for track '55' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [351-353] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-335] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-359] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-354] for track '59' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.