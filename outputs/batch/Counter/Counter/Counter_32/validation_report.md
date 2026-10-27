# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_32`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 66: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [182–199], lower_priority='Action_DownBlock' annotated_start=180, effective_Action_DownBlock_start=200.
> - Action 'Action_None' range [182-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [180-219] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-296] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-223] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-233] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-236] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-253] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [180-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [204-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [212-263] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [180-227] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-275] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-321] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-331] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.