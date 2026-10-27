# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_248`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_248/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 498: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '5' (LT) duration 98 frames exceeds threshold 90 frames [start=104, end=201].
> - Validation warning: Action 'Action_PullBlock' for track '14' (RG) duration 103 frames exceeds threshold 90 frames [start=104, end=206].
> - Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 95 frames exceeds threshold 90 frames [start=104, end=198].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [102–115], lower_priority='Action_DownBlock' annotated_start=104, effective_Action_DownBlock_start=116.
> - Action 'Action_None' range [102-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-138] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-233] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-195] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-223] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-139] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-189] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [104-163] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-128] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-141] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-248] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-186] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-223] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [104-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [124-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [131-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [135-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-181] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-137] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-145] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-169] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-194] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [196-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-316] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-172] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-209] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-328] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-221] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-252] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-327] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-298] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-323] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-317] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '39' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.