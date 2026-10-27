# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_73`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [143–153], lower_priority='Action_DownBlock' annotated_start=148, effective_Action_DownBlock_start=154.
> - Action 'Action_None' range [143-226] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [148-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-322] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-282] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [284-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-257] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-265] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-285] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-172] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [177-184] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-264] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-284] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-12] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-35] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [143-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [216-223] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-142] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [179-218] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-188] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-278] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [153-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [163-172] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [184-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [190-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [197-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-279] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-268] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-243] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-303] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-276] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-289] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-309] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-304] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-283] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [287-291] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-311] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-293] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-307] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-327] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-297] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-329] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-307] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-319] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-322] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '44' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.