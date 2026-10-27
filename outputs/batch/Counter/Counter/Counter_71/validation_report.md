# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_71`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 129 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [100–112], lower_priority='Action_DownBlock' annotated_start=109, effective_Action_DownBlock_start=113.
> - Action 'Action_None' range [100-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-135] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [108-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [141-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [168-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-240] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-286] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-262] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-125] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-119] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-272] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-285] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-133] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-163] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-232] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [109-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [139-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-294] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-230] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-299] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-268] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [282-290] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-299] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-228] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-252] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-299] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-299] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-277] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-285] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-293] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '38' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.