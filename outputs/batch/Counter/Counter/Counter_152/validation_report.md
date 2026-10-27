# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_152`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_152/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 157 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Overlapping action conflict at frame 126 for track '1': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
> - Segment 'Action_PullBlock' for track '6' has invalid range: start=126, end=114. Clamping end to start.
> - Action 'Action_None' range [123-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-220] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-249] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [126-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [172-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [189-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-292] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-276] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-213] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-276] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-25] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-197] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-246] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-257] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-283] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-13] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-20] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-91] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [123-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [168-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-200] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-312] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-332] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-221] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-249] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-128] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-274] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-233] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-294] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-292] for track '17' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [169-266] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-286] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-222] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-274] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [278-298] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-223] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-307] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-260] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-237] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-247] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-273] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-304] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-354] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-271] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-276] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-284] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-297] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-352] for track '36' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.