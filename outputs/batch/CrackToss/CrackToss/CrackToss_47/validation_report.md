# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_47`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 200 targets track ID '227', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 96: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 96: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 96: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '16' (TE1) duration 118 frames exceeds threshold 90 frames [start=141, end=258].
> - Validation warning: Action 'Action_PullBlock' for track '20' (RT) duration 156 frames exceeds threshold 90 frames [start=141, end=296].
> - Action 'Action_None' range [138-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-250] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-229] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-194] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-253] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-275] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-261] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-290] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-264] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-286] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-239] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [257-263] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-194] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-178] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-286] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [141-258] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [141-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [181-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [255-258] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-179] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [181-194] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [197-266] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-277] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-178] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-268] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-293] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-178] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [141-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [181-255] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [263-264] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [267-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [270-296] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-137] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-250] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-272] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-261] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '25' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.