# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_31`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [201–225], lower_priority='Action_DownBlock' annotated_start=207, effective_Action_DownBlock_start=226.
> - Action 'Action_None' range [201-381] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-262] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-331] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-285] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-389] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [201-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [233-236] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-241] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-294] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-307] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [207-287] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-366] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [207-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-368] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-297] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [304-348] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-354] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-349] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [356-389] for track '27' has 1 frames without a visible bounding box.
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