# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_177`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_177/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [272-276] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-300] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [189-271] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-295] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-309] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-258] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-327] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-247] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-283] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-309] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-321] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [194-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [216-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-263] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-304] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-274] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-257] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-306] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-271] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-253] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-12] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-329] for track '23' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.