# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_88`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 47 for track '12': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
> - Action 'Action_None' range [47-95] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [47-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [121-125] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [47-81] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.