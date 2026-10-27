# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_306`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_306/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [79–93], lower_priority='Action_DownBlock' annotated_start=82, effective_Action_DownBlock_start=94.
> - Action 'Action_None' range [79-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-146] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-193] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [82-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [117-167] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-124] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-164] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [79-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [103-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-249] for track '14' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-127] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-233] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-169] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-166] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-221] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-246] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-329] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-207] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-263] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-273] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-295] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-319] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-285] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-298] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-320] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.