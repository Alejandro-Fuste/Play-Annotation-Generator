# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_36`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 131 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '7' (TE1) duration 104 frames exceeds threshold 90 frames [start=77, end=180].
> - Validation warning: Action 'Action_DownBlock' for track '12' (RG) duration 104 frames exceeds threshold 90 frames [start=77, end=180].
> - Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 100 frames exceeds threshold 90 frames [start=77, end=176].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [74–85], lower_priority='Action_DownBlock' annotated_start=77, effective_Action_DownBlock_start=86.
> - Action 'Action_PullLeadBlock' range [77-120] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-303] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-313] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-293] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-225] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [77-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-244] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-319] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-131] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-161] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [77-124] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-129] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-190] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-322] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-27] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-127] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-205] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-116] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-251] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-318] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-229] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-261] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-313] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-329] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-276] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [282-303] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-314] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-322] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-277] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-322] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-304] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-319] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.