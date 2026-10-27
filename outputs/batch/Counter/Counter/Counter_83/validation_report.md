# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_83`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [144–156], lower_priority='Action_PullBlock' annotated_start=151, effective_Action_PullBlock_start=157.
> - Action 'Action_None' range [144-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [191-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [151-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-171] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [157-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-53] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-83] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-113] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.