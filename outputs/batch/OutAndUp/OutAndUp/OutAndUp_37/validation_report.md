# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_37`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 168 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [2–8], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=9.
> - Action 'Action_SellOut' range [68-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [73-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [93-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [255-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-63] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-99] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-177] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-236] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-84] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-213] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-184] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-73] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-85] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-227] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-46] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-240] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-57] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-250] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-146] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [155-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [199-266] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-121] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-218] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [220-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [225-241] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [246-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-57] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-198] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [206-258] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-37] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-60] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-123] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-136] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [145-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [155-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [166-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [175-221] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-262] for track '24' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-153] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-265] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-188] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-241] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-215] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-255] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-258] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-250] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-251] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-263] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-251] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-268] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '48' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-269] for track '49' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.