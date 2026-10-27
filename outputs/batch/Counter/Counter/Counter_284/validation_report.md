# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_284`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_284/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [57-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-111] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [60-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [91-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-285] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [294-295] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-281] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [60-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-94] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-299] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [71-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-105] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-213] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-297] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-297] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-172] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-297] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-297] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-294] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-271] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-297] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-285] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-289] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-292] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-295] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '43' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.