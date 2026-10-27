# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_174`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_174/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '0' (WR2) duration 93 frames exceeds threshold 90 frames [start=230, end=322].
> - Validation warning: Action 'Action_DownBlock' for track '5' (WR1) duration 93 frames exceeds threshold 90 frames [start=230, end=322].
> - Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 93 frames exceeds threshold 90 frames [start=230, end=322].
> - Action 'Action_PreSnap' range [0-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [230-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [248-305] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-375] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-67] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-327] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-350] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-348] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-229] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-335] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-357] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-293] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [280-424] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [428-514] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-366] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-503] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-539] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-351] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-280] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-298] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-255] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-338] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [230-261] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [264-275] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [278-322] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-395] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [230-245] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [250-279] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-270] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-294] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-354] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-310] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-393] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-387] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-346] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-415] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-421] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-358] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-389] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [391-392] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-539] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-426] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-466] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-428] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-512] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-517] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-444] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-474] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [459-500] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-499] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-518] for track '44' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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