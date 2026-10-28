# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_7`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [58–75], lower_priority='Action_PassBlock' annotated_start=61, effective_Action_PassBlock_start=76.
> - Action 'Action_None' range [58-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-246] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [58-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-309] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-278] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-136] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-279] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-317] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-85] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-321] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-136] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-285] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-130] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-289] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-329] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [134-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-275] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.