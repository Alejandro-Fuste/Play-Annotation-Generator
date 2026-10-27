# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_56`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=183, end=144. Clamping end to start.
> - Action 'Action_PreSnap' range [0-189] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-196] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [199-348] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [354-355] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-251] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-342] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-336] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-359] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [160-206] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-187] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-241] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-208] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-359] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_Handoff' range [157-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-255] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [135-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [176-191] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-167] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-328] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-346] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-298] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-262] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-359] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-334] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.