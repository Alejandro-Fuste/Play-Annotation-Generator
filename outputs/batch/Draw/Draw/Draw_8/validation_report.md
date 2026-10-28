# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_8`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [41–53], lower_priority='Action_PassBlock' annotated_start=44, effective_Action_PassBlock_start=54.
> - Action 'Action_None' range [41-90] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-131] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-329] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-290] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-308] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [81-303] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [305-307] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [321-322] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [324-325] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-86] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-178] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-228] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-259] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-301] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-285] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.